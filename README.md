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
* Não foram levantados requisitos de autenticação e segurança.

## Sugestões ## 

* Foi adicionado o campo **ponderador (weigh_price)** ao produto. Esse campo visa
 ponderar o valor do produto em relação aos demais.
* Foi adicionado um histórico de preços (**PriceProduct**). Ao adicionar um novo PriceProduct
o valor do produto é atualizado automáticamente.

## Dependências ##

* Python 3.5
* [django 1.9.7](https://www.djangoproject.com/)
* [djangorestframework 3.5.3](http://www.django-rest-framework.org/)
* [django-filter 1.0.1](http://www.django-rest-framework.org/)
* [django-cors-headers 2.0.1](https://github.com/ottoyiu/django-cors-headers)

## API ##

#### Safra - /api/harvest/{id} ####
 * GET: Lista 'safras' ou retorna um objeto 'safra específico(passando o {id}).
 * POST: Cria um novo objeto do tipo 'safra' (não utilizar o {id}).
 * PUT: Atualiza o objeto 'safra' com id igual ao {id}(uso obrigatório).
 * DELETE: Remove o objeto 'safra' com id igual ao {id}(uso obrigatório).
 
 Exemplo:
 
 ```
     {
        "id": 1,
        "name": "Soja 2017",
        "start_date": "2017-02-28",
        "end_date": "2017-08-30"
    }
 ```

#### Produto - /api/product/{id} ####
 * GET: Lista 'produtos' ou retorna um objeto 'produto' específico(passando o {id}).
 * POST: Cria um novo objeto do tipo 'produto' (não utilizar o {id}).
 * PUT: Atualiza o objeto 'produto' com id igual ao {id}(uso obrigatório).
 * DELETE: Remove o objeto 'produto' com id igual ao {id}(uso obrigatório).

Exemplo:

```
    {
        "id": 1,
        "name": "Diesel",
        "last_average_price": "15.000",
        "weigh_price": "1.00"
    }
 ```

#### Serviço - /api/service/{id} ####
 * GET: Lista 'serviços' ou retornar um objeto 'serviço' específico(passando o {id}).
 * POST: Cria um novo objeto do tipo 'serviço' (não utilizar o {id}).
 * PUT: Atualiza o objeto 'serviço' com id igual ao {id}(uso obrigatório).
 * DELETE: Remove o objeto 'serviço' com id igual ao {id}(uso obrigatório).

Exemplo:

```
    {
        "id": 2,
        "name": "Colheita",
        "start_date": "2017-01-10",
        "end_date": "2017-02-01",
        "cost": "50.000",
        "harvest": 1
    }
 ```

#### Preço do Produto - /api/price-product/{id} ####
 * GET: Lista histórico de preços ou retornar um objeto específico(passando o {id}).
 * POST: Cria um novo preço para um produto (não utilizar o {id}).
 * PUT: Atualiza o objeto 'preço do produto' com id igual ao {id}(uso obrigatório).
 * DELETE: Remove o objeto 'preço do produto' com id igual ao {id}(uso obrigatório).

Exemplo:

```
    {
        "id": 2,
        "creation_date": "2017-02-04",
        "average_price": "12.000",
        "product": {
            "id": 1,
            "name": "Diesel",
            "last_average_price": "15.000",
            "weigh_price": "1.00"
        }
    }
 ```

#### Atualizar Preços dos Produtos - /api/update_products/ ####
 * POST: Atulizar valores médios dos produtos utilizados no mês anterior.


## Outros Repositórios ##

* Front-end: https://github.com/marcospereirampj/m2agro-frontend
* Script - Teste Lógica: https://github.com/marcospereirampj/m2agro-script

## Demonstração ##

* API Rest: http://m2agro.marcospereirajr.com.br/api/
* Front-end (AngularJS): http://m2agro.marcospereirajr.com.br/

## Lições Aprendidas

* Utilizar a PEP8
* 




