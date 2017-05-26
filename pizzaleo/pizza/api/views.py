from rest_framework import viewsets

from pizza.api.serializers import IngredientSerializer
from pizza.api.serializers import PizzaSerializer
from pizza.api.serializers import CommentSerializer
from pizza.models import ingredient
from pizza.models import Pizza
from pizza.models import Comment

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [
        #Ejemplo de permiso para usuario logueado: IsAuthenticated
    ]

class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [
        #Ejemplo de permiso para usuario logueado: IsAuthenticated
    ]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        #Ejemplo de permiso para usuario logueado: IsAuthenticated
    ]