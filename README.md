# Calculadora de rendimento - CRA | MGA
Essa calculadora é baseada no regimento do guia acadêmico 2018 da engenharia da computação - UFU: [link para a páfina](http://www.prograd.ufu.br/sites/prograd.ufu.br/files/media/arquivo/guia_academico2018_1_engenharia_de_computacao_uberlandia_1.pdf)
As fórmulas utlizadas nesse código se encontram nas páginas 58 e 59.

## O que é CRA?
CRA é o Coeficiente de Rendimento Acadêmico, comummente utilizado em processos seletivos, uma vez que é um cálculo efetuado com base nas notas adquiridas pelo discente durante os semestres na faculdade.
## O que é MGA?
MGA é a média geral acumulada, e é utilizado em casos excepcionais em que não é evidenciado o CRA.
*vale ressaltar que essas coeficientes/índices variam de universidade para universidade *

## Sobre o código
Fiz o somatório levando em consideração a distinção entre carga horária **cursada** (CHc) e carga horária **matriculada** (CHm).
Sendo que o primeiro contempla apenas os componentes curriculares cursados com **reprovação/aprovação**,
e o segundo contempla os componentes cursados e com **trancamento parcial**.
Além disso, é preciso considerar em um segundo fator: a carga horária em componentes com **reprovação por frequência** (CHrf).

Outro aspecto é a desconsideração dos primeiros trancamentos parciais em relação à carga horária total dos cursos.

Isso associado à possibilidade de escolher quantos semestres entrarão no cálculo do Coeficiente de Rendimento Acadêmico.
O que torna possível calcular mais de um semestre e realizar a média dos resultados. 

## Como usar:
1 - Se você ainda não tem o Git instalado em sua máquina, você pode baixá-lo e instalá-lo a partir do site oficial do Git. Siga as instruções de instalação adequadas para o seu sistema operacional.
2 - Abra o terminal (Linux/Mac) ou o Git Bash (Windows) e navegue até o diretório onde você deseja armazenar o projeto. Em seguida, use o seguinte comando para clonar o repositório: git clone https://github.com/me15degrees/calculadora-rendimento-ufu.git
3 - Navegue para o diretório do projeto usando o comando cd: cd nome-do-repositorio
4 - Use pip install para o rich_menu: pip install rich_menu (crie um ambiente virutal antes)
5 - Verificar se possui python instalado, para isso entre no site oficial e siga as instruções de instalação adequadas para o seu sistema operacional.
6 - Depois de instalar as dependências, você pode executar o projeto com o seguinte comando: python 'nome do arquivo.py'.

dica -> para a lista de dependências específicas do projeto você pode usar o seguinte comando: pip install -r requirements.txt


