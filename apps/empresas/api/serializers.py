from rest_framework import serializers
from apps.empresas.models import TipoContribu,TamanoEmpresa 

class TipoContribuSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContribu
        fields = ['codigo','tipoContri','flagTipo','flagEstado']

class TamanoEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TamanoEmpresa
        fields = ['codigo','descripcion','fecmod','usemod','usereg','flagestado','fecreg']

            

  
