#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# 
# feito por: Marcos Rodrigues de Carvalho
# Cidade: Itatiba
# Estado: SP

from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

url = 'http://concurso.esa.ensino.eb.br/site/ProvasAnteriores.aspx'
resp = urlopen(url).read()

info = str(url).split('/')

print('''
=======================
= Informações obtidas =
=======================

Site: - - - - - - - - - - - - - - - {}
Diretórios no site: - - - - - - - - {}
Pagina que o scrapping ira atuar: - {}

========================
= Arquivos encontrados =
========================
'''.format(info[2], info[3], info[4]))

soup = BeautifulSoup(resp, 'html.parser')
link_d = []
for link in soup.find_all('a'):
    if link.get('href')[-3:] in 'pdf':
        link_d.append(link.get('href'))
        print(''.join(link.get('href').split('/')[-1]))
        
op = str(input('''
= Você deseja salvar os arquivos em seu computador s/n?
'''))

if op.lower() == 's':
    for i in link_d:
        nome = i.split('/')[-1]
        with open(nome, 'wb') as f:
            f.write(urlopen(i).read())
            print(nome + ' ---> ' + os.getcwd() + '/' + nome)
else:
    print('Ok, até logo!')
    exit()
            
