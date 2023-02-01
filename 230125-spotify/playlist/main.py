import os
import base64
import requests

client_id = '2d7800dcec2241389843e017b8ab5e4d'
client_secret = 'e8f0ce222da24f62881d26db6c2b0291'

if os.path.isfile('../code.txt'):
    f = open('../code.txt', 'r')
    code = f.read()
    f.close()
    print('Codigo:', code)
    credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode('utf-8')

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
print(r)