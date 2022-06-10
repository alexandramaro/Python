""" ex114: Crie um código que teste se o site Pudim está acessível pelo computador usado."""

import urllib.request

try:
    site = urllib.request.urlopen('https://github.com/AlexandrAmaro')
except urllib.error.URLError:
    print('O site \033[31mGitHub-AlexandrAmaro\033[m não está acessível no momento.')
else:
    print('Consegui aceder ao site \033[34mGitHub-AlexandrAmaro\033[m com sucesso!')
#    print(site.read)   → para ler o conteúdo do site
