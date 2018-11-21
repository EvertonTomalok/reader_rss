from controles import *
import os
from tqdm import tqdm
from time import sleep


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def crawl_noticias(iteravel, categoria):

    clear()

    news = []

    tm = len(iteravel)

    print(f'\n\n   Crawleando Informações {categoria.upper()}:\n')

    with tqdm(initial=0, total=tm, bar_format='{desc}: {percentage:3.0f}%|{bar}|{n_fmt}/{total_fmt} > Time: {elapsed}') as pbar:

        pbar.update(0)

        for link in iteravel:

            parse = parser_feed(link)

            if parse is not None:
                news.extend(parse)

            news = sorted(news, key=lambda parameter: parameter[3], reverse=True)
            pbar.update(1)

        sleep(0.5)
        clear()

    total = len(news)
    if total > 0:

        contador = 0

        while True:

            tamanho_cat = len(categoria)
            print('-' * (tamanho_cat + 4))
            print(f'  {categoria.upper()}')
            print('-' * (tamanho_cat + 4))

            texto = sumarizador(news[contador][1])
            data_postagem = news[contador][3].strftime('%A - %d/%B/%Y %H:%M:%S')

            # Titulo da noticia
            frase_a_direita = '\033[;1mNotícia atual:\033[m ' + str(contador + 1) + '/' + str(total)
            print(f'\n\n\n \033[;1m Título: {news[contador][0]}  \033[m ', end='\n')
            print(f'->\033[;1m Data de postagem: \033[m{data_postagem} {frase_a_direita:>70}', end='\n\n\n')

            # Texto Sumarizado
            print('='*60, '\n{:^50}'.format('\033[;1mCONTEÚDO\033[m'), end='\n\n')
            print(f' {texto}\n\n')
            print('=' * 60, end='\n\n')

            # link
            print(f' Link: \033[;4m{news[contador][2]}\033[m')

            verificacao = input(
                '\n\n\n   '
                'Aperte qualquer tecla para ir para próxima notícia, :v para voltar ou :q para sair.'
                '\n\n    ')

            clear()

            if verificacao == ':q':
                break

            elif verificacao == ':v':
                if contador > 0:
                    contador -= 1

            else:
                if contador < total - 1:
                    contador += 1

        clear()

    else:
        print('Nenhuma notícia foi crawleada!')
