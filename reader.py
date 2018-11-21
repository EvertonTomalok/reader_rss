from controles.gerador_menu import menu, sair, clear


if __name__ == '__main__':
    try:
        menu()

    except KeyboardInterrupt:
        sair()
        clear()

    except Exception as err:
        print(type(err), err)
