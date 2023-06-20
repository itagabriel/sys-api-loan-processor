from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, criar_proposta, sucesso


app_name = 'gestaopropostas'

urlpatterns = [
    path('', index, name='index'),
    path('api/criar-proposta/', criar_proposta, name='criar_proposta'),
    path('sucesso/', sucesso, name='sucesso'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )