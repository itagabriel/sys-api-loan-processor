from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, PropostaViewSet

router = DefaultRouter()
router.register('propostas', PropostaViewSet)

app_name = 'gestaopropostas'

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]