fim = 0
def clear():
    import os
    import platform
    desk = platform.system()
    if desk == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
while fim != '0':
    clear()
    print('==================================')
    print('========  MENU PRINCIPAL  ========')
    print('==================================')
    print('   1 - CADASTRAR CLIENTE')
    print('   2 - PESQUISAR CLIENTE')
    print('   3 - MODIFICAR CLIENTE')
    print('   4 - DELETAR CLIENTE')
    print('   0 - SAIR')
    option = input('Escolha sua opção ? ')
    if option == '1':
        clear()
        print ('opção 1')
        input(' Pressione enter para continuar...')
    elif option == '2':
        clear()
        print ('opção 2')
        input(' Pressione enter para continuar...')
    elif option == '3':
        clear()
        print('opçao 3')
        input(' Pressione enter para continuar...')
    elif option == '4':
        clear()
        print ('opção 4')
        input(' Pressione enter para continuar...')
    elif option == '0':
        clear()
        print ('Programa encerrado!')
        break
