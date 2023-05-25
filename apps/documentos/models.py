from django.db import models

# Create your models here.

class TipoDocumentos(models.Model):
    codigo = models.CharField(db_column='V_CODTDOCIDE', primary_key=True, max_length=2, null=True, blank=True, verbose_name='Código')
    descripcion = models.CharField(db_column='V_DESTDOCIDE', max_length=200, null=True, blank=True, verbose_name='Descripción')
    abreviatura = models.CharField(db_column='V_DESABR', max_length=3, null=True, blank=True, verbose_name='Abreviatura')
    flag = models.IntegerField(db_column='N_FLGESTDOC', null=True, blank=True, verbose_name='Flag')

    class Meta:
        managed = False
        db_table = 'SIMINTRA1"."SITB_TDOCIDE'
        verbose_name_plural = 'Tipo de Documentos'
