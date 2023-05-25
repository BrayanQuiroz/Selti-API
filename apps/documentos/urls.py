from django.urls import include, path

app_name = 'documentos'

urlpatterns = [
     path('api/', include('apps.documentos.urls', namespace='api-documentos')),
]
