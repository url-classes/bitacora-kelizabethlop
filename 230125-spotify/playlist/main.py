import os
import sys
import base64
import requests
from typing import Optional
from PyQt6.QtWidgets import QApplication
from auth_window import AuthWindow

client_id = '2d7800dcec2241389843e017b8ab5e4d'
client_secret = '418d5f1d798842fc924c28c8bf6f4124'

app = QApplication(sys.argv)
auth_window = AuthWindow()
user_id: Optional[str] = None


def check_permissions():
    global user_id
    if os.path.isfile('../token.txt'):
        # Verificar si el token sigue siendo valido
        f = open('../token.txt', 'r')
        token = f.read()
        f.close()
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
        else:
            print('Error...')

    elif os.path.isfile('../code.txt'):
        # Verificar si el codigo es valido
        f = open('../code.txt', 'r')
        code = f.read()
        f.close()
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

        r = requests.post(
            'https://accounts.spotify.com/api/token',
            data=token_data,
            headers=token_headers
        ).json()

        if 'error' in r:
            print('Su código de acceso a expirado.')
            print('Vuelva a acceder a http://localhost:7777/authorize')
        else:
            token = r['access_token']
            f = open('../token.txt', 'w')
            f.write(token)
            f.close()
            print('El token de acceso ha sido generado.')

        try:
            os.remove('../code.txt')
            print('El archivo ../code.txt ha sido eliminado')
        except Exception as error:
            print('No puede eliminar el archivo ../code.txt')
            print('Error:', error)


def main():
    auth_window.show()
    app.exec()


main()
