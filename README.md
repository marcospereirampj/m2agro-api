API m2agro - Documentação
=========================

API Rest para a plataforma de planejamento agrícola [m2agro](http://www.m2agro.com.br/) desenvolvida 
como parte do desafio técnico para vaga de Desenvolvedor foda Python/Django.


## Requisitos ##

* Safra deve ter nome, data de início e fim.
* Produtos são itens utilizados em um serviço que é executado em uma safra.
* Produto deve conter nome e preço médio.
* Serviço precisa de ter nome, datas de ínicio e fim, safra onde será executado e produtos
que serão utilizados, assim com suas respectivas quantidades.
* Mensalmente deve ser calculado o preço médio de cada produto. Para isso, deve ser 
levado em consideração os valores dos serviços e as quantidades utilizadas de cada produto.
* Os sistema deve permitir a integração com sistemas externos.

## Dependências ##


* [django 1.9.7](https://www.djangoproject.com/)
* [djangorestframework 3.5.3](http://www.django-rest-framework.org/)
* [django-filter 1.0.1](http://www.django-rest-framework.org/)

## Demonstração ##

* API Rest: http://m2agro.marcospereirajr.com.br/api/
* Front-end (AngularJS): http://m2agro.marcospereirajr.com.br/




