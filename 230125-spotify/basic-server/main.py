from my_server import MyServer
from http.server import HTTPServer

web_server = HTTPServer(
    ('localhost', 7777),
    MyServer
)

print('Iniciando servidor...')
try:
    web_server.serve_forever()
except KeyboardInterrupt:
    print('Apagando el servidor...')

print('El servidor se ha detenido.')
print('Adiós.')
print('No vuelva.')
