from django.urls import path
from gestaopropostas.views import index

app_name = 'gestaopropostas'

urlpatterns = [
    path('', index, name='index' ),
]