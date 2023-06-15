from django.db import models

class TipoContribu(models.Model):
    codigo = models.CharField(db_column='V_CODTIPCON', primary_key=True, max_length=2)
    tipoContri = models.CharField(db_column='V_DESTIPCON', max_length=250)
    flagTipo = models.CharField(db_column='V_FLGTIPO', max_length=1)
    flagEstado = models.CharField(db_column='V_FLGESTADO', max_length=1)

    class Meta:
        managed = False
        db_table = 'SIMINTRA1"."SITB_TIPOCONTRIBU'
        verbose_name_plural = 'Tipo de Contribuyente'

class TamanoEmpresa(models.Model):
    codigo = models.IntegerField(db_column='N_CODTAMEMP', primary_key=True)
    descripcion = models.CharField(db_column='V_DESCRIPCION', max_length=20)
    fecmod = models.DateField(db_column='D_FECMOD')
    usemod = models.CharField(db_column='V_USEMOD', max_length=50)
    usereg = models.CharField(db_column='V_USEREG', max_length=50)
    flagestado = models.IntegerField(db_column='N_FLAGESTADO')
    fecreg = models.DateField(db_column='D_FECREG')

    class Meta:
        db_table = 'RESLTISYS"."RESLTITBC_TAMEMPRESA'
        verbose_name_plural = 'Tamaño de contribuyente'
