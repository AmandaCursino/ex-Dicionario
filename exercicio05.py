dic = {}

def criar_dicionario():
    while True:
        chave = input('Digite uma chave: ')
        if chave == '':
            break
        valor = input('Digite um número para a chave: ')
        dic[chave] = valor
        
    chaves = []
    for i in dic.keys():
        chaves.append(i)
    print('As chaves são: ', chaves)
        
criar_dicionario()