from rest_framework import serializers, viewsets
from .models import Proposta, CustomFields

class CustomFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomFields
        fields = '__all__'

class PropostaSerializer(serializers.ModelSerializer):
    campos_adicionais = CustomFieldsSerializer(many=True, read_only=True)

    class Meta:
        model = Proposta
        fields = ['id', 'nome_completo', 'cpf', 'endereco', 'valor_emprestimo', 'status', 'data_proposta', 'campos_adicionais']

    def get_campos_adicionais(self, obj):
        campos_personalizados = obj.campos_adicionais.all()
        campos_serializados = {}
        for campo in campos_personalizados:
            campos_serializados[campo.nome] = campo.valor
            print(campos_serializados)
        return campos_serializados

class PropostaViewSet(viewsets.ModelViewSet):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer