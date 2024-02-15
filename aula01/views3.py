from utils import load_data, load_template

def index():
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    
    # if request.startswith('POST'):
    #     request = request.split('\r', '')

    #     partes = request.split('\n\n')
    #     corpo = partes[1]
    #     params = {}

    #     for chave_valor in corpo.split('&'):
    #         chave, valor = chave_valor.split('=')
    #         params[chave] = valor
    
    
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('data/notes.json')
    ]
    notes = '\n'.join(notes_li)

    resposne = load_template('index3.html').format(notes=notes)

    return resposne.encode()