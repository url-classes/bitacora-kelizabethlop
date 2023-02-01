import webbrowser
from urllib.parse import urlencode
from my_server import MyServer
from http.server import HTTPServer


client_id = '2d7800dcec2241389843e017b8ab5e4d'
client_secret = 'e8f0ce222da24f62881d26db6c2b0291'
auth_headers = {
    'client_id': client_id,
    'response_type': 'code',
    'redirect_uri': 'http://localhost:7777/callback',
    'scope': 'playlist-modify-public'
}
url = 'https://accounts.spotify.com/authorize?'

webbrowser.open(url + urlencode(auth_headers))

web_server = HTTPServer(
    ('localhost', 7777),
    MyServer
)
print('Iniciando Servidor...')
web_server.serve_forever()