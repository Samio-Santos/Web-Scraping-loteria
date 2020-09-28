import requests
from bs4 import BeautifulSoup

# Faz um requisição no site da loteria
requisicao = requests.get('http://loterias.caixa.gov.br/wps/portal/loterias')


# Coleta todas as informações para exibir no terminal
site = BeautifulSoup(requisicao.text, "html.parser")

titulo = site.find(class_='description').text.split()

premio = site.find(class_='action clearfix').text.split()

jogo = site.find(class_='resultado-loteria').text.strip()

resultado = f'{jogo[:2]}-{jogo[2:4]}-{jogo[4:6]}-{jogo[6:8]}-{jogo[8:10]}-{jogo[10:12]}'


# Faz a formatação do cabeçalho da loteria
print('MEGA-SENA\n')
for i in titulo:
    print(i, end=' ')

# Mostra o resultado.
print(f'\nResultado: {resultado}')

print('')

# Mostra o premio para o novo concurso da loteria.
print('Acumulou!')
for i in premio:
    print(f'{i}', end=' ')
print('!')


