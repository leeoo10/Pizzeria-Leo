from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class ingredient(models.Model):
    name = models.CharField(verbose_name=_("Nombre"),max_length=100)
    price = models.DecimalField(verbose_name=_("Precio"),max_digits=6,decimal_places=2)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(verbose_name=_("Nombre"),max_length=100)
    ingredients = models.ManyToManyField('pizza.ingredient',verbose_name=_("Ingredientes"),related_name='pizza')
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(0)])
    pizza = models.ForeignKey('pizza.Pizza',related_name='comments',null=True)

    def __str__(self):
        return self.text
