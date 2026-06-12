import requests


resultado = requests.get('https://api.nasa.gov/EPIC/api/natural/date/2019-05-30?api_key=SUA_CHAVE')
print(resultado.status_code)
print(resultado.json())