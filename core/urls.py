from django.urls import path
from apps.apidocumento.views import DataAPI
from apps.documentos.api.views import TipoDocumentoList
from apps.empresas.api.views import TipoContribuyenteList,TamanoEmpresaList

urlpatterns = [
    path('apidocumento/<str:tipo_documento>/<str:numero_documento>/',DataAPI.api_documentos, name='api_documentos'),
    path('apisunat/<str:nruc>/',DataAPI.api_sunat, name='api_sunat'),
    path('apitipodocumento/',TipoDocumentoList.as_view(), name='apitipodocumento'),
    path('apitipocontribuyente/',TipoContribuyenteList.as_view(), name='apitipocontribuyente'),
    path('apitamanoempresa/',TamanoEmpresaList.as_view(), name='apitamanoempresa'),

]
