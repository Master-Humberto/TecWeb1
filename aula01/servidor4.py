import socket
from pathlib import Path
from utils import extract_route, read_file, build_response
# from utils import load_data, load_template
from views4 import index

CUR_DIR = Path(__file__).parent
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

# NOTE_TEMPLATE = '''  <li>
#     <h3>{title}</h3>
#     <p>{details}</p>
#   </li>
# '''

# RESPONSE_TEMPLATE = '''HTTP/1.1 200 OK

# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="UTF-8">
# <title>Get-it</title>
# </head>
# <body>

# <img src="img/logo-getit.png">
# <p>Como o Post-it, mas com outro verbo</p>

# <ul>
# {notes}
# </ul>

# </body>
# </html>
# '''

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

print(f'Servidor escutando em (ctrl+click): http://{SERVER_HOST}:{SERVER_PORT}')

while True:
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()
    print('*'*100)
    print(request)

    route = extract_route(request)
    filepath = CUR_DIR / route
    if filepath.is_file():
        response = build_response() + read_file(filepath)
        # print("Amogus")
    elif route == '':
        if request.split()[0] == 'POST' and len(request.split("\n\n")) == 1:
            request += client_connection.recv(1024).decode()
        response = index(request)
        # print("Bongus")
    else:
        response = build_response(body = 'Not Found', code=404, reason='Not Found')
        # print("Bingus")
    client_connection.sendall(response)

    client_connection.close()

server_socket.close()