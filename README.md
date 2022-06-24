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
- **Perfomance do modelo:** Respondendo as perguntas de negócio utilizando as métricas.

## Top 3 insights
- Mais de 40% de homens e mulheres possuem seguro veicular.
  - Verdadeiro, pois 50,25% das mulheres possuem seguro veicular, enquanto apenas 42% do homens possuem.

**Mulheres**
| Gender | Previously_Insured | Quantidade de clientes | Porcentagem |
| ------ | ------------------ | ---------------------- | ----------- |
| Female |         0          | 69618                  | 49,77692 %  |
| Female |         1          | 70242                  | 50,22308 %  |

**Homens**
| Gender | Previously_Insured | Quantidade de clientes | Porcentagem |
| ------ | ------------------ | ---------------------- | ----------- |
| Male   |         0          | 95645                  | 57,957183 % |
| Male   |         1          | 69382                  | 42,042817 % |

<p align="center"><img src="https://github.com/jhonatanmarques92/health_insurance_cross_sell/blob/main/img/h4.png" width="820" height="520"></p> 

- Pessoas com menos de 40 anos se acidentam 20% mais.
  - Falso, pessoas com menos de 40 anos se acidentam 18,74% menos

| Idade  | vehicle_damage     | Quantidade de clientes | Porcentagem |
| ------ | ------------------ | ---------------------- | ----------- |
| Maior de 40 anos |     Yes    | 91635                | 59,415667 % |
| Menor de 40 anos |     Yes    | 62592                | 40,584333 % |

<p align="center"><img src="https://github.com/jhonatanmarques92/health_insurance_cross_sell/blob/main/img/h5.png" width="820" height="520"></p>

- Menos de 40% das pessoas com menos de 40 anos dirigem sem seguro no veículo, enquanto mais de 70% das pessoas com mais de 40 anos possuem seguro.
  - Falso, pois 41,53% das pessoas com menos de 40 anos não possuem seguro, 69,6% das pessoas com mais de 40 anos não possuem.

**Maior de 40 anos**
| Idade  | previously_insured     | Quantidade de clientes | Porcentagem |
| ------ | ------------------ | ---------------------- | ----------- |
| Maior de 40 anos |     0    | 95725                | 69,620207 % |
| Maior de 40 anos |     1    | 41771                | 30,379793 % |

**Menor de 40 anos**
| Idade  | previously_insured     | Quantidade de clientes | Porcentagem |
| ------ | ------------------ | ---------------------- | ----------- |
| Menor de 40 anos |     0    | 69538                | 41,542257 % |
| Menor de 40 anos |     1    | 97853                | 58,457743 % |

<p align="center"><img src="https://github.com/jhonatanmarques92/health_insurance_cross_sell/blob/main/img/h7.png" width="820" height="520"></p>

## Modelos de Machine Learning aplicados
Os 304887 clientes foram divididos em:
  - 243909 para treino
  - 60978 para teste
Utilizado 5 algoritmos para o treinamento do modelo (Logistic Regression, KNN, Random Forest, Extra Trees e XGBoost).  
Abaixo a avaliação de cada modelo treinado.  

**Logistic Regression**  
Sem cross validation

| Top % | Precision | Recall |
| ----- | --------- | ------ |
| 30 %  | 0.28      | 0.68   |
| 50 %  | 0.24      | 0.99   |
| 70 %  | 0.18      | 1.0    |

**KNN**  
Sem cross validation

| Top % | Precision | Recall |
| ----- | --------- | ------ |
| 30 %  | 0.27      | 0.67   |
| 50 %  | 0.21      | 0.83   |
| 70 %  | 0.16      | 0.9    |

**Random Forest**  
Sem cross validation

| Top % | Precision | Recall |
| ----- | --------- | ------ |
| 30 %  | 0.3      | 0.73   |
| 50 %  | 0.24      | 0.98   |
| 70 %  | 0.18      | 0.99    |

**Extra Trees**  
Sem cross validation

| Top % | Precision | Recall |
| ----- | --------- | ------ |
| 30 %  | 0.29      | 0.71   |
| 50 %  | 0.24      | 0.97   |
| 70 %  | 0.17      | 0.99    |

**XGBoost**  
Sem cross validation

