from statistics import mean
from scipy.stats import norm

# o arquivo a ser lido deve conter um valor por linha e estar no mesmo local do arquivo do código
# renomeie a variável nome_arquivo para o que será utilizado

nome_arquivo = 'valores.txt'
data = []

with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        data.append(float(linha.strip()))

# constantes
media = mean(data)
tamanho = len(data) 
dmax = 1- (1/2*tamanho) 

outliers = []

somatorio_variancia = 0
for num in data: 
    variancia = (num - media)**2 / (tamanho - 1)
    somatorio_variancia += variancia

desvio_padrao = variancia ** 0.5 #constante
    
z = (dmax - media) / desvio_padrao

for num in data:
    znum = (num - media) / desvio_padrao
    probabilidade_cauda_esquerda = norm.cdf(z)
    probabilidade_cauda_direita = 1 - probabilidade_cauda_esquerda

    if probabilidade_cauda_direita < dmax:
        print(f"{num} está fora da curva padrão.")
        outliers.append(num)

num_outliers = len(outliers)

if all(z >= znum for z in data):
    print("Todos os valores estão dentro da curva padrão.")
else:
    print(f"O(s) número(s) acima estão fora da curva padrão. Há {num_outliers} outliers.")