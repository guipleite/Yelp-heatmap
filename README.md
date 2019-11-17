# Yelp Heatmap

- Gabriel Monteiro

- Guilherme Leite

- Hugo Carl

EntregaC.ipynb - Explicações sobre o Spark e o dataset, além de algumas demonstrações do framework

df_business_maker.ipynb - Cria uma base de dados juntando as informações já existentes com as coletadas a partir da API do Yelp.

api.py - Scrip usado para acessar a base de dados SQL

EntregaBeA.ipynb - Relaciona a base de dados SQL criada com o Spark e cria o heatmap

Jupyter Notebooks used to demonstrate how Apache Spark can be used to manipulate data, with an end goal of generating a heatmap based on the reviews of users.


## Entrega C

## Entrega B e A

- df_business_maker é o script em que foi feito requests e montado a tabela de business do banco de dados relacional.

- EntregaBeA é o script que cria as outras tabelas do campo e termina o banco de dados, além de implementar a api.py e possuir uma célula interativa que ao colocar o id do usuário, retorna o mapa de calor dos lugares frequentados por ele.


### Imagens dos mapas de calor(o notebook no git não mostra elas no final)

- Célula interativa do script

![alt text](https://github.com/guipleite/Yelp-heatmap/blob/master/imagens/interativa.png?raw=true)


- Média do lugares

![alt text](https://github.com/guipleite/Yelp-heatmap/blob/master/imagens/media.png?raw=true)

- Desvio Padrão dos lugares

![alt text](https://github.com/guipleite/Yelp-heatmap/blob/master/imagens/dp.png?raw=true)

- Banco de Dados Relacional

![alt text](https://github.com/guipleite/Yelp-heatmap/blob/master/imagens/banco.png?raw=true)


Dataset used: https://www.kaggle.com/yelp-dataset/yelp-dataset/download
