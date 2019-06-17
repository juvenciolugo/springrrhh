# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-04-28 14:41
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(choices=[('Banco_Nacional_de_Mexico_Banamex', 'Banco Nacional de México Banamex'), ('Banco_Santander_Mexico', 'Banco Santander México'), ('HSBC_Mexico', 'HSBC México'), ('Scotiabank_Inverlat', 'Scotiabank Inverlat'), ('BBVA_Bancomer', 'BBVA Bancomer'), ('Banco_Mercantil_del_Norte_Banorte', 'Banco Mercantil del Norte Banorte'), ('Banco_Interacciones', 'Banco Interacciones'), ('Banco_Inbursa', 'Banco Inbursa'), ('banca_Mifel', 'banca Mifel'), ('Banco_Regional_de_Monterrey', 'Banco Regional de Monterrey'), ('Banco_Invex', 'Banco Invex'), ('Banco_del_Bajio', 'Banco del Bajio'), ('Bansi', 'Bansi'), ('Banca_Afirme', 'Banca Afirme'), ('Bank_of_America_Mexico', 'Bank of America México'), ('Banco_JP_Morgan', 'Banco JP Morgan'), ('Banco_Ve_Por_Mas', 'Banco Ve Por Mas'), ('American_Express_Bank_Mexico', 'American Express Bank México'), ('Investa_Bank', 'Investa Bank'), ('CiBanco', 'CiBanco'), ('Bank_of_TokyoMitsubishi_UFJ_Mexico', 'Bank of TokyoMitsubishi UFJ México'), ('Banco_Monex', 'Banco Monex'), ('Deutsche_Bank_Mexico', 'Deutsche Bank México'), ('Banco_Azteca', 'Banco Azteca'), ('Banco_Credit_Suisse_Mexico', 'Banco Credit Suisse México'), ('Banco_Autofin_Mexico', 'Banco Autofin México'), ('Barclays_Bank_Mexico', 'Barclays Bank México'), ('Banco_Ahorro_Famsa', 'Banco Ahorro Famsa'), ('Intercam_Banco', 'Intercam Banco'), ('ABC_Capital', 'ABC Capital'), ('Banco_Actinver', 'Banco Actinver'), ('Banco_Compartamos', 'Banco Compartamos'), ('Banco_Multiva', 'Banco Multiva'), ('UBS_Bank_Mexico', 'UBS Bank México'), ('Bancoppel', 'Bancoppel'), ('ConsuBanco', 'ConsuBanco'), ('Banco_WalMart_de_Mexico', 'Banco WalMart de México'), ('Volkswagen_Bank', 'Volkswagen Bank'), ('Banco_Base', 'Banco Base'), ('Banco_Pagatodo', 'Banco Pagatodo'), ('Banco_Forjadores', 'Banco Forjadores'), ('Bankaool', 'Bankaool'), ('Banco_Inmobiliario_Mexicano', 'Banco Inmobiliario Mexicano'), ('Fundación_Donde_Banco', 'Fundación Donde Banco'), ('Banco_Bancrea', 'Banco Bancrea')], default='Banco_Nacional_de_Mexico_Banamex', max_length=60, verbose_name='Entidad bancaria')),
                ('contrato', models.FileField(upload_to='bancos/', verbose_name='Cabecera de contrato bancario')),
                ('clabe', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999999999999999)], verbose_name='Clabe')),
            ],
        ),
        migrations.CreateModel(
            name='Capacitaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_curso', models.CharField(choices=[('Curso', 'Curso'), ('Diplomado', 'Diplomado'), ('Taller', 'Taller')], default='Curso', max_length=60, verbose_name='Tipo de curso')),
                ('nombre_curso', models.CharField(max_length=100, verbose_name='Título o descripción')),
                ('certificado', models.FileField(blank=True, null=True, upload_to='certificados/', verbose_name='Certificado / Constancia')),
            ],
        ),
        migrations.CreateModel(
            name='Conyugue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acta', models.ImageField(upload_to='acta_matrimonio/', verbose_name='Acta de Matrimonio / Unión Libre')),
                ('acta_nacimiento', models.ImageField(default='', upload_to='acta_nacimiento/', verbose_name='Acta de Nacimiento / Conyuge')),
                ('nombre', models.CharField(max_length=600, verbose_name='Nombre del conyugue')),
                ('apellido_paterno', models.CharField(max_length=600, verbose_name='Apellido paterno del conyugue')),
                ('apellido_materno', models.CharField(max_length=600, verbose_name='Apellido materno del conyugue')),
                ('fecha_nacimiento', models.DateTimeField(verbose_name='Fecha de nacimiento del conyugue')),
                ('profesion', models.CharField(max_length=600)),
                ('tlf', models.CharField(max_length=255, verbose_name='Tel')),
                ('email', models.CharField(max_length=600)),
                ('email_trabajo', models.CharField(blank=True, max_length=600, null=True)),
                ('lugar_de_trabajo', models.CharField(blank=True, max_length=600, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=600, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_comprobante', models.CharField(choices=[('Agua', 'Agua'), ('Cable', 'Cable'), ('Teléfono', 'Teléfono'), ('Gas', 'Gas'), ('Electricidad', 'Electricidad')], default='Agua', max_length=60, verbose_name='Tipo de comprobante de domicilio')),
                ('comprobante_domicilio', models.FileField(upload_to='comprobantes_domicilio/', verbose_name='Comprobante de domicilio')),
                ('tlf_residencial', models.CharField(max_length=255, verbose_name='Teléfono residencial')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nombre', models.CharField(max_length=600)),
                ('apellido_paterno', models.CharField(max_length=600)),
                ('apellido_materno', models.CharField(max_length=600)),
                ('fecha_nacimiento', models.DateTimeField(verbose_name='fecha de nacimiento')),
                ('tipo', models.CharField(default='xx', max_length=600)),
                ('calle', models.CharField(default='xx', max_length=600)),
                ('num_ext', models.CharField(default=1, max_length=600)),
                ('num_int', models.CharField(blank=True, max_length=600, null=True)),
                ('calle_uno', models.CharField(default='xx', max_length=600)),
                ('calle_dos', models.CharField(default='xx', max_length=600)),
                ('piso', models.CharField(blank=True, max_length=6, null=True)),
                ('depto', models.CharField(blank=True, max_length=6, null=True)),
                ('cp', models.IntegerField(default=0)),
                ('colonia', models.CharField(default='xx', max_length=600)),
                ('esdo', models.CharField(default='VERACRUZ', max_length=600)),
                ('referencia', models.TextField(blank=True, max_length=600, null=True)),
                ('tel', models.CharField(max_length=255)),
                ('cel', models.CharField(max_length=255)),
                ('email_personal', models.CharField(max_length=600)),
                ('edad', models.IntegerField()),
                ('foto', models.ImageField(upload_to='profiles/')),
                ('acta_nacimiento', models.ImageField(upload_to='actas_nacimiento/')),
                ('docu_ident_front', models.ImageField(upload_to='documentos_identidad/')),
                ('docu_ident_back', models.ImageField(blank=True, upload_to='documentos_identidad/')),
                ('pasaporte', models.BigIntegerField(blank=True, null=True)),
                ('pasaporte_valido', models.DateTimeField(blank=True, null=True, verbose_name='fecha de vencimiento')),
                ('imagen_pasaporte', models.ImageField(blank=True, null=True, upload_to='pasaportes/')),
                ('status', models.IntegerField(default=1)),
                ('curp', models.CharField(blank=True, max_length=600, null=True)),
                ('imagen_curp', models.ImageField(blank=True, null=True, upload_to='curps/')),
                ('rfc', models.CharField(blank=True, max_length=600, null=True)),
                ('imagen_rfc', models.ImageField(blank=True, null=True, upload_to='rfcs/')),
                ('sat', models.CharField(blank=True, max_length=600, null=True)),
                ('imagen_sat', models.ImageField(blank=True, upload_to='sats/')),
                ('infonavit', models.CharField(blank=True, max_length=600, null=True)),
                ('imagen_infonavit', models.ImageField(blank=True, null=True, upload_to='infonavits/')),
                ('imss', models.IntegerField(blank=True, null=True)),
                ('imagen_imss', models.ImageField(blank=True, null=True, upload_to='imss/')),
                ('estado_civil', models.CharField(blank=True, max_length=600, null=True)),
                ('numero_hijos', models.IntegerField(default=0)),
                ('pais_direc', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pais_de_direccion', to='empleados.Country')),
                ('pais_nacimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pais_nacimiento_de', to='empleados.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_estudios', models.CharField(choices=[('Secundaria Completa', 'Secundaria Completa'), ('Secundaria Trunca', 'Secundaria Trunca'), ('Educación Media Terminada', 'Educación Media Terminada'), ('Educación Superior Terminada', 'Educación Superior Terminada'), ('Profesional Titulado', 'Profesional Titulado'), ('Profesional con Maestría', 'Profesional con Maestría'), ('Profesional con Doctorado', 'Profesional con Doctorado'), ('Educación Media en curso', 'Educación Media en curso'), ('Educación Superior en curso', 'Educación Superior en curso')], default='Profesional Titulado', max_length=60, verbose_name='Nivel de estudios máximo')),
                ('universidad', models.CharField(blank=True, max_length=100, null=True, verbose_name='Universidad de donde es (o será) títulado')),
                ('titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Título universitario obtenido o a obtener')),
                ('carrera', models.CharField(blank=True, max_length=100, null=True, verbose_name='Carrera o profesión')),
                ('cedula_profesional_cedula', models.IntegerField(blank=True, null=True, verbose_name='Número de cédula profesional')),
                ('cedula_profesional_imagen_cedula_profesional', models.ImageField(blank=True, null=True, upload_to='cedulas_profesionales/', verbose_name='Cédula profesional')),
                ('constacia_de_estudio', models.ImageField(blank=True, null=True, upload_to='cedulas_profesionales/', verbose_name='Constancia de estudio o diploma universitario')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_de_nivel_estudios', to='empleados.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Hijo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=600, verbose_name='Nombre')),
                ('apellido_paterno', models.CharField(max_length=600, verbose_name='Apellido paterno')),
                ('apellido_materno', models.CharField(max_length=600, verbose_name='Apellido materno')),
                ('fecha_nacimiento', models.DateTimeField(verbose_name='Fecha de nacimiento')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_de_hijos', to='empleados.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(max_length=60, verbose_name='Idioma')),
                ('nivel_escrito', models.CharField(choices=[('Nivel Bajo', 'Nivel Bajo'), ('Nivel Medio', 'Nivel Medio'), ('Nivel Alto', 'Nivel Alto'), ('Nivel Bilingüe', 'Nivel Bilingüe')], default='Nivel Bajo', max_length=60, verbose_name='Nivel Escrito')),
                ('nivel_hablado', models.CharField(choices=[('Nivel Bajo', 'Nivel Bajo'), ('Nivel Medio', 'Nivel Medio'), ('Nivel Alto', 'Nivel Alto'), ('Nivel Bilingüe', 'Nivel Bilingüe')], default='Nivel Bajo', max_length=60, verbose_name='Nivel Hablado')),
                ('conversacion', models.CharField(choices=[('No', 'No'), ('Si', 'Si')], default='No', max_length=60, verbose_name='Entablar conversación')),
                ('info_tecnica', models.CharField(choices=[('No', 'No'), ('Si', 'Si')], default='No', max_length=60, verbose_name='Leer información técnica')),
                ('redactar', models.CharField(choices=[('No', 'No'), ('Si', 'Si')], default='No', max_length=60, verbose_name='Puede redactar')),
                ('leer', models.CharField(choices=[('No', 'No'), ('Si', 'Si')], default='No', max_length=60, verbose_name='Puede leer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_de_idioma', to='empleados.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='LicenciasConducir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_vigencia', models.DateTimeField(verbose_name='fecha de termino de vigencia')),
                ('imagen_lic_anverso', models.ImageField(upload_to='licencias_conducir/')),
                ('imagen_lic_reverso', models.ImageField(upload_to='licencias_conducir/')),
                ('permanente', models.BooleanField(default=False)),
                ('estado_emision', models.CharField(max_length=600)),
                ('licencia', models.CharField(max_length=600, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_de_licencia', to='empleados.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nacionalidad_de', to='empleados.Country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_de', to='empleados.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extranjero', models.BooleanField(default=False, verbose_name='¿Es Extranjero?')),
                ('fecha_llegada', models.DateTimeField(verbose_name='Fecha de llegada al país')),
                ('permiso_trabajo', models.BooleanField(default=False, verbose_name='¿Tiene permiso de trabajo?')),
                ('solicitud_permiso_trabajo', models.BooleanField(default=False, verbose_name='¿Ya ha solicitado el permiso de trabajo?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_de_preguntas', to='empleados.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Recomendaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carta_recomendacion', models.FileField(blank=True, null=True, upload_to='cartas_recomendacion/', verbose_name='Carta de recomendación')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_de_recomendaciones', to='empleados.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumentoIdentidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(max_length=600, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='visas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_vigencia', models.DateTimeField(verbose_name='Fecha de termino de vigencia')),
                ('imagen_visa', models.ImageField(upload_to='visas/')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nacionalidad_de_visas', to='empleados.Country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_de_visas', to='empleados.Empleado')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='tipo_documento_identidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_docu_ident', to='empleados.TipoDocumentoIdentidad'),
        ),
        migrations.AddField(
            model_name='domicilio',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_de_domicilio', to='empleados.Empleado'),
        ),
        migrations.AddField(
            model_name='conyugue',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_de_conyugue', to='empleados.Empleado'),
        ),
        migrations.AddField(
            model_name='capacitaciones',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_de_curso', to='empleados.Empleado'),
        ),
        migrations.AddField(
            model_name='banco',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_de_banco', to='empleados.Empleado'),
        ),
    ]
