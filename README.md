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
