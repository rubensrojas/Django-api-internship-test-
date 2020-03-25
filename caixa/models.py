from django.db import models

# Create your models here.

# Produtos
class Product(models.Model):
    name        = models.CharField(max_length = 100)
    description = models.CharField(max_length = 256)
    price       = models.FloatField()
    stock       = models.IntegerField(default = 0)
    created_at  = models.DateTimeField(auto_now_add=True) # Data de criação na database

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products_table' # Tabela no banco de dados
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

"""
# Usuários
class User(models.Model):
    username   = models.CharField (max_length = 30, unique = True)
    password   = models.CharField (max_length = 30)
    email      = models.EmailField(max_length = 254, unique = True)
    first_name = models.CharField (max_length = 30)
    last_name  = models.CharField (max_length = 100)
    address    = models.CharField (max_length = 254)
    create_at  = models.DateField (auto_now_add=True)
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users_table' # Tabela no banco de dados
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'


# Pedidos
class Order(models.Model):
    product     = models.ForeignKey(Product, on_delete = models.CASCADE) # Product
    owner       = models.ForeignKey(User, on_delete = models.CASCADE)    # User
    quantity    = models.IntegerField(default = 0)
    total_price = models.FloatField(default = 0)
    paid        = models.BooleanField(default = False)
    #create_at?

    def __str__(self):
        return self.owner + '_' + self.product

    class Meta:
        db_table = 'orders_table' # Tabela no banco de dados
        managed = True
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
"""




