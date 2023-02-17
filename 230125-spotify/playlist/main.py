import os
import sys
import base64
import requests
from typing import Optional
from PyQt6.QtWidgets import QApplication
from auth_window import AuthWindow
from playlist_window import PlaylistWindow

client_id = ''
client_secret = ''

app = QApplication(sys.argv)
auth_window = AuthWindow()
playlist_window = PlaylistWindow()


def generate_token(code: str) -> str | None:
    credentials = base64.b64encode(
        client_id.encode()
        + b':'
        + client_secret.encode()
    ).decode('utf-8')

    token_headers = {
        'Authorization': 'Basic ' + credentials,
        'content-type': 'application/x-www-form-urlencoded'
    }

    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:7777/callback'
    }

    token_response = requests.post(
        'https://accounts.spotify.com/api/token',
        data=token_data,
        headers=token_headers
    ).json()

    if os.path.isfile('../code.txt'):
        os.remove('../code.txt')

    if 'error' in token_response:
        return None
    else:
        token = token_response['access_token']
        file = open('../token.txt', 'w')
        file.write(token)
        file.close()

        return token


def get_code() -> str | None:
    if os.path.isfile('../code.txt'):
        file = open('../code.txt')
        code = file.read()
        file.close()
        return code

    return None


def get_token() -> str | None:
    if os.path.isfile('../token.txt'):
        file = open('../token.txt')
        token = file.read()
        file.close()
        return token
    elif os.path.isfile('../code.txt'):
        code = get_code()
        if code is None:
            return None
        else:
            return get_token()


def check_permissions() -> str | None:
    user_id: Optional[str] = None
    token = get_token()

    if token is not None:
        user_headers = {
            'Authorization': 'Bearer ' + token,
            'Content-type': 'application/json'
        }
        user_profile_response = requests.get(
            'https://api.spotify.com/v1/me',
            headers=user_headers
        ).json()

        if not ('error' in user_profile_response):
            user_id = user_profile_response['id']
        elif 'error' in user_profile_response and os.path.isfile('../token.txt'):
            os.remove('../token.txt')

    return user_id


def main():
    user_id = check_permissions()
    if user_id is None:
        auth_window.show()
    else:
        playlist_window.show()

    app.exec()


main()
