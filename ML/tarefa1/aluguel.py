# Atividade Avaliativa 

### Membros 
# * Andre Herman Freire Bezerra - 20202000080
 
# # Problemática:
# ### Utilizando a base de dados sobre alugueis tente estimar um valor de aluguel para um imóvel com as seguintes condições (um exemplo de teste):
# - Tipo: Apartamento
# - Bairro: Centro
# - Quartos: 2
# - Vagas (na garagem): 1
# - Area: 80
# - Condominio: 700
# - IPTU: 400
 
# ## 1 - Importando a base de dados

# Importando as bibliotecas

import pandas as pd
import numpy as np

data = pd.read_csv("aluguel_residencial.csv", sep = ";") # Lê um arquivo csv importado localmente
data_pred = pd.read_csv("predicoes.csv", sep = ";") # Lê um arquivo csv importado localmente

#print(data.head()) # Exibe os 5 primeiros dados

### Conhecendo mais sobre a base de dados

print(data.describe())

### Conhecendo melhor os campos não numéricos

#### Campo "Tipo":

#print(data.groupby(["Tipo"]).mean())

#### Campo "Bairro":

#print(data.groupby(["Bairro"]).mean())

# analisando visualmente a relação entre os dados
import matplotlib.pyplot as plt
import seaborn as sns
#sns.pairplot(data, height=1.5)
#plt.tight_layout()
#plt.show()


# imprimindo valores únicos das colunas Tipo e Bairro
tipos = data.Tipo.unique()
bairros = data.Bairro.unique()
#print(tipos)
#print(bairros)

## 2 - Treinamento 
# * Escolha um dos algoritmos estudados até o momento e realize o treinamento
# * Use algoritmos para regressão (preço do aluguel)   
# * A escolha dos atributos da base de dados é livre 
# * Discuta sobre suas escolhas e deixe registrado aqui 

# O algoritmo escolhido foi o de regressão linear múltipla da biblioteca do scikit learn.
# Foram elaboradas seis regressões lineares, resultando em seis modelos que simulam seis 
#   diferentes cenários com diferentes atributos. Os cenários são os seguintes:
#     1) Não leva em consideração os atributos não numéricos
#     2) Igual ao cenário 1, porém descartando os atributos Condomínio, Vagas e IPTU
#     3) Igual ao cenário 2, porém adicionando o atributo Tipo
#     4) Igual ao cenário 2, porém adicionando o atributo Bairro
#     5) Igual ao cenário 2, porém adicionando os atributos Tipo e Bairro
#     6) Igual ao cenário 1, porém descartando o atributo Valor m2
#
# O cenário 1 serviu como base de exploração para a escolha dos demais cenários.
# Analisando os resultados do cenário 1, decidiu-se testar um modelo sem os atributos 
#   condominio, vagas e IPTU devido à baixa contribuição de cada um individualmente.
#   Esse é o cenário 2.
# Os coeficientes resultantes desses atributos no cenário 1 foram próximos de zero, 
#   indicando a baixa contribuição.
# O resultado foi um modelo mais simples (cenário 2, com menos parametros) e com resultados
#   similares ao cenário 1 (a diferença do score é da ordem de 10E-5).
# Com os resultados do cenário 2, decidiu-se testar os atributos não numéricos. 
# O atributo Tipo foi adicionado ao cenário 2, gerando o cenário 3.
# O atributo Bairro foi adicionado ao cenário 2, gerando o cenário 4.
# Os dois atributos (Tipo e Bairro) foram adicionados ao cenário 2, gerando o cenário 5.
# A idéia dos cenários 3, 4 e 5 é o de analisar a influência desses atributos no valor
#   da predição, tanto de maneira isolada como conjunta.
# Finalmente, o cenário 6 foi pensado para verificar a influencia do atributo Valor m2, 
#   uma vez que um modelo bem simples seria simplesmente multiplicar o valor do m2 pela área
#   do imíovel para se ter uma estimativa do valor do aluguel.


