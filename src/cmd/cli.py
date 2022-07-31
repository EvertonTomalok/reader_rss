from src.controles.gerador_menu import menu, sair, clear


def cli():
    try:
        menu()

    except KeyboardInterrupt:
        sair()
        clear()

    except Exception as err:
        print(type(err), err)