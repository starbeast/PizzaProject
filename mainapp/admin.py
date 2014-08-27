from django.contrib import admin
from mainapp.models import Product, Ingredient, ProductCategory


class IngredientInline(admin.StackedInline):
    model = Product.ingredients.through
    filter_horizontal = ('ingredients', )
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name',)
    # inlines = [IngredientInline, ]
    list_filter = ('ingredients', )
    filter_horizontal = ('ingredients', )


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name',)
    list_filter = ('products', )
    filter_horizontal = ('products', )


class ProductCategoryAdmin(admin.ModelAdmin):
    model = ProductCategory
    list_display = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)