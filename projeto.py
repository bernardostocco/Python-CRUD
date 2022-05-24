def apresentese():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Cauã Ricci Meneguetti                     RA:22007578       |')        
    print('| Diogo do Amaral Nicastro                  RA:22005103       |')        
    print('| Filipe Asaph Mendonça Ferreira            RA:22010332       |')        
    print('| Bernardo Stocco Kruschewsky Whehaibe      RA:22000390       |')        
    print('|                                                             |')
    print('| Versão 3.0 de 22/abril/2022                                 |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')


def umTexto(solicitacao, mensagem, valido):
    digitouDireito = False
    while not digitouDireito:
        txt = input(solicitacao)

        if txt not in valido:
            print(mensagem, '- Favor redigitar...')
        else:
            digitouDireito = True

    return txt


def opcaoEscolhida(mnu):
    print()

    nroDaOpc = 1
    for opc in mnu:
        print(nroDaOpc, ') ', opc, sep='')
        nroDaOpc += 1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', [str(opc) for opc in range(1, len(mnu) + 1)])


'''
procura nom em agd e, se achou, retorna:
uma lista contendo True e a posicao onde achou;
MAS, se não achou, retorna:
uma lista contendo False e a posição onde inserir,
aquilo que foi buscado, mas nao foi encontrado,
mantendo a ordenação da lista.
'''


def ondeEsta(nom, agd):
    inicio = 0
    final = len(agd) - 1

    while inicio <= final:
        meio = (inicio + final) // 2

        if nom == agd[meio][0]:
            return [True, meio]
        elif nom < agd[meio][0]:
            final = meio - 1
        else:  # nom>agd[meio][0]
            inicio = meio + 1

    return [False, inicio]


def incluir(agd):
    digitouDireito = False
    while not digitouDireito:
        nome = input('\nNome.......: ')

        resposta = ondeEsta(nome, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if achou:
            print('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito = True

    aniversario = input('Aniversário: ')
    endereco = input('Endereço...: ')
    telefone = input('Telefone...: ')
    celular = input('Celular....: ')
    email = input('e-mail.....: ')

    contato = [nome, aniversario, endereco, telefone, celular, email]

    agd.insert(posicao, contato)
    print('Cadastro realizado com sucesso!')


def procurar(agd):
    digitouDireito = False
    while not digitouDireito:
        proc = input(
            'digite o nome da pessoa procurada, ou escreva "menu" para voltar. ')
        if (proc == 'menu'):
            return
        resposta = ondeEsta(proc, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if not achou:
            print('Pessoa não encontrada')

        else:
            digitouDireito = True

    print('nome........:', agd[posicao][0])
    print('aniversario.:', agd[posicao][1])
    print('endereco....:', agd[posicao][2])
    print('telefone....:', agd[posicao][3])
    print('celular.....:', agd[posicao][4])
    print('email.......:', agd[posicao][5])


def atualizar(agd):
    digitouDireito = False
    while not digitouDireito:
        proc = input(
            'digite o nome da pessoa que deseja atualizar, ou digite "menu" para voltar. ')
        if (proc == 'menu'):
            return
        resposta = ondeEsta(proc, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if not achou:
            print('Pessoa não encontrada, favor redigitar...')
        else:
            digitouDireito = True

    print('1)Aniversario')
    print('2)Endereco')
    print('3)Telefone')
    print('4)Celular')
    print('5)Email')
    upd = input('Escolha uma opção para atualizar.')
    if (upd == "1"):
        print('aniversario: ', agd[posicao][1])
        aniversario = input('Aniversário: ')
        agd[posicao][1] = aniversario
    elif (upd == "2"):
        print('endereco: ', agd[posicao][2])
        endereco = input('Endereço: ')
        agd[posicao][2] = endereco
    elif (upd == "3"):
        print('telefone: ', agd[posicao][3])
        telefone = input('Telefone: ')
        agd[posicao][3] = telefone
    elif (upd == "4"):
        print('celular: ', agd[posicao][4])
        celular = input('Celular: ')
        agd[posicao][4] = celular
    else:
        print('email: ', agd[posicao][5])
        email = input('Email: ')
        agd[posicao][5] = email

    print('O contato foi atualizado com sucesso!')


def listar(agd):
    if agd == []:
        print('A agenda não possui pessoas cadastradas!')
    else:
        for contato in agd:
            print('\nNome.......:', contato[0])
            print('Aniversário:', contato[1])
            print('Endereço...:', contato[2])
            print('Telefone...:', contato[3])
            print('Celular....:', contato[4])
            print('e-mail.....:', contato[5])
        '''
        posicao=0
        while posicao<len(agd):
            print('\nNome.......:',agd[posicao][0])
            print('Aniversário:',agd[posicao][1])
            print('Endereço...:',agd[posicao][2])
            print('Telefone...:',agd[posicao][3])
            print('Celular....:',agd[posicao][4])
            print('e-mail.....:',agd[posicao][5])
            posicao+=1
        '''


def excluir(agd):
    print()

    digitouDireito = False
    while not digitouDireito:
        nome = input('Nome.......: ')

        resposta = ondeEsta(nome, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if not achou:
            print('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito = True

    print('Aniversario:', agd[posicao][1])
    print('Endereco...:', agd[posicao][2])
    print('Telefone...:', agd[posicao][3])
    print('Celular....:', agd[posicao][4])
    print('e-mail.....:', agd[posicao][5])

    resposta = umTexto('Deseja realmente excluir? ',
                       'Você deve digitar S ou N', ['s', 'S', 'n', 'N'])

    if resposta in ['s', 'S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')


# daqui para cima, definimos subprogramas
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(inserir), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresentese()

agenda = []

menu = ['Incluir Contato',
        'Procurar Contato',
        'Atualizar Contato',
        'Listar Contatos',
        'Excluir Contato',
        'Sair do Programa']

opcao = None
while opcao != 6:
    opcao = int(opcaoEscolhida(menu))

    if opcao == 1:
        incluir(agenda)
    elif opcao == 2:
        procurar(agenda)
    elif opcao == 3:
        atualizar(agenda)
    elif opcao == 4:
        listar(agenda)
    elif opcao == 5:
        excluir(agenda)

print('OBRIGADO POR USAR ESTE PROGRAMA!')
