from django.db import models
from users.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images')


    def __str__(self):
        return self.name

    def __str__(self):
        return f'Книга: {self.name}'


class Basket(models.Model):
    user = models.ForeignKey(to = User, on_delete=models.CASCADE)
    product = models.ForeignKey(to= Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    creared_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} |Книга: {self.product.name}'


    def sum(self):
        return self.product.price * self.quantity
