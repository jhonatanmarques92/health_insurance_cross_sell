[![Linkedin](https://img.shields.io/badge/-linkedin-blue?logo=linkedin&link=https://www.linkedin.com/in/jhonatanmarques/)](https://www.linkedin.com/in/jhonatanmarques/)

# Health insurance cross sell
<p align="center"><img src="https://github.com/jhonatanmarques92/health_insurance_cross_sell/blob/main/img/transito.jpg" width="590" height="300"></p>
Projeto de Learn to Rank, com o objetivo de fazer um ranqueamento de clientes com maior interesse em adquirir um seguro veicular.

### Observação: O contexto do problema de negócio não é real

## Questão de Negócio
A Insurance All é uma empresa com o foco em vendas de seguro saúde, mas está analisando a possibilidade de oferecer um seguro veicular. O novo produto, os clientes precisarão pagar uma anualidade destinado aos custos de acidentes e danos veiculares.  
A Insurance All fez uma pesquisa com 304887 clientes sobre o interesse em adquirir o novo produto, após, selecionaram 127037 novos clientes que não responderam a pesquisa para que o time de vendas possa entrar em contato e oferecer o seguro.  
Antes de iniciar a campanha de vendas do seguro veicular, foi constatado que o time de venda tem a capacidade de efetuar apenas 20 mil ligações durante o período estabelecido.  

## Entendimento do Negócio
- **Objetivo:** Construir um ranking de clientes com maior interessa em adquirir o produto, maximizar as vendas no menor número de ligações.
- **Perguntas as serem respondidas**
  - Qual a porcentagem de vendas efetuadas com as 20 mil ligações?
  - Qual a porcentagem de vendas efetuadas caso o time de vendas consiga fazer 30 mil ligações?
- **Entrega da solução:** Uma planilha no Google Sheets, com um botão que irá fazer o ranqueamento.

## Informação dos dados
Os dados foram retirados do Kaggle: https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction

| Colunas | Descrição |
| ------- | --------- |
| Id      | Código de identificação do cliente |
| Gender	| Gênero do cliente |
| Age	    | Idade do cliente |
| Driving_License | Se o cliente possui ou não habilitação |
| Region_Code | Código único da ragião |
| Previously_Insured | Se o cliente possui ou não seguro veicular |
| Vehicle_Age | Idade do veículo |
| Vehicle_Damage | Se o veículo do cliente já foi ou não danificado |
| Annual_Premium | Valor que o cliente precisa pagar como prêmio no ano |
| PolicySalesChannel | Côdigo do canal de divulgação ao cliente |
| Vintage | Número de dias que o cliente é associado |
| Response | Resposta se o cliente estaria ou não interessado no produto |

## Estratégia de solução
Para solucionar o problema, foi utilizado o CRISP-DS, uma metodologia cíclica para o andamento de cada etapa do desenvolvimento do projeto.  
<p align="center"><img src="https://github.com/jhonatanmarques92/rossmann_sales_prediction/blob/main/img/crisp-ds.png" width="650" height="400"></p>

- **Questão e entendimento do negócio:** Recebimento do problema de negócio, onde se dará início no planejamento da solução e nas respostas.
- **Coleta dos dados:** Arquivos em csv, disponível no Kaggle.
- **Descrição dos dados:** Renomear as colunas e fazer uma análise descritiva.
- **Feature engineering:** Criação do mapa mental e a lista de hipóteses.
- **Análise exploratória dos dados:** 
  - Análise univariada: Verificar distribuição e outliers das features.
  - Análise bivariada: Respondendo as hipóteses, procurando insights.
  - Análise multivariada: Criando um mapa de calor com as correlações entre as features.
- **Preparação dos dados:** Ápos realizar a separação dos dados de treino e teste, foi aplicado as técnicas abaixo.
  - Normalização para features numéricas com a distribuição normal.
  - Rescaling para features numéricas que não possuem uma distribuição normal.
  - Encoding para features categóricas.
- **Seleção de features:** Utilizado o feature_importances de um algoritmo ensamble (Extra Tree Classifier), pois o Boruta retornou apenas duas features como relevante, para selecionar apenas as mais importantes.
- **Modelos de Machine Learning:** Utilizado 5 algoritmos para o treinamento do modelo (Logistic Regression, KNN, Random Forest, Extra Trees e XGBoost), utilizando cross validation e analisando algumas métricas (precision top K, recall top K, curva de ganho cumulativo e curva lift).
- **Fine Tunning:** Testando parâmentros diferentes no melhor modelo, tentando aumentar a perfomance.
