# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-29 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0039_auto_20190523_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='afianzado',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='¿Ha sido afianzado?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='afianzado_monto',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Monto afianzado'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='afiliado_sindicato',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='¿Esta afiliado a algún sindicato?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='auto_marca',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Marca del automóvil'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='auto_modelo',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Modelo del automóvil'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='auto_propio',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='¿Cuenta con automóvil?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='bebe',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='¿Tiene bebe?(de 0 a 3 años)'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='carrera',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre de carrera'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='conocido_depto',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Departamento donde labora'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='conocido_nombre',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Nombre del familiar o conocido'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='conyuge_apellido_materno',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Apellido materno del conyuge'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='conyuge_apellido_paterno',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Apellido paterno del conyuge'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='conyuge_domicilio',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Domicilio del conyuge'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='conyuge_lugar_trabajo',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Lugar de trabajo del conyuge'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='conyuge_nombre',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Nombre del conyuge'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='conyuge_ocupacion',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Ocupación del conyuge'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='conyuge_tel',
            field=models.CharField(blank=True, max_length=16, verbose_name='Teléfono o celular del conyuge'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='credito_infonavit',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='¿Tiene crédito infonavit?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='disposicion_rolar',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='¿Dispuesto a rolar turnos?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='disposicion_viajar',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='¿Dispuesto a viajar?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='embarazo',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='¿Está embarazada?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='especialidad',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Especialidad'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='especialidad_documento',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Documento recibido'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='especialidad_inicio',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='especialidad_nombre',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre de la especialidad'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='especialidad_termino',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Fecha de término'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='estado_salud',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Estado de salud'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='estudia_actualmente',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='¿Estudia actualmente?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='estudia_donde',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='¿Dónde estudia?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='estudia_horario',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Horario'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='estudia_que',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='¿Qué estudia?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='estudia_termino',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de término'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='fecha_disponible',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha disponible para iniciar'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='forma',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Forma de titulación'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='fuma',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='¿Fuma?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='ingreso_extra',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='¿Tiene otros ingresos?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='ingreso_fuente',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Fuente del ingreso extra'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='ingreso_monto',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Monto del ingreso extra'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='labora_conocido',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='¿Labora un familiar o conocido con nosotros?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='madre_apellido_materno',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Apellido materno de la madre'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='madre_apellido_paterno',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Apellido paterno de la madre'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='madre_domicilio',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Domicilio de la madre'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='madre_lugar_trabajo',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Lugar de trabajo de la madre'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='madre_nombre',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Nombre de la madre'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='madre_ocupacion',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Ocupación de la madre'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='madre_tel',
            field=models.CharField(blank=True, max_length=16, verbose_name='Teléfono o celular de la madre'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='maquinas_equipos',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Maquinas o equipos que maneja'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='padre_apellido_materno',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Apellido materno del padre'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='padre_apellido_paterno',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Apellido paterno del padre'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='padre_domicilio',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Domicilio del padre'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='padre_lugar_trabajo',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Lugar de trabajo del padre'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='padre_nombre',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Nombre del padre'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='padre_ocupacion',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Ocupación del padre'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='padre_tel',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Teléfono o celular del padre'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='pago_infonavit',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Pago mensual de infonavit'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='perforaciones',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='¿Tiene perforaciones?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='postgrado',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Postgrado'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='postgrado_documento',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Documento recibido'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='postgrado_inicio',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='postgrado_nombre',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre del postgrado'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='postgrado_termino',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Fecha de término'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='preparatoria',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Preparatoria'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='preparatoria_documento',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Documento recibido'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='preparatoria_inicio',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='preparatoria_termino',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Fecha de término'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='primaria',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Primaria'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='primaria_documento',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Documento recibido'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='primaria_inicio',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='primaria_termino',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Fecha de término'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='profesional',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Profesional'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='profesional_documento',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Documento recibido'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='profesional_inicio',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='profesional_termino',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Fecha de término'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='religion',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Religión'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='secundaria',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Secundaria'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='secundaria_documento',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Documento recibido'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='secundaria_inicio',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='secundaria_termino',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Fecha de término'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='seguro_monto',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Monto del seguro de vida'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='seguro_vida',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='¿Cuenta con seguro de vida?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='sindicato_cargo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Cargo en el sindicato'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='sindicato_nombre',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre del sindicato'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='tatuajes',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='¿Tiene tatuajes?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='tecnica',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Técnica'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='tecnica_documento',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Documento recibido'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='tecnica_inicio',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='tecnica_termino',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Fecha de término'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='tiempo_libre',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='¿A qué dedica su tiempo libre?'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='vivienda_propia',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Vive en casa'),
        ),
    ]