| Top % | Precision | Recall |
| ----- | --------- | ------ |
| 30 %  | 0.32      | 0.77   |
| 50 %  | 0.24      | 0.99   |
| 70 %  | 0.18      | 1.0    |

- **Comparação dos modelos**
Precision e recall de cada modelo, com cross validation em 3 folds e top 30%, curva de ganho cumulativo e curva lift

** Precision e recall**  
| model_name     |          Precision        |          Recall            |
| -------------- | ------------------------- | -------------------------- |
| XGBoost        | mean: 0.32 / std: +- 0.0	 | mean: 0.78 / std: +- 0.0   |
| Random Forest  | mean: 0.3 / std: +- 0.0   | mean: 0.73 / std: +- 0.0  |
| Extra Trees    | mean: 0.29 / std: +- 0.0 | mean: 0.72 / std: +- 0.0    |
| Logistic Regression | mean: 0.28 / std: +- 0.0 | mean: 0.68 / std: +- 0.01 |
| KNN            | mean: 0.27 / std: +- 0.0  | mean: 0.67 / std: +- 0.0   |

**Curva de ganho cumulativo**
<p align="center"><img src="https://github.com/jhonatanmarques92/health_insurance_cross_sell/blob/main/img/curva_ganho.png" width="820" height="520"></p>

**Curva lift**
<p align="center"><img src="https://github.com/jhonatanmarques92/health_insurance_cross_sell/blob/main/img/lift.png" width="820" height="520"></p>

- Fine tunning do modelo XGBoost, com cross validation de 3 folds e top 30%

|                                       Parâmetros                                                         |        Precision         |             Recall       |
| ---------------------------------------------------------------------------------------------------------| ------------------------ | ------------------------ |
| n_estimators: 120, eta: 0.01, max_depth: 5, subsample: 0.5, colsample_bytree: 0.7, min_child_weight: 3   | mean: 0.32 / std: +- 0.0 | mean: 0.78 / std: +- 0.0 |
| n_estimators: 160, eta: 0.03, max_depth: 10, subsample: 0.5, colsample_bytree: 0.5, min_child_weight: 8  | mean: 0.32 / std: +- 0.0 | mean: 0.77 / std: +- 0.0 |
| n_estimators: 300, eta: 0.01, max_depth: 5, subsample: 0.5, colsample_bytree: 0.7, min_child_weight: 3   | mean: 0.32 / std: +- 0.0 | mean: 0.78 / std: +- 0.0 |

Após os treinamentos, foi utilizado como modelo final o XGBoost com os parâmetros padrão.

## Perfomance do modelo escolhido
Para responder as duas perguntas de negócio, foram utilizados os 60978 clientes dos dados de teste.  

- **Qual a porcentagem de vendas efetuadas com as 20 mil ligações?**  
  - Dos 60978 clientes, após as 20 mil ligações, o modelo ja vai ter atingido quase 82% da base contra 32,8% caso seja feito uma escolha aleatória, sendo 2,5 vezes melhor.

**Curva de ganho cumulativo**
<p align="center"><img src="https://github.com/jhonatanmarques92/health_insurance_cross_sell/blob/main/img/curva_ganho_20k.png" width="820" height="520"></p>

**Curva lift**
<p align="center"><img src="https://github.com/jhonatanmarques92/health_insurance_cross_sell/blob/main/img/lift_20k.png" width="820" height="520"></p>

- **Qual a porcentagem de vendas efetuadas caso o time de vendas consiga fazer 30 mil ligações?**
  - Dos 60978 clientes, após as 30 mil ligações, o modelo ja vai ter atingido quase 99% da base contra 49,2% caso seja feito uma escolha aleatória, sendo 2 vezes melhor.

**Curva de ganho cumulativo**
<p align="center"><img src="https://github.com/jhonatanmarques92/health_insurance_cross_sell/blob/main/img/curva_ganho_30k.png" width="820" height="520"></p>

**Curva lift**
<p align="center"><img src="https://github.com/jhonatanmarques92/health_insurance_cross_sell/blob/main/img/lift_30k.png" width="820" height="520"></p>

## Modelo em produção
O modelo foi hospedado no Heroku e criado um botão no Google Sheets, através do apps script com JavaScript, para que possa ser feito o ranqueamento.   

https://user-images.githubusercontent.com/49005736/175660666-3bae9530-8716-4123-a2c9-5b4a9aa05aa1.mp4


