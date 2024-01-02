# O que é o critério de Chauvenet?
O Critério de Chauvenet é uma abordagem estatística utilizada para avaliar a possibilidade de um ponto de dados em um conjunto de observações ser considerado um valor atípico (outlier). Desenvolvido pelo estatístico norte-americano William Chauvenet, o critério é frequentemente empregado em disciplinas como estatística, metrologia e análise de dados.

O método de Chauvenet baseia-se na suposição de que os dados seguem uma distribuição normal. Ele estabelece um limite superior para a probabilidade de um dado ponto ser considerado um outlier, comumente fixando esse limite em 0,5% (ou 1 em 200). Caso a probabilidade de um ponto ser considerado um outlier ultrapasse esse limite, o ponto é rejeitado.

Para determinar se um ponto é um outlier, o critério de Chauvenet utiliza a média e o desvio padrão da amostra. O procedimento consiste em calcular a probabilidade de um ponto distar mais do que uma certa quantidade de desvios padrão da média e, se essa probabilidade for inferior ao limite preestabelecido, o ponto é considerado um outlier.
## Passo a passo dos cálculos:
1 - Calcular a média e o desvio padrão da amostra.<br><br>2 - Calcular a distância de cada ponto em relação à média em unidades de desvio padrão (z-score).<br><br>3 - Calcular a probabilidade de cada z-score usando a distribuição normal padrão.<br><br>4 - Calcular o limite de corte usando a fórmula 1−1/4n​.<br><br>5 - Identificar os pontos cujas probabilidades de cauda direita são menores que o limite como outliers.
