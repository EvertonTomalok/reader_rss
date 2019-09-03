from controles.geradornoticias import clear, crawl_noticias
from doc.links import *


def sair():
    from time import sleep

    print("\n\n\n")
    print("-" * 15)
    print("*{:^13}*".format("SAINDO"))
    print("-" * 15)
    sleep(1)


def menu():
    while True:
        print("-" * 45)
        print("|{:^42} |".format("MENU"))
        print("-" * 45)
        print("| {:^42}|".format("Selecione uma opção (Digite o número)"))
        print("-" * 45)
        print("| {:42}|".format("1 - ÚLTIMAS NOTÍCIAS,"))
        print("| {:42}|".format("2 - ECONÔMIA,"))
        print("| {:42}|".format("3 - POLÍTICA,"))
        print("| {:42}|".format("4 - ESPORTES,"))
        print("| {:42}|".format("5 - CINEMA,"))
        print("| {:42}|".format("6 - SAÚDE,"))
        print("| {:42}|".format("7 - BRASIL E MUNDO,"))
        print("| {:42}|".format("8 - AUTOMÓVEIS,"))
        print("| {:42}|".format("9 - TRÂNSITO,"))
        print("| {:42}|".format("10 - SAÚDE,"))
        print("| {:42}|".format("11 - CULTURA, TECNOLOGIA E CIÊNCIA,"))
        print("| {:42}|".format("12 - EDUCACAO,"))
        print("| {:42}|".format("13 - TODAS NOTÍCIAS."))
        print("-" * 45)
        print("| {:42}|".format("99 - LIMPAR TELA"))
        print("-" * 45)
        print("| {:42}|".format("0 - SAIR"))
        print("-" * 45)
        escolha = input("\n\n     Digite o número da notícia a ser crawleada: ")

        try:
            escolha = int(escolha)
        except ValueError:
            print("Digite apenas o NÚMERO da opção desejada.")

        if escolha == 1:
            crawl_noticias(ultimas_noticias, "últimas noticias")
        elif escolha == 2:
            crawl_noticias(economia, "econômia")
        elif escolha == 3:
            crawl_noticias(politica, "política")
        elif escolha == 4:
            crawl_noticias(esportes, "esportes")
        elif escolha == 5:
            crawl_noticias(cinema, "cinema")
        elif escolha == 6:
            crawl_noticias(saude, "saúde")
        elif escolha == 7:
            crawl_noticias(brasil_e_mundo, "Brasil E mundo")
        elif escolha == 8:
            crawl_noticias(automoveis, "automóveis")
        elif escolha == 9:
            crawl_noticias(transito, "trânsito")
        elif escolha == 10:
            crawl_noticias(saude, "saúde")
        elif escolha == 11:
            crawl_noticias(cultura_tecnologia_ciencia, "Cultura, tecnologia e ciência")
        elif escolha == 12:
            crawl_noticias(educacao, "Educação")
        elif escolha == 13:

            todos_links = {
                ultimas_noticias,
                economia,
                politica,
                esportes,
                cinema,
                saude,
                brasil_e_mundo,
                automoveis,
                transito,
                saude,
                cultura_tecnologia_ciencia,
                educacao,
            }

            todas = [link for elemento in todos_links for link in elemento]

            crawl_noticias(todas, "TODOS LINKS")

        elif escolha == 99:
            clear()
        elif escolha == 0:
            sair()
            clear()
            break
        else:
            print("\n\nEscolha inválida. TENTE NOVAMENTE.\n\n")
