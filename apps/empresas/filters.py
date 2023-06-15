import django_filters
from apps.empresas.models import (TipoContribu,TamanoEmpresa)

class TipoContribuFilterSet(django_filters.FilterSet):
    class Meta:
      models = TipoContribu
      fiedls = ['codigo','tipoContri','flagTipo','flagEstado']

class TamanoEmpresasFilterSet(django_filters.FilterSet):
   class Meta:
      models = TamanoEmpresa
      fiedls = ['codigo','descripcion','fecmod','usemod','usereg','flagestado','fecreg']