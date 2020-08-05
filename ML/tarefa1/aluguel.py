# Atividade Avaliativa 

### Membros 
# * Andre Herman Freire Bezerra - 20202000080
# 
# ### Descrição Geral
# * O objetivo desta atividade é propocionar um problema em que os estudantes 
# fiquem mais livres para investigar modelos de _Machine Learning_ para tarefas 
# de regressão.
# * A equipe deve avaliar o resultado do modelo escolhido.
# * Veja as instruções nas seções de treinamento e avaliação.
# 
# # Problemática:
# ### Utilizando a base de dados sobre alugueis tente estimar um valor de aluguel para um imóvel com as seguintes condições (um exemplo de teste):
# - Tipo: Apartamento
# - Bairro: Centro
# - Quartos: 2
# - Vagas (na garagem): 1
# - Area: 80
# - Condominio: 700
# - IPTU: 400
# 
# ## 1 - Importando a base de dados
# * Este exemplo mostra como carregar os dados a partir do google drive
# * A forma como o carregamento dos dados será feita é livre 
# * A base de dados está neste link: [aluguel_residencial.csv](https://drive.google.com/file/d/1hmJsg7X8HT2KDs_ThSzU25edpStDyqBs/view?usp=sharing)

# Importando as bibliotecas

import pandas as pd
import numpy as np

# Esse foi o caminho do meu google drive
# Escolha uma pasta e atualize aqui
# Uma sugestão: crie uma pasta com o nome "dados" na raiz do seu google drive, coloque o arquivo de dados e abra com seguinte caminho "/content/drive/My Drive/dados/aluguel_residencial.csv"
data = pd.read_csv("aluguel_residencial.csv", sep = ";") # Lê um arquivo csv importado localmente

print(data.head()) # Exibe os 5 primeiros dados

### Conhecendo mais sobre a base de dados

print(data.describe())

### Conhecendo melhor os campos não numéricos

#### Campo "Tipo":

print(data.groupby(["Tipo"]).mean())

#### Campo "Bairro":

print(data.groupby(["Bairro"]).mean())

# analisando visualmente a relação entre os dados
import matplotlib.pyplot as plt
import seaborn as sns
#sns.pairplot(data, height=1.5)
#plt.tight_layout()
#plt.show()


# imprimindo valores únicos das colunas Tipo e Bairro
tipos = data.Bairro.unique()
bairros = data.Tipo.unique()
print(tipos)
print(bairros)

## 2 - Treinamento 
# * Escolha um dos algoritmos estudados até o momento e realize o treinamento
# * Use algoritmos para regressão (preço do aluguel)   
# * A escolha dos atributos da base de dados é livre 
# * Discuta sobre suas escolhas e deixe registrado aqui 
from sklearn.linear_model import LinearRegression # minimize the root mean square error between the observed targets in the dataset and the targets predicted by the linear approximation.
y = data['Valor']
x = data[['Quartos', 'Vagas', 'Suites', 'Area', 'Condominio', 'IPTU', 'Valor m2']]

reg = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False).fit(x,y)

### 2.1 - Análise sem condomínio, vagas e iptu
# Após visualizar os resultados, decidimos testar o modelo sem as features 
#   condominio, vagas e IPTU devido à baixa contribuição de cada um individualmente.
#   Os coeficientes resultantes foram próximos de zero, indicando uma baixa contribuição.
# O resultado foi um modelo mais simples (com menos parametros) e com resultados
#   muito similares (a diferença do score é da ordem de 10E-5)
x_no_cond = data[['Quartos', 'Suites', 'Area', 'Valor m2']]
reg_no_cond = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False).fit(x_no_cond,y)

#sns.pairplot(x_no_cond, height=1.5)
#plt.tight_layout()
#plt.show()

### 2.2 - Adicionando Tipo ao modelo
# Utilizando OneHotEncoding pois os dados são categóricos porém não possuem ordem
#   (ou níveis hierárquicos) como:
#   - graduação, mestrado, doutorado; ou
#   - Junior, Pleno, Senior
#   Para os casos de ordem nos dados, utilizar LabelEncoding.
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder()
tmp = ohe.fit_transform(data.Tipo.values.reshape(-1,1)).toarray()
print(data.shape)
dataOH = pd.DataFrame(tmp, columns = ["Tipo_"+str(int(i)) for i in range(5)])
x_tipo = pd.concat([x_no_cond, dataOH], axis=1)
print(x_tipo.head())

reg_tipo = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False).fit(x_tipo,y)

### 2.3 - Adicionando Bairro ao modelo
# Utilizando OneHotEncoding
ohe = OneHotEncoder()
tmp = ohe.fit_transform(data.Bairro.values.reshape(-1,1)).toarray()
print(data.shape)
dataOH = pd.DataFrame(tmp, columns = ["Bairro_"+str(int(i)) for i in range(151)])
x_bairro = pd.concat([x_no_cond, dataOH], axis=1)
print(x_bairro.head())

reg_bairro = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False).fit(x_bairro,y)


x_tipo_bairro = pd.concat([x_tipo, dataOH], axis=1)
print(x_tipo_bairro.head())
reg_tipo_bairro = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False).fit(x_tipo_bairro,y)


##3 - Avaliação dos Resultados 
# * Use uma métrica para avaliar a qualidade do treinamento 
# * Você pode usar o Erro quatrático Médio (MSE)
# * Para mais opções acesse: https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics 

print("\n\nParametros da regresão:")
print(reg.get_params())

print("\nCoeficientes:")
print(" Todos:                        ", reg.coef_, "\n", 
      "Sem condominio, vagas e IPTU: ", reg_no_cond.coef_, "\n", 
      "Com o tipo:                   ", reg_tipo.coef_, "\n", 
      "Com o Bairro:                 ", reg_bairro.coef_, "\n", 
      "Com Tipo e Bairro:            ", reg_tipo_bairro.coef_)

print("\nIntercepto-y:")
print(" Todos:                        ", reg.intercept_, "\n", 
      "Sem condominio, vagas e IPTU: ", reg_no_cond.intercept_, "\n",  
      "Com o tipo:                   ", reg_tipo.intercept_, "\n",  
      "Com o Bairro:                 ", reg_bairro.intercept_, "\n",  
      "Com Tipo e Bairro:            ", reg_tipo_bairro.intercept_)

print("\nCoeficiente de determinação (r^2):")
print(" Todos:                        ", reg.score(x,y), "\n", 
      "Sem condominio, vagas e IPTU: ", reg_no_cond.score(x_no_cond, y), "\n", 
      "Com o tipo:                   ", reg_tipo.score(x_tipo,y), "\n", 
      "Com o Bairro:                 ", reg_bairro.score(x_bairro,y), "\n", 
      "Com Tipo e Bairro:            ", reg_tipo_bairro.score(x_tipo_bairro,y))

# Discussão:
# Adicionar o Tipo como um parametro categórico aumentou o score do modelo,
#  o que reflete em predições mais precisas.
# Adicionar o Bairro não se mostrou interessante. Os relativos aos bairros apresentaram
#   valores iguais, indicando que o preço independe (ou depende igualmente) da localização
# Entretanto, quando considerado tanto o Tipo quanto o Bairro, o score aumentou.
