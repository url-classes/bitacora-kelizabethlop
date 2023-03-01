import os
import requests
import base64
from playlist.main import client_id, client_secret

while True:
    if os.path.isfile('../token.txt'):
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

        if 'error' in user_profile_response:
            print(user_profile_response['error']['message'])
            os.remove('../token.txt')
            print('El archivo ../token.txt ha sido eliminado')
        else:
            user_id = user_profile_response['id']
            user_uri = user_profile_response['uri']
            if os.path.isfile('../playlist.txt'):
                f = open('../playlist.txt', 'r')
                playlist_id = f.read()
                f.close()
                endpoint = f'https://api.spotify.com/v1/playlists/{playlist_id}'
                get_playlist_response = requests.get(
                    endpoint,
                    headers=user_headers
                ).json()
                playlist_id = get_playlist_response['id']
                playlist_uri = get_playlist_response['uri']
                print('Playlist ID:', playlist_id)
                print('Playlist URI:', playlist_uri)

                endpoint = 'https://api.spotify.com/v1/search'
                search_response = requests.get(
                    endpoint,
                    headers=user_headers,
                    params={
                        'q': 'Bad bunny',
                        'type': 'album,track',
                        'limit': 5,
                        'include_external': 'audio'
                    }
                ).json()
                print('Resultados de la búsqueda:')
                tracks = search_response['tracks']['items']
                # duration_ms
                # ID
                # name
                canciones = []
                for track in tracks:
                    print(track['id'])
                    print(track['name'])
            else:
                endpoint = f'https://api.spotify.com/v1/users/{user_id}/playlists'
                body = {
                    "name": "Mi nueva playlist",
                    "description": "Esta playlist es del curso de Estructura de Datos I"
                }

                create_playlist_response = requests.post(
                    endpoint,
                    json=body,
                    headers=user_headers
                ).json()

                playlist_id = create_playlist_response['id']
                f = open('../playlist.txt', 'w')
                f.write(playlist_id)
                print('Se ha creado una playlist:', playlist_id)

    elif os.path.isfile('../code.txt'):
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
            print('No pude eliminar el archivo ../code.txt')
            print('Error:', error)

    else:
        print('No hay credenciales de acceso.')
        print('Acceda a: http://localhost:7777/authorize')

    option = input('¿Volver a intentar? (s/n): ')
    if option == 'n':
        break
