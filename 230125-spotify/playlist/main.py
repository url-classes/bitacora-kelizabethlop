import os
import sys
import base64
import requests
from PyQt6.QtWidgets import QApplication
from auth_window import AuthWindow
from playlist_window import PlaylistWindow
from communicate import Communicate
from search_window import SearchWindow

client_id = '2d7800dcec2241389843e017b8ab5e4d'
client_secret = '418d5f1d798842fc924c28c8bf6f4124'

app = QApplication(sys.argv)
communicate = Communicate()
auth_window = AuthWindow(communicate)
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
            # Solicitar entrar localhost:7777/authorize
            return None
        else:
            token = generate_token(code)
            return token


def check_permissions() -> str | None:
    user_id: str | None = None
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


playlist_window = PlaylistWindow(token=get_token(), user_id=check_permissions())
search_window = SearchWindow(token=get_token(), user_id=check_permissions())


def load_window():
    user_id = check_permissions()
    if user_id is None:
        playlist_window.close()
        auth_window.show()
    else:
        auth_window.close()
        token = get_token()
        playlist_window.load_ui(token, user_id)


def main():
    auth_window.close()
    playlist_window.close()

    load_window()

    communicate.verify_code.connect(load_window)

    app.exec()


main()
