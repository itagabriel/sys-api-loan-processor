from django.shortcuts import render
from rest_framework import viewsets
from .models import Proposta
from .serializers import PropostaSerializer

def index(request):
    return render(
        request,
        'gestaopropostas/index.html'
    )

class PropostaViewSet(viewsets.ModelViewSet):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer