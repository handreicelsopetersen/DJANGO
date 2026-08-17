from django.contrib import admin


# Register your models here.
from .models import Category, Recipe

class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

##  executa o register se voce quiser utilizar o admin do django para gerenciar a categoria, caso contrario nao precisa registrar   
admin.site.register(Category, CategoryAdmin)
