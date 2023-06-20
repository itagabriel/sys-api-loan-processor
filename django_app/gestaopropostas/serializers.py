from rest_framework import serializers, viewsets
from .models import Proposta, CustomFields

class CustomFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomFields
        fields = '__all__'

class PropostaSerializer(serializers.ModelSerializer):
    campos_adicionais = CustomFieldsSerializer(many=True)

    class Meta:
        model = Proposta
        fields = ['id', 'nome_completo', 'cpf', 'endereco', 'valor_emprestimo', 'status', 'data_proposta', 'campos_adicionais']

class PropostaViewSet(viewsets.ModelViewSet):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer