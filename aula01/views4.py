from utils import load_data, load_template, build_response
import json
def index(request):
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    if request.startswith('POST'):
        request = request.replace('\r', '')
        
        partes = request.split('\n\n')  

        corpo = partes[1]
        print(corpo)
        params = load_data('data/notes.json')
        # print(corpo)
        for chave_valor in corpo.split('&'):
            if chave_valor.startswith('titulo'):
                titulo = chave_valor.split('=')[1]
                params.append({'titulo': titulo})
            if chave_valor.startswith('detalhes'):
                detalhes = chave_valor.split('=')[1]
                params[-1]['detalhes'] = detalhes
        

        
        #     titulo = chave_valor.split('=')[1]
        #     detalhes = chave_valor.split('=')[3]
        #     params.append({'titulo': titulo, 'detalhes': detalhes})

        
        with open('data/notes.json', 'w') as file:
            json.dump(params, file, indent=4, ensure_ascii=False)
         
    
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('data/notes.json')
    ]
    notes = '\n'.join(notes_li)

    html = load_template('index4.html').format(notes=notes)
    response = build_response(html)


    return response