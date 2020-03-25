# Django-api-internship-test-
Repositório para criação de um API Rest.

Trello: https://trello.com/b/VxClBfCv/api-django-rest-framework

urls(endpoints):
# products ( Produtos )
products                          # GET - Lista todos os produtos
products/<int:id>                 # GET - PATCH - DELETE - De um produto especifico (os verbos [PATCH, DELETE] precisam de autenticação)
# Orders ( Pedidos )              # Todos os endpoints em Orders precisam de autenticação
orders                            # GET - POST - Lista todos os pedidos do usuário / Cria um pedido
orders/<int:id>                   # GET - PATCH - DELETE - Pega, atualiza ou deleta um pedido em especifico
orders/<int:id>/pay               # POST - Paga o pedido: "paid" = True
# Account ( Login e registro )    
account/registration              # POST - Registra o usuário
account/login                     # POST - Faz login de um usuário e recupera seu Token

# Autenticação
Para usar a autenticação no postman:
Em header's, use a Key: Authorization, e em Value use: Token "hash do token".
Exemplo:

Key: Authorization
Value: Token 54c71d7f9a204b317c63a8395db54ed9de019ac0

# Acesso Heroku
https://djangointernship.herokuapp.com/products
https://djangointernship.herokuapp.com/products/1     # id = 1, apenas de exemplo
https://djangointernship.herokuapp.com/orders
https://djangointernship.herokuapp.com/orders/1
https://djangointernship.herokuapp.com/orders/1/pay 
https://djangointernship.herokuapp.com/account/registration
https://djangointernship.herokuapp.com/account/login

