import requests


cep = 39280000

resultado = requests.get('https://cep.awesomeapi.com.br/json/{}'.format(cep))
print(resultado.json())
