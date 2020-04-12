from django.db import models


class JewelryType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True)
    jewelry_type = models.ForeignKey(JewelryType, on_delete=models.CASCADE)
    price = models.FloatField(blank=True, null=True)
    date_added = models.DateField(auto_now=True)
    disc = models.TextField(null=True)

