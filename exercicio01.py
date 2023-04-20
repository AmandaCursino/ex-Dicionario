lista = {}

def num():
    return str(input('Informe uma chave: '))

while True:
    item = num()
    if item == '':
        break
    valor = int(input('Informe o valor desta chave: '))
    lista[item] = valor

maior = max(lista.items())
print(f'O maior valor da lista: {maior}')