from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Product Categories'


class Ingredient(models.Model):
    name = models.CharField(max_length=100, blank=False)
    products = models.ManyToManyField('Product', through='ProductsIngredient')

    def __unicode__(self):
        return self.name


class Product(models.Model):
    ingredients = models.ManyToManyField(Ingredient, through='ProductsIngredient')
    name = models.CharField(max_length=100, blank=False)
    price = models.IntegerField(blank=False, default=0)
    category = models.ForeignKey(ProductCategory)

    def __unicode__(self):
        return self.name


class ProductsIngredient(models.Model):
    product = models.ForeignKey(Product)
    ingredient = models.ForeignKey(Ingredient)

    class Meta:
        verbose_name = 'Product\'s Ingredient'
        verbose_name_plural = 'Product Ingredients'
        unique_together = ['product', 'ingredient']