# readerrss

Um sumarizador de notícias, de diversas fontes, agrupadas por categorias.

# Instalando no seu SO

Abra um `terminal` ou shell e rode o comando:
    - python3 setup.py install --user

Agora rode:
    - reader-rss

O Prompt de escolhas ira aparecer


# Instalação alternativa
## Instalando os Requisitos

Abral um `terminal` ou shell, e instale os requisitos necessários.

    - Recomendado (via ambiente virtual)
        
        pip install pipenv
        pipenv install

    - Outras formas:
        pip install -r requirements.txt
        
        or
        
        pip install --user nltk tqdm feedparser beautifulsoup4

## Após isso, rode o programa:
    
Obs.: Se você instalou via pipenv, rode primeiro `pipenv shell`

    python reader.py



Aproveite seu feed de notícias! :)