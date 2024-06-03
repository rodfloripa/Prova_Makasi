#!/usr/bin/env python
# coding: utf-8

# # Requisitos Técnicos para a entrega do teste

# Requisitos Técnicos para a entrega do teste
# 
# • Sugerimos a utilização de Python para o desenvolvimento do código.
# 
# Foi usado python
# 
# 
# 
# • Utilize seus padrões de organização de projeto, documentação e código.
# 
# O código está documentado e organizado
# 
# 
# 
# • Pode ser utilizada qualquer lib adicional que julgar importante para o bom funcionamento da exploração dos datasets, mas não se esqueça de dar as orientações de instalação delas (caso seja necessário).
# 
# As bibliotecas estão em requirements.txt
# 
# 
# 
# • Caso haja uma aplicação em código, está será rodada em localhost.
# 
# Roda local desde que voce tenha jupyter instalado: https://jupyter.org/install
# 
# 
# 
# • Ainda na documentação, explicar a sua motivação de escolha das libs e frameworks (ou o motivo de ter feito na mão). Uma explicação sobre a estrutura do projeto também será bem vinda.
# 
# Foram usadas as bibliotecas mais comuns para analise de dados em python,como pandas,numpy,sklearn e statsmodels
# 
# 
# 
# • É imprescindível que caso use código para executar o teste, este funcione corretamente em qualquer máquina.
# 
# Foi fornecido o arquivo requirements.txt para que rode em qualquer máquina
# 
# 
# 
# • Documentos adicionais (PDF, PowerPoint, Planilhas e etc) ao teste devem ser compartilhados e enviados para fabiane+dados@makasi.com.br
# 
# Não existem documentos adicionais

# # Leitura e Tratamento de Dados

# ## Tratamento da amostra 1


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

proj1 = pd.read_csv('amostra_projeto1.csv')
proj1 = proj1['Unnamed: 13'].tail(152)
proj1 = pd.DataFrame(proj1)
proj1 = proj1.replace('Total',0)
df1 = proj1.replace('[R$]', '', regex=True).astype(str)
df1['Unnamed: 13'] = df1['Unnamed: 13'].str.strip()
df1['Unnamed: 13'] = df1['Unnamed: 13'].str.replace('.','')
df1['Unnamed: 13'] = df1['Unnamed: 13'].str.replace(',','.')
df1 = df1['Unnamed: 13'].astype(str).astype(float)
valor = np.round(df1.sum(),1)

proj1 = pd.read_csv('amostra_projeto1.csv').head(8)
proj1 = proj1[['DADOS','Unnamed: 1']].tail(7)
df2 = {'DADOS':'Valor','Unnamed: 1': valor}
proj1 = proj1.append(df2, ignore_index = True)
proj1 = proj1.rename(columns={'Unnamed: 1': 'X'}) 

# ## Tratamento da amostra 2

proj2 = pd.read_csv('amostra_projeto_2.csv')
proj2 = proj2['Unnamed: 13'].tail(162)
proj2 = pd.DataFrame(proj2)
proj2 = proj2.replace('Total',0)
df2 = proj2.replace('[R$]', '', regex=True).astype(str)
df2['Unnamed: 13'] = df2['Unnamed: 13'].str.strip()
df2['Unnamed: 13'] = df2['Unnamed: 13'].str.replace('.','')
df2['Unnamed: 13'] = df2['Unnamed: 13'].str.replace(',','.')
df2 = df2['Unnamed: 13'].astype(str).astype(float)
valor = np.round(df2.sum(),1)

proj2 = pd.read_csv('amostra_projeto_2.csv').head(8)
proj2 = proj2[['DADOS','Unnamed: 1']].tail(7)
df2 = {'DADOS':'Valor','Unnamed: 1': valor}
proj2 = proj2.append(df2, ignore_index = True)
proj2 = proj2.rename(columns={'Unnamed: 1': 'Y'}) 


# ## Tratamento da amostra 3


proj3 = pd.read_csv('amostra_projeto_3.csv')
proj3 = proj3['Unnamed: 13'].tail(157)
proj3 = pd.DataFrame(proj3)
proj3 = proj3.replace(' Total',0)
df3 = proj3.replace('[R$]', '', regex=True).astype(str)
df3['Unnamed: 13'] = df3['Unnamed: 13'].str.strip()
df3['Unnamed: 13'] = df3['Unnamed: 13'].str.replace('.','')
df3['Unnamed: 13'] = df3['Unnamed: 13'].str.replace(',','.')
df3 = df3['Unnamed: 13'].astype(str).astype(float)
valor = np.round(df3.sum(),1)

proj3 = pd.read_csv('amostra_projeto_3.csv').head(8)
proj3 = proj3[['DADOS','Unnamed: 1']].tail(7)
df2 = {'DADOS':'Valor','Unnamed: 1': valor}
proj3 = proj3.append(df2, ignore_index = True)
proj3 = proj3.rename(columns={'Unnamed: 1': 'Z'}) 

# ## Tratamento da amostra 4

proj4 = pd.read_excel('amostras_projetos.xlsx',engine='openpyxl')
proj4 = proj4['Unnamed: 13'].tail(152)
proj4 = pd.DataFrame(proj4)
proj4 = proj4.replace('Total',0)
df4 = proj4.replace('[R$]', '', regex=True).astype(str)
df4['Unnamed: 13'] = df4['Unnamed: 13'].str.strip()
df4 = df4['Unnamed: 13'].astype(str).astype(float)
valor = np.round(df4.sum(),1)
proj4 = pd.read_csv('amostra_projeto_3.csv').head(8)
proj4 = proj4[['DADOS','Unnamed: 1']].tail(7)
df2 = {'DADOS':'Valor','Unnamed: 1': valor}
proj4 = proj4.append(df2, ignore_index = True)
proj4 = proj4.rename(columns={'Unnamed: 1': 'Z1'}) 


