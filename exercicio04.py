dic = {}

def criar_dicionario():
    while True:
        chave = input('Digite uma chave: ')
        if chave == '':
            break
        valor = int(input('Digite um número para a chave: '))
        dic[chave] = valor
        
        
    for item in dic.keys():
        print('As chaves são:', item )
    for item in dic.keys():
        print('Os valores são:', dic[item])
    
criar_dicionario()