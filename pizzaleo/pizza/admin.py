from django.contrib import admin

from pizza.models import ingredient
from pizza.models import Pizza
from pizza.models import Comment

# Register your models here.

admin.site.register(ingredient)
admin.site.register(Pizza)
admin.site.register(Comment)