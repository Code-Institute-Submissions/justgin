from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    normal_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_normal_name(self):
        return self.normal_name


class Product(models.Model):
    name = models.CharField(max_length=254)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    gin_desc = models.TextField()
    alc_level = models.DecimalField(max_digits=6, decimal_places=2)
    alc_vol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