# ## Amostra de previsão

teste = pd.read_csv('projeto_4.csv').head(8)
teste = teste.replace({'Térrea':1,'Sobrado':2}).T
teste = teste.replace(',', '.', regex=True)

# ## Concatenando dados

dados = pd.concat([proj1, proj2['Y'],proj3['Z'],proj4['Z1']], axis=1)
dados = dados.replace({'Térrea':1,'Sobrado':2}).T
dados = dados.replace(',', '.', regex=True).astype(str)
dados.columns = dados.iloc[0]

# # Análise Exploratória

d = dados[1:].reset_index().drop(['index'],axis=1).astype(float)
pd.plotting.scatter_matrix(d,figsize=(12, 12),diagonal='hist');

# É possivel ver as correlações positivas entre 'Valor' e 'Qtde BWC','Area Fundação' e 'Area Terreno'.É importante notar que estas correlações não são perfeitas
# As variáveis de área são bastante correlacionadas

import matplotlib.pyplot as plt

for column in d:
    plt.figure()
    d.boxplot([column])

# É possível perceber que Tipologia térrea(1) é um outlier,assim como Area do Terreno 300 e Valor do Orçamento 4569025.2

# # Previsão do Orçamento

# #### As variáveis correlacionadas serão removidas com o calculo do VIF

from statsmodels.stats.outliers_influence import variance_inflation_factor
# remover variaveis correlacionadas
dados2 = dados.copy()
dados2.columns = dados.iloc[0]
dados2 = dados2[1:]
dados2 = dados2.drop(dados2.columns[[2,3,4,5,6,7]], axis=1).apply(pd.to_numeric)

# calcular VIF
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(dados2.values, i) for i in range(dados2.shape[1])]
vif["features"] = dados2.columns

# #### Várias combinações foram testadads,mas o menor VIF foi obtido com as variáveis Tipologia e Area do Terreno. Estas duas variáveis serão utilizadas na regressão linear.
# #### A regressão linear foi escolhida pela relação linear entre o valor e as variáveis,observada na análise exploratória.Um modelo de árvore regressiva não teria melhores resultados que # a regressão.



from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error

X = dados2[['Tipologia','Área Terreno' ]].apply(pd.to_numeric)
X = X.to_numpy()
y = dados['Valor'][1:].apply(pd.to_numeric).to_numpy()
reg = LinearRegression().fit(X, y)
reg.score(X, y)
y_pred = reg.predict(X)
mape = mean_absolute_percentage_error(y, y_pred)
print('sklearn MAPE: {:.2f}'.format(mape))


# #### O MAPE é de 9%,ou seja, Acurácia de 91%

prev = reg.predict((teste[[1,2]].to_numpy()[1].astype(np.float)).reshape(1,-1)) 
orc = pd.DataFrame({'Orçamento': y,'Orçamento Previsto': y_pred})
orc['Erro Absoluto']= abs(orc['Orçamento']-orc['Orçamento Previsto'])
orc['Erro Percentual(%)'] = 100*orc['Erro Absoluto']/orc['Orçamento Previsto']
orc.round(2)

# O máximo erro percentual será usado como erro na previsão do orçamento


print('A previsão de orçamento é de R$ {:.1f} +- {:.1f}'.format(prev[0],(max(orc['Erro Percentual(%)'])/100)*prev[0]))


# ### Historias

# 
# • Como orçamentista, eu gostaria de um previsão do orçamento da casa denominada "Projeto 4" em reais.
# 
# 
print('Como orçamentista, eu gostaria de um previsão do orçamento da casa denominada "Projeto 4" em reais.')
print('A previsão de orçamento é de R$ {:.1f}'.format(prev[0]))


# • Como engenheiro responsável pelo projeto, eu gostaria de ter a documentação completa do método usado para chegar ao valor previsto para o "Projeto 4", incluindo cálculos.
print('Como engenheiro responsável pelo projeto, eu gostaria de ter a documentação completa do método usado para chegar ao valor previsto para o "Projeto 4", incluindo cálculos.')
print("Os cálculos foram mostrados nesse notebook jupyter")
print("Regressão linear")
print("intercepto",reg.intercept_)
print("coeficicentes de Tipologia e Area do Terreno",reg.coef_)


# • Como gerente comercial da conta do cliente do "Projeto 4", eu gostaria de ter uma base estatística para indicar o quão aproximado o valor estipulado está da realidade, e no caso de variação, quanto esse valor pode variar.
# 
print('Como gerente comercial da conta do cliente do "Projeto 4", eu gostaria de ter uma base estatística para indicar o quão aproximado o valor estipulado está da realidade')
print('A previsão de orçamento é de R$ {:.1f} +- {:.1f}'.format(prev[0],(max(orc['Erro Percentual(%)'])/100)*prev[0]))


# • Como responsável pela gestão de risco de projetos, eu gostaria de entender o risco implícito nessa previsão, indicando o que pode impactar em outliers ou variações acima do previsto.
print('Como responsável pela gestão de risco de projetos, eu gostaria de entender o risco implícito nessa previsão')
# Como só tenho 4 orçamentos seria interessante obter mais orçamentos para avaliar o risco,mas nos orçamentos analisados o erro não foi
# maior que +-18.3% do valor previsto.
print('Como só tenho 4 orçamentos seria interessante obter mais orçamentos para avaliar o risco,mas nos orçamentos analisados o erro não foi maior que +-18.3% do valor previsto.')
