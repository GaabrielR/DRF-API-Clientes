from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF digitado deve ser válido."})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"O nome deve conter apenas letras."})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG digitado deve ter 9 dígitos."})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O celular deve seguir o padrão: (XX) 91234-1234."})
        return data
    