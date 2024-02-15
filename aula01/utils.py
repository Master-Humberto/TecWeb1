import json

def extract_route(request):
    return request.split(' ')[1][1:]

def  read_file(filepath):
    with open(filepath, 'rb') as file:
        return file.read()

def load_data(filename):
    with open(filename) as file:
        return json.load(file)

def load_template(filename):
    with open(filename) as file:
        return file.read()

def build_response(body='',code=200, reason='OK', headers = ''):
    response = f'HTTP/1.1 {code} {reason}'

    if code == 404:
        response = f'HTTP/1.1 404 Not Found\n\nNot Found'
        return response.encode()
    
    if headers : 
        response += '\n' + headers  
    response += '\n\n' + body
    return response.encode()
