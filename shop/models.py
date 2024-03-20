from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(null=True)



    def __str__(self):
        return f'{self.name},{self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Client(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    items = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='clients')
    date_purchase = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Purchase(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='purchases')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='purchases')