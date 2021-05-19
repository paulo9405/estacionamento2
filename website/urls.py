from django.conf.urls import url, include
from django.urls import path
from .views import (
    home,
    contato,
    servicos,
    planos,
    sobre
)
urlpatterns = [
    path('', home, name='website_home'),
    path('servicos', servicos, name='website_servicos'),
    path('sobre', sobre, name='website_sobre'),
    path('planos', planos, name='website_planos'),
    path('contato', contato, name='website_contato'),
]