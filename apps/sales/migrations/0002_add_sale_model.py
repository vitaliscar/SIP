from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, db_column='id')),
                ('compania', models.CharField(max_length=255, blank=True, null=True, db_column='Compa\u00f1ia')),
                ('sucursal', models.CharField(max_length=255, blank=True, null=True, db_column='Sucursal')),
                ('codigo_cliente', models.CharField(max_length=100, blank=True, null=True, db_column='Cod. Cliente')),
                ('cliente_vnq', models.CharField(max_length=255, blank=True, null=True, db_column='Cliente VNQ')),
                ('suplidor', models.CharField(max_length=255, blank=True, null=True, db_column='Suplidor')),
                ('codigo_vendedor', models.CharField(max_length=50, blank=True, null=True, db_column='Cod. Vendedor')),
                ('vendedor', models.CharField(max_length=255, blank=True, null=True, db_column='Vendedor')),
                ('numero_factura', models.CharField(max_length=50, blank=True, null=True, db_column='N\u00ba Factura')),
                ('cantidad', models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, db_column='Cantidad')),
                ('pvp_total_ext', models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, db_column='P.V.P. Total $ Extendido')),
                ('tipo_de_venta', models.CharField(max_length=255, blank=True, null=True, db_column='Tipo de Venta')),
                ('cod_vend_ov', models.CharField(max_length=50, blank=True, null=True, db_column='Cod.Vend.OV')),
                ('nombre_vendedor_ov', models.CharField(max_length=255, blank=True, null=True, db_column='Nombre Vendedor OV')),
                ('numero_pieza', models.CharField(max_length=50, blank=True, null=True, db_column='N\u00ba Pieza')),
                ('created_at', models.DateTimeField(db_column='createdAt')),
                ('fecha_factura', models.CharField(max_length=255, blank=True, null=True, db_column='Fecha Factura')),
            ],
            options={'managed': False, 'db_table': '"Sale"'},
        ),
    ]
