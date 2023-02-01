from http.server import BaseHTTPRequestHandler
from urllib import parse


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        if parsed_path.path == '/callback':
            query = parsed_path.query
            code = query.split('=')[1]
            f = open('../code.txt', 'w')
            f.write(code)
            f.close()
        else:
            print("No hacer nada")
        self.send_response(200, 'Todo bien')