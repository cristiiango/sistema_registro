import datetime
import random
import os.path


def menu():
    escolha = input('\033[1;34m1 - Adicionar registro\n2 - Ler registro\n3 - Sair\n\033[m'
                    '\033[1;93mEscolha uma opção: \033[m')
    if escolha == '1':
        adicionar()
    elif escolha == '2':
        reg()
    elif escolha == '3':
        fechar_reg = open('registro.txt', 'a')
        fechar_reg.close()
        exit()
    elif escolha != '1' or '2' or '3':
        print('Opção invalida')
        menu()


def adicionar():
    f_add_qtde = 0
    add_reg = open('registro.txt', 'a')
    add_id = input('Qual o ID do animal? ')
    add_qtde = input('Qual a quantia de leite produzido? ')

    if len(add_qtde) == 1:
        f_add_qtde = '0'+add_qtde+'.0'
    elif len(add_qtde) == 2:
        f_add_qtde = add_qtde+'.0'
    elif len(add_qtde) == 4:
        f_add_qtde = add_qtde
    else:
        print('Valor invalido')
        menu()

    if int(add_id) not in range(1, 999):
        print(f'\033[31mID invalido\033[00m')
        menu()
    elif float(add_qtde) > 30:
        print(f'\033[1;31mQuantidade invalida\033[m')
        menu()
    else:
        f_add_id = '%03d' % int(add_id)
        add_reg.writelines(f'{f_add_id}{dia_atual}{mes_atual}{ano_atual}{f_add_qtde}\n')
        print(f'\033[1;91mRegistro adicionado com sucesso! ')
        add_reg.close()
        menu()


def gerador():
    def gerar():
        anim_id = random.randint(0, 999)
        dia = random.randint(1, 30)
        mes = random.randint(1, 12)
        ano = random.randint(2016, 2020)
        qtde = random.randint(2, 18)
        qtdedec = random.randint(0, 9)

        convan = str('%03d' % anim_id)
        convdia = str('%02d' % dia)
        convmes = str('%02d' % mes)
        convano = str(ano)
        convqtde = str('%02d' % qtde)
        convqtdedec = str(qtdedec)

        a = f'{convan}{convdia}{convmes}{convano}{convqtde}.{convqtdedec}'
        return a

    abrir = open('registro.txt', 'a')

    lista = []
    k = 10000
    for i in range(0, k):
        gerar()
        lista.append(gerar())
        abrir.writelines(f'{gerar()}\n')
    menu()


def reg():
    def busca_bin(val_input, reg_lista):
        reg_lista.sort()
        n = len(reg_lista)
        inicio = 0
        fim = n - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2
            if val_input < int(reg_lista[meio][0:3]):
                fim = meio - 1
            elif val_input > int(reg_lista[meio][0:3]):
                inicio = meio + 1
            else:
                res_lista.append(reg_lista[meio])
                del reg_lista[meio]
                busca_bin(val_input, reg_lista)
        return -1

    def ler_registro():
        for regs in ler.readlines():
            lista.append(regs.replace('\n', ''))
        busca_bin(valor, lista)

    def print_res():
        print('ID  |    DATA    | QTDE')
        for res in res_lista:
            temp_lista.append(res)

        for qtde in res_lista:
            lista_qtde.append(float(f'{qtde[11:15]}'))
        soma_total = 0
        for soma in lista_qtde:
            soma_total += soma
        for lines in temp_lista:
            print(f'\033[1;33m{lines[0:3]}\033[m | \033[35m{lines[3:5]}/{lines[5:7]}/{lines[7:11]}\033[0m |'
                  f'\033[34m {lines[11:15]} l\033[m')

        print(f'\033[34m            Total:', '%.1f' % soma_total, 'l\033[m')

    lista = []
    res_lista = []
    temp_lista = []
    lista_qtde = []

    ler = open('registro.txt', 'r')
    valor = int(input('Qual o ID do animal? '))
    ler_registro()
    print_res()

    if busca_bin(valor, lista) == -1:
        print(f'\nFim da busca\n{len(temp_lista)} Registros referentes ao ID: {valor:03}\n')
        busca_bin(valor, lista)
        ler.close()
        menu()


dia_atual = '%02d' % datetime.datetime.now().day
mes_atual = '%02d' % datetime.datetime.now().month
ano_atual = datetime.datetime.now().year
reg_verif = os.path.isfile('registro.txt')

if reg_verif:
    menu()
else:
    gerador()
