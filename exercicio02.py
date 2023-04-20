lista = {}

def funcao():
    while True:
        nomezin = input('Digite um nome: ')
        if nomezin == '':
            break
        ida = int(input(f'Digite a idade: '))
        lista[nomezin] = {'idade':ida}

    for i, maior in lista.items():
        if maior['idade'] >= 18:
            maior_de_18 = maior['idade']
            print('Nome:', i)
            print('Idade:', maior_de_18, 'anos')

funcao()