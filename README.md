# Calculadora de rendimento - CRA | MGA
Essa calculadora é baseada no regimento do <a href=http://www.prograd.ufu.br/sites/prograd.ufu.br/files/media/arquivo/guia_academico2018_1_engenharia_de_computacao_uberlandia_1.pdf >guia acadêmico 2018</a> da engenharia da computação. As fórmulas utlizadas nesse código se encontram nas páginas 58 e 59.

## O que é CRA?
CRA é o Coeficiente de Rendimento Acadêmico, comumente utilizado em processos seletivos, uma vez que é um cálculo efetuado com base nas notas adquiridas pelo discente durante os semestres na faculdade.
## O que é MGA?
MGA é a média geral acumulada, e é utilizado em casos excepcionais em que não é evidenciado o CRA.

*Vale ressaltar que essas coeficientes/índices variam de universidade para universidade*


## Sobre o código
Fiz o somatório levando em consideração a distinção entre carga horária **cursada** (CHc) e carga horária **matriculada** (CHm).
Sendo que o primeiro contempla apenas os componentes curriculares cursados com **reprovação/aprovação**,
e o segundo contempla os componentes cursados e com **trancamento parcial**.
Além disso, é preciso considerar em um segundo fator: a carga horária em componentes com **reprovação por frequência** (CHrf).

Outro aspecto é a desconsideração dos primeiros trancamentos parciais em relação à carga horária total dos cursos.

Isso associado à possibilidade de escolher quantos semestres entrarão no cálculo do Coeficiente de Rendimento Acadêmico.
O que torna possível calcular mais de um semestre e realizar a média dos resultados. 

## Como usar:
1 - Se você ainda não tem o Git instalado em sua máquina, você pode baixá-lo e instalá-lo a partir do site oficial do Git. Siga as instruções de instalação adequadas para o seu sistema operacional.<br/><br/>2 - Abra o terminal (Linux/Mac) ou o Git Bash (Windows) e navegue até o diretório onde você deseja armazenar o projeto. Em seguida, use o seguinte comando para clonar o repositório: `git clone https://github.com/me15degrees/calculadora-rendimento-ufu.git`<br/><br/>3 - Navegue para o diretório do projeto usando o comando cd: `cd calculadora-rendimento-ufu`<br/><br/>4 - Use pip install para o rich_menu: `pip install rich_menu` (crie um ambiente virutal antes)<br/><br/>5 - Verificar se possui python instalado, para isso entre no site oficial e siga as instruções de instalação adequadas para o seu sistema operacional.<br/><br/>6 - Depois de instalar as dependências, você pode executar o projeto com o seguinte comando: `python contas.py`.<br/><br/>

<div align="center">
Follow me:
  
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/maria-eduarda-nascimento-andrade-bb0b86213/)
  [![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=flat&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCh6sgz1ij_my64lX8rQnPXg)
  [![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=flat&logo=spotify&logoColor=white)](https://open.spotify.com/user/223w3q4xdm4pquahzl5xhfpia?si=t08g7SlVRvqhF0LseXTyXg&nd=1&dlsi=87356229bcf14264)
  [![Last.fm](https://img.shields.io/badge/Last.fm-D51007?style=flat&logo=last.fm&logoColor=white)](https://www.last.fm/user/me15degrees)
  

</div>
