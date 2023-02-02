import requests
import re
import json
from bs4 import BeautifulSoup
from collections import Counter


def contagem_palavra(site_url, palavra_especifica=None, quantidade_de_paginas=10):
    """
    Esta função raspa as palavras de um site e seus links, exibindo as palavras e sua frequência. Ela permite procurar
    por uma palavra específica e limitar a quantidade de páginas a serem pesquisadas. O resultado é salvo como um
    arquivo JSON que inclui os links dos sites e a contagem das palavras encontradas.
    :param site_url: URL do site que a função fara a busca das palavras ou palavra especifica.
    :param palavra_especifica: Palavra especifica que o usuario deseja procurar. (opcional)
    :param quantidade_de_paginas: Quantidade de paginas do site que serao analisadas. (opcional)
    :return: None
    """
    site = requests.get(site_url)  # Site que sera analisado
    html = BeautifulSoup(site.text, 'html.parser')  # Pegando HTML do site
    links = []  # Links de outras paginas do site
    site_e_dados = {}  # Dicionario onde ira conter cada site e suas palavras
    cont = 0  # Contador para saber se a função ja analisou a quantidade de sites que foi especificado

    # Pegando o link das paginas do site
    for tag in html:
        for link in re.findall(r'href="(https://[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*[\w\d\s]*\.*-*/*=*:*\(*\)*)', str(tag), re.I):
            if link not in links:
                links.append(link)

    # Se o usuario tentou analisar mais paginas do que o site tem.
    if quantidade_de_paginas > len(links):
        print('\n\n\t\tO site não possui a quantidade de paginas que foi pedida para analise.\n'
              f'Voce vera somente a analise de {len(links)} paginas que este site possui.\n\n')
        quantidade_de_paginas = len(links)  # Colocando para analisar a quantidade de paginas que o site tem

    while cont != quantidade_de_paginas:  # Enquanto a função nao analisar a quantidade de paginas especificada
        if cont == 0:  # Se for o primeiro site a ser analisado
            site = requests.get(site_url)
        else:
            site = requests.get(links[cont - 1])

        html = BeautifulSoup(site.text, 'html.parser')
        palavra = ''  # Variavel que ira conter cada palavra encontrada

        # Pegando cada palavra, considerando que a palavra começa quando sua primeira letra é maiuscula
        for letra in html.text:
            if letra.isalpha() or letra == ' ':
                if not letra == ' ':
                    if letra.isupper():
                        palavra += '\n'
                        palavra += letra
                    else:
                        palavra += letra
                else:
                    palavra += '\n'

        # Adicionando cada palavra em ordem e separando elas por linhas que foram puladas
        palavras_ordenadas = sorted(Counter(palavra.splitlines()).items(), key=lambda x: x[1], reverse=True)

        for index, palavra_contage in enumerate(palavras_ordenadas):  # Removendo espaço em branco
            if palavra_contage[0] == '':
                palavras_ordenadas.remove(palavra_contage)

        # Adicionando os dados coletados no dicionario
        site_e_dados[site.url] = palavras_ordenadas
        cont += 1

    if palavra_especifica is None:  # Se o usuario nao informou uma palavra especifica
        with open('analise.json', 'w+') as file:  # Criando arquivo JSON com todas as palavras encontradas
            dados_json = json.dumps(site_e_dados)
            file.write(dados_json)

    else:
        palavras_achadas = []  # Lista com o site e quantidade que a palavra foi encontrada
        for site, palavras in site_e_dados.items():
            for palavra in palavras:
                if palavra_especifica == palavra[0] or palavra_especifica == palavra[0].title() or \
                        palavra_especifica == palavra[0].upper() or \
                        palavra_especifica == palavra[0].lower():  # Se encontrou a palavra especifica
                    palavras_achadas.append({f'{site}': [palavra[0], palavra[1]]})

        if len(palavras_achadas) > 0:  # Se encontrou a palavra especifica
            with open('analise.json', 'w+') as file:
                dados_json = json.dumps(palavras_achadas)
                file.write(dados_json)

        else:
            print('\n\n\t\tA palavra que foi especificada nao foi encontrada em nenhuma das paginas\n\n')


if __name__ == '__main__':
    contagem_palavra('https://g1.globo.com/', 'bolsonaro', 100)
