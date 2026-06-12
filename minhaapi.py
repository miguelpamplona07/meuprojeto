from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    
    data = request.args.get('data_escolhida', '1998-05-27')
    
    url = f'https://api.nasa.gov/planetary/apod?api_key=udjhEqIiDKfQEcojXN3GZqTLhPQypZa5naiOqKzH&date={data}'
    
    resultado = requests.get(url)
    dados_nasa = resultado.json()
    
    return render_template('index.html', info=dados_nasa, data_atual=data)

if __name__ == '__main__':
    app.run(debug=True)