pessoas = [
    {
        'Nome': 'Miguel',
        'CPF': '61286948029',
        'Email': 'augustom956a@gmail.com'

    },
    {
        'Nome': 'Luiz',
        'CPF': '07526724010',
        'Email': 'luizfernandes@outlook.com'
    },
    {
        'Nome': 'Pedro',
        'CPF': '72503424015',
        'Email': 'pedroavelino@aluno.unip.br'
    },
]

nome:str
cpf:str
email:str
menu:int = 0

def Verifica(tipo): # 1: Nome, 2: CPF, 3: Email
    variavel = ''

    match tipo:
        case 1:
            variavel = str(input('Digite o Nome:'))

            while not variavel:
                variavel = str(input('Por Favor digite um nome: '))
            return variavel
        
        case 2:
            variavel = str(input('Digite o CPF: '))
            for pessoa in pessoas:
                while variavel == pessoa['CPF'] or len(variavel) != 11:
                    variavel = str(input('Erro! CPF inválido ou Cliente já existente. Digite um CPF: '))
            return variavel
        
        case 3:
            variavel = str(input('Digite o Email: '))
            while '@' not in variavel:
                variavel = str(input('Email não localizado! Digite um Email válido: '))
            return variavel
            

def Adicionar():
    print('\n','='*10,'Adicionar Cliente','='*10)

    nome = Verifica(1)
    cpf = Verifica(2)
    email = Verifica(3)

    pessoas.append({'Nome': nome,'CPF':cpf,'Email':email})
    print('Pessoa Adicionada!')
    
    while nome:
        nome = str(input('Digite "1" para voltar ao menu ou "2" para adicionar mais clientes: '))
        if nome == '1':
            return None
        elif nome == '2':
            return Adicionar()
        
    
def Remover():
    print('='*10,'Remover Cliente','='*10)
    cpf = str(input('Digite o CPF da pessoa que deseja remover ou digite "1" para voltar ao Menu: '))
    
    if cpf == '1':
        return None
    
    for i in range(len(pessoas)):
        if pessoas[i]['CPF'] == cpf:
            del pessoas[i]
            print(f'O cliente foi removido!')
            while cpf:
                cpf = str(input('Digite "1" para voltar ao menu ou "2" para remover mais clientes: '))
                if cpf == '1':
                    return None
                elif cpf == '2':
                    return Remover()
        else:
            if pessoas[-1]['CPF'] != cpf:
                print('Nenhum CPF foi encontrado!')
                return Remover()

def Editar():
    print('\n','='*10,'Editar Cliente','='*10)
    cpf = str(input('Digite o CPF da pessoa que deseja editar ou digite "1" para voltar ao Menu: '))
    
    if cpf == '1':
        return None
    
    for i in range(len(pessoas)):
        if pessoas[i]['CPF'] == cpf:
            pessoas[i]['Nome'] = Verifica(1)
            pessoas[i]['CPF'] = Verifica(2)
            pessoas[i]['Email'] = Verifica(3)
            print('Cliente Alterado!')
            while cpf:
                cpf = str(input('Digite "1" para voltar ao menu ou "2" para alterar mais clientes: '))
                if cpf == '1':
                    return None
                elif cpf == '2':
                    return Editar()
        else:
            if pessoas[-1]['CPF'] != cpf:
                print('Nenhum CPF foi encontrado!')
                return Editar()

def VerClientes():
    nome = '0'
    print('='*10,'Clientes Cadastrados','='*10)

    if len(pessoas) == 0:
        print('Não há Clientes cadastrados!')

    for pessoa in pessoas:
        print(f'Nome: {pessoa["Nome"]}, Email: {str(pessoa["Email"])}, CPF: {pessoa["CPF"]}')
    
    while nome:
        nome = str(input('Digite "1" para voltar ao menu: \n'))
        if nome == '1':
            return None
        
print('======================================================')
print('                    Programa CRUD - UNIP APS          ')
print('      Aplicação para gerenciamento de Clientes        ')
print('======================================================')
    
while menu >= 0:
    menu = int(input('\n ======= Menu ======= \n 1. Adicionar Cliente \n 2. Remover Cliente \n 3. Editar Cliente \n 4. Ver Clientes \n 5. "Sair" \n\n Digite o ID do menu para acessar: '))

    if menu == 1:
        Adicionar()

    if menu == 2:
        Remover()

    if menu == 3:
         Editar()
                           
    if menu == 4:
        VerClientes()

    if menu == 5:
        break