from sklearn.linear_model import LinearRegression # minimize the root mean square error between the observed targets in the dataset and the targets predicted by the linear approximation.

### 2.1 Todos os atributos numéricos
y = data['Valor']
x = data[['Quartos', 'Vagas', 'Suites', 'Area', 'Condominio', 'IPTU', 'Valor m2']]
x_pred = data_pred[['Quartos', 'Vagas', 'Suites', 'Area', 'Condominio', 'IPTU', 'Valor m2']]

reg = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False).fit(x,y)

y_pred = reg.predict(x_pred)
print("\n\nValores das predições do imóvel emn cada cenário:\n")
print("1) ", y_pred)

### 2.2 - Análise sem condomínio, vagas e iptu
x_no_cond = data[['Quartos', 'Suites', 'Area', 'Valor m2']]
x_pred_no_cond = data_pred[['Quartos', 'Suites', 'Area', 'Valor m2']]
reg_no_cond = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False).fit(x_no_cond,y)

y_pred_no_cond = reg_no_cond.predict(x_pred_no_cond)
print("2) ", y_pred_no_cond)

#sns.pairplot(x_no_cond, height=1.5)
#plt.tight_layout()
#plt.show()

### 2.3 - Adicionando Tipo ao modelo
# Utilizando OneHotEncoding pois os dados são categóricos porém não possuem ordem
#   (ou níveis hierárquicos) como:
#   - graduação, mestrado, doutorado; ou
#   - Junior, Pleno, Senior
#   Para os casos de ordem nos dados, utilizar LabelEncoding.
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder()
tmp = ohe.fit_transform(data.Tipo.values.reshape(-1,1)).toarray()
#print(data.shape)
dataOH = pd.DataFrame(tmp, columns = ["Tipo_"+str(int(i)) for i in range(5)])
x_tipo = pd.concat([x_no_cond, dataOH], axis=1)
x_pred_tipo = pd.concat([x_pred_no_cond, dataOH], axis=1)
#print(x_tipo.head())

reg_tipo = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False).fit(x_tipo,y)

y_pred_tipo = reg_tipo.predict(x_pred_tipo.iloc[:1,:])
print("3) ", y_pred_tipo)

### 2.4 - Adicionando Bairro ao modelo
# Utilizando OneHotEncoding
ohe = OneHotEncoder()
tmp = ohe.fit_transform(data.Bairro.values.reshape(-1,1)).toarray()
#print(data.shape)
dataOH = pd.DataFrame(tmp, columns = ["Bairro_"+str(int(i)) for i in range(151)])
x_bairro = pd.concat([x_no_cond, dataOH], axis=1)
x_pred_bairro = pd.concat([x_pred_no_cond, dataOH], axis=1)
#print(x_bairro.head())

reg_bairro = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False).fit(x_bairro,y)

y_pred_bairro = reg_bairro.predict(x_pred_bairro.iloc[:1,:])
print("4) ", y_pred_bairro)

### 2.5 - Adicionando Tipo e Bairro ao modelo
x_tipo_bairro = pd.concat([x_tipo, dataOH], axis=1)
x_pred_tipo_bairro = pd.concat([x_pred_tipo, dataOH], axis=1)
#print(x_tipo_bairro.head())
reg_tipo_bairro = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False).fit(x_tipo_bairro,y)

y_pred_tipo_bairro = reg_tipo_bairro.predict(x_pred_tipo_bairro.iloc[:1,:])
print("5) ", y_pred_tipo_bairro)

### 2.6 Análise sem valor por m2
x_no_m2 = data[['Quartos', 'Vagas', 'Suites', 'Area', 'Condominio', 'IPTU']]
x_pred_no_m2 = data_pred[['Quartos', 'Vagas', 'Suites', 'Area', 'Condominio', 'IPTU']]

reg_no_m2 = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False).fit(x_no_m2,y)

y_pred_no_m2 = reg_no_m2.predict(x_pred_no_m2)
print("6) ", y_pred_no_m2)


##3 - Avaliação dos Resultados 
# * Use uma métrica para avaliar a qualidade do treinamento 
# * Você pode usar o Erro quatrático Médio (MSE)
# * Para mais opções acesse: https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics 

resumo = True

if resumo:
    print("\n\nParametros da regresão:")
    print(reg.get_params())
    
    #print("\nCoeficientes:")
    #print(" Todos:                        ", reg.coef_, "\n", 
    #      "Sem condominio, vagas e IPTU: ", reg_no_cond.coef_, "\n", 
    #      "Com o tipo:                   ", reg_tipo.coef_, "\n", 
    #      "Com o Bairro:                 ", reg_bairro.coef_, "\n", 
    #      "Com Tipo e Bairro:            ", reg_tipo_bairro.coef_)
    
    #print("\nIntercepto-y:")
    #print(" Todos:                        ", reg.intercept_, "\n", 
    #      "Sem condominio, vagas e IPTU: ", reg_no_cond.intercept_, "\n",  
    #      "Com o tipo:                   ", reg_tipo.intercept_, "\n",  
    #      "Com o Bairro:                 ", reg_bairro.intercept_, "\n",  
    #      "Sem valor por m2:             ", reg_no_m2.intercept_, "\n",  
    #      "Com Tipo e Bairro:            ", reg_tipo_bairro.intercept_)
    
    print("\nCoeficiente de determinação (r^2):")
    print(" 1) Todos                         ", reg.score(x,y), "\n", 
          "2) Sem Condominio, Vagas e IPTU  ", reg_no_cond.score(x_no_cond, y), "\n", 
          "3) Com o Tipo                    ", reg_tipo.score(x_tipo,y), "\n", 
          "4) Com o Bairro                  ", reg_bairro.score(x_bairro,y), "\n", 
          "5) Com Tipo e Bairro             ", reg_tipo_bairro.score(x_tipo_bairro,y), "\n",
          "6) Sem valor por m2              ", reg_no_m2.score(x_no_m2,y))

# Discussão:
# A eficácia da predição foi analisada com base no coeficiente de determinação (r^2), calculado 
#   pela comparação entre os valores observados e preditos (estimados). Ao final, o script apresenta 
#   um sumário contendo os parametros utilizados em todos os cenários e seus valores de r^2.
# Adicionar o Tipo como um parametro categórico aumentou o valor de r^2 do modelo. Esse aumento,
#   porém, não necessariamente justifica o acréscimo de mais um parametro, já que é da ordem de 0.3%.
#   O mesmo pode se dizer para a adição do parametro Bairro isoladamente.
# Entretanto, quando considerado ambos Tipo e Bairro, o valor de r^2 aumentou na ordem de ~2.5%. Isso 
#   indica que existe uma forte correlação entre os atributos Tipo e Bairro. Em outras palavras, 
#   saber que o imóvel é apartamento ou casa, de acordo com esses dados, não necessariamente contribui
#   para o valor do aluguel, porém saber que é um apartamento em Higienópolis significa muito mais para
#   o modelo preditivo.
# Foi observado que o atributo valor por m2 é talvez o mais importante na predição. A eliminação do atributo
#   no ajuste do modelo do cenário 6 é um indício disso, provocando uma redução de 20% no valor de r^2. 

# Conclusões:
# Têm-se, portanto, algumas possibilidades de se escolher um dentre os seis modelos aqui apresentados:
#  1) Escolher o modelo com maior r^2, ou seja, maior precisão estatística. Nesse caso, o modelo seria o
#     do cenário 5. Deve-se saber qual o Tipo de imóvel e qual o Bairro em que ele se encontra.
#  2) No caso de não se conhecer as informações do Tipo e Bairro (difícil de se imaginar, nesse caso)
#     pode-se utilizar o modelo do cenário 2.
