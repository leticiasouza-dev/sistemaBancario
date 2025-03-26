print(f'-----Sistema Bancário PyBang-----')
print(f'Selecione a opção desejada:')

opcao_escolhida = int(input('1 - Criar Conta\n2 - Acessar Conta \n3 - Sair \n'));
nome = ''
ano_nascimento = 0
agencia = 1550
saldo = 0

def verifica_idade(ano_nascimento: int):
    ano_atual = 2025;
    idade_cliente = ano_atual - ano_nascimento

    if idade_cliente >= 18:
        return True;
    else: 
        return False;

if opcao_escolhida == 1:
    print(f"Vamos inicar a criação da sua conta, e para isso preciso de algumas informações:")
    nome = input('Digite seu nome:')

    ano_nascimento = int(input('Digite o seu ano de nascimento'));

    usuario_e_maior_de_idade = verifica_idade(ano_nascimento)
    
    if usuario_e_maior_de_idade == True:
        print('Sua conta esta criada' + nome + ', sua agenda é ', agencia, 'e o seu saldo é de: ' , saldo)
    else:
        print('infelizmente você é menor de idade e não poderá continuar com a criação da conta');
print(nome);








    