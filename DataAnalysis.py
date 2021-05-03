import pandas as pd

url_dados = 'https://github.com/alura-cursos/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true'

dados = pd.read_csv(url_dados, compression = 'zip')
dados
##Mostra a tabela de informações./ Shows the list of informations.

dados.head()
##Mostra os primeiros 5 elementos da tabela.

dados.shape
##Mostra os conteúdos presentes na tabela.

dados['tratamento']
##Mostra somente a ala da tabela que trata dos tratamentos.

dados['tratamento'].unique()
##Mostra os elementos únicos presentes na na ala tratamentos.

dados['tempo'].unique()
##Outro exemplo de como Unique funciona.

dados['dose'].unique()
##Mesma coisa lol

dados['droga'].unique()
##...

dados['tratamento'].value_counts()
##Mostra o valor absoluto dos elementos presentes na ala de tratamentos. No caso, com_droga tem 21948 valores, e com_controle tem 1866.

dados['dose'].value_counts()
##Mostra o valor absoluto dos elementos presentes na ala de dose. no caso, D1 tem 12147 valores, e D2 tem 11667.

dados['tratamento'].value_counts(normalize = True)
##Mostra o valor percentual entre os elementos presentes na ala de tratamentos. No caso, com_droga tem 0.921643, e com_controle 0.078357.

dados['dose'].value_counts(normalize = True)
##Mostra o valor percentual entre os elementos presentes na ala de valor. No caso, D1 tem 0.510078, e D2 0.489922.

plt.pie(dados['tratamento'].value_counts(), explode=[0, 0.1], autopct='%1.3f%%', shadow = True)
plt.title('Gráfico que indica o tratamento com drogas e sem drogas')
plt.legend(labels=['Com droga ', 'Sem droga'], loc= 'best')
plt.show()
##Gráfico de Pizza que indica o percentual dos valores nele representados. A parcela Sem_droga(com_controle), salta um pouco para fora do gráfico por conta da função explode presente no Pandas.

plt.pie(dados['tempo'].value_counts(), autopct='%1.2f%%', shadow = True)
plt.title('Tempo em que a cultura ficou sob efeito de drogas')
plt.legend(labels=['48 horas', '72 horas', '24 horas'], loc= 'best')
plt.show()
##Gráfico de Pizza que indica o percentual dos valores nele representados.

dados['tempo'].value_counts().plot.bar()
import matplotlib.pyplot as plt
import pandas as pd
plt.title('Horas x Cultura', fontsize =16)
plt.show()
##Gráfico de barras mostrando a relação Cultura x Tempo.

dados_filtrados = dados[dados['g-0']>0]
dados_filtrados.head()
##Uma filtragem dos dados da tabela g-0, mostrando apenas os elementos com valor maior que 0 na lista, e logo em seguida, mostrando apenas os primeiros 5 valores apresentados.
