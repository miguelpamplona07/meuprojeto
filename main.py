
import numpy as np
from sklearn.linear_model import LinearRegression
# 1. Dados de entrada (X: Temperatura, y: Vendas)
X = np.array([[22], [25], [23], [28], [31], [26], [21], [29], [24], [32]])
y = np.array([15, 18, 22, 32, 35, 24, 12, 40, 20, 38 ])

# 2. Criar e treinar o modelo
modelo = LinearRegression()
modelo.fit(X, y)

# 3. Definir a temperatura para o 6º dia e prever
temperatura_sexta_venda = 34
previsao = modelo.predict([[temperatura_sexta_venda]])

print(f"Modelo Treinado!")
print(f"Para uma temperatura de {temperatura_sexta_venda}°C, a 6ª venda será de: {previsao[0]:.0f} sorvetes.")
import matplotlib.pyplot as plt

# Criar o gráfico
plt.figure(figsize=(8, 5))

# Desenhar os pontos reais (os 5 dias iniciais)
plt.scatter(X, y, color='blue', label='Vendas Reais')

# Desenhar a linha que o modelo criou (Reta de Regressão)
plt.plot(X, modelo.predict(X), color='red', label='Linha de Tendência')

# Destacar a previsão da 6ª venda (Ponto Verde)
plt.scatter([temperatura_sexta_venda], previsao, color='green', marker='*', s=200, label='Sexta Venda (Previsão)')

# Detalhes visuais
plt.title('Análise de Vendas de Sorvete')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Sorvetes Vendidos')
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()
