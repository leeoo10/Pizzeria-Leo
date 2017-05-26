"""pizzaleo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from pizza.api.views import IngredientViewSet
from pizza.api.views import PizzaViewSet
from pizza.api.views import CommentViewSet

swagger_view = get_swagger_view(title="Pizzería Leo")

router_api = routers.DefaultRouter()
router_api.register(r'ingredients', IngredientViewSet)
router_api.register(r'pizza', PizzaViewSet)
router_api.register(r'comment', CommentViewSet)

api_urlpatterns = [
    url(r'^', include(router_api.urls)),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(api_urlpatterns)),
    url(r'^docs/', swagger_view),
    # url(r'^pizzas/', include('pizza.urls')),
    url(r'^', include('pizza.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
