import re
import unicodedata
from collections import defaultdict
from datetime import datetime, timedelta
from heapq import nlargest

import nltk
from bs4 import BeautifulSoup

import feedparser
from src.doc.stop_words import words

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")


def meu_tokenizer(string):
    """
    Just a tokenizer created using module 're'
    """
    pattern = r"""\w+\S+\w+|\w+|\d+\.?,?\d+%|[0-9]{1,2}h?:?[0-9]{2}|[#$&\*'"]+"""

    return re.findall(pattern, string)


def sumarizador(texto):
    # iniciamos um novo defaultdict, aonde cada chave nova gerada, irá receber o valor 0, caso a chave não exista
    ranking = defaultdict(int)

    # Preprocessing
    texto = (
        texto.replace("R$", " ")
        .replace("$", " ")
        .replace("\n", " ")
        .replace("\t", " ")
        .replace(".", ". ")
        .strip()
    )
    texto = unicodedata.normalize("NFKD", texto)
    texto = " ".join(texto.split())

    # Tokenization
    tokens = meu_tokenizer(texto)
    tokens = [t for t in tokens if t not in words]
    sents = nltk.sent_tokenize(texto)

    # Caso número de sentenças menor ou igual à 2, não será sumarizado e retornará o texto de entrada
    if len(sents) <= 2:
        return texto

    # Calculando a Frequência dos tokens
    freq = nltk.probability.FreqDist(tokens)

    # A primeira sentença sempre irá ser retornada. Para isso jogamos um valor de ranking elevado para garantir
    # sempre a primeira posição na lista de ranking
    ranking[0] = 10000000000

    for i, sent in enumerate(sents):
        for w in meu_tokenizer(sent.lower()):
            if w in freq:
                ranking[i] += freq[w]

    # definindo o número de sentenças que devem gerar o sumário
    if 2 < len(sents) < 5:
        num = 2
    else:
        num = 3

    # Recuperamos os indices que obtiverem as maiores pontuações.
    # Obedecemos o num acima, como delimitador de sentenças a serem recuperadas.
    sents_idx = nlargest(num, ranking, key=ranking.get)
    texto_sumarizado = "\n\n               ...\n\n ".join(
        [sents[j] for j in sorted(sents_idx)]
    )

    return texto_sumarizado


def parser_feed(url):
    try:
        textos = list()

        my_feed = feedparser.parse(url)

        for post in my_feed.entries:

            try:
                not_con = post.summary_detail.value
            except Exception:
                not_con = post.summary

            soup_conteudo = BeautifulSoup(not_con, "lxml")
            soup_title = BeautifulSoup(post.title, "lxml")
            link = post.link

            try:
                data = post["published_parsed"]

                y = data.tm_year
                m = data.tm_mon
                d = data.tm_mday
                H = data.tm_hour
                M = data.tm_min
                S = data.tm_sec

                # Ajustar para o fuso de brasília, diminuímos 2 horas
                data = datetime(y, m, d, H, M, S) - timedelta(hours=2)
            except Exception:
                data = datetime.now() - timedelta(hours=12)

            if "vídeos" not in soup_title.text.lower():

                textos.append((soup_title.text, soup_conteudo.text, link, data))

        return textos

    except Exception as err:
        print(err)

        return None
