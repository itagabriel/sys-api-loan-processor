from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, criar_proposta, sucesso


app_name = 'gestaopropostas'

urlpatterns = [
    path('', index, name='index'),
    path('api/criar-proposta/', criar_proposta, name='criar_proposta'),
    path('sucesso/', sucesso, name='sucesso'),
]