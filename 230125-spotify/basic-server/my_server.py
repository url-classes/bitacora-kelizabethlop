from http.server import BaseHTTPRequestHandler
from urllib import parse
import webbrowser

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = parse.urlparse(self.path)

        if parsed_path.path == '/authorize':
            client_id = '3u8j2XwGGhJjNbwB2tekad'
            auth_headers = {
                'client_id': client_id,
                'response_type': 'code',
                'redirect_uri': 'http://localhost:7777/callback',
                'scope': 'playlist-modify-public'
            }
            url = 'https://accounts.spotify.com/authorize?'
            webbrowser.open(url + parse.urlencode(auth_headers))

        elif parsed_path.path == '/callback':
            query = parsed_path.query
            code = query.split('=')[1]
            f = open('../code.txt', 'w')
            f.write(code)
            f.close()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()