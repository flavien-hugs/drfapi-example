# shop.models

from django.db import models


class ModelMixin(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(ModelMixin):

    def __str__(self):
        return self.name


class Product(ModelMixin):

    category = models.ForeignKey(
        'shop.Category', on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return self.name


class Article(ModelMixin):

    product = models.ForeignKey(
        'shop.Product', on_delete=models.CASCADE,
        related_name='articles'
    )
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name
