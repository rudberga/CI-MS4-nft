from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Pieces(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    creator = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    year = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    path = models.URLField(max_length=1024, null=True, blank=True)
    cid = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
