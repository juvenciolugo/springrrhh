#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from .opciones import *
from composite_field import CompositeField
from os.path import splitext, basename
from django.core.validators import MaxValueValidator 

class CedulaProfesional(CompositeField):
    cedula = models.IntegerField('Número de cédula profesional', blank=True, null=True)
    imagen_cedula_profesional = models.ImageField('Cédula profesional',upload_to='cedulas_profesionales/', blank=True, null=True)

class Country(models.Model):
    pais = models.CharField(max_length=600, unique=True)

    def __str__(self):
        return str(self.pais)

class TipoDocumentoIdentidad(models.Model):
    tipo_documento = models.CharField(max_length=600, unique=True)

    def __str__(self):
        return str(self.tipo_documento)

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=600)
    apellido_paterno = models.CharField(max_length=600)
    apellido_materno = models.CharField(max_length=600)
    pais_nacimiento = models.ForeignKey(Country, related_name="pais_nacimiento_de")
    fecha_nacimiento = models.DateTimeField('fecha de nacimiento', auto_now_add = False)
    #direccion = models.CharField(max_length=600)
    tipo = models.CharField(max_length=600, default="xx")
    calle = models.CharField(max_length=600, default="xx")
    num_ext = models.CharField(max_length=600, default=1)
    num_int = models.CharField(max_length=600,null =True,blank=True)
    calle_uno = models.CharField(max_length=600, default="xx")
    calle_dos = models.CharField(max_length=600, default="xx")
    piso =models.CharField(max_length=6, null=True, blank=True)
    depto =models.CharField(max_length=6, null=True, blank=True)
    cp = models.IntegerField(blank = False, default=0)
    colonia = models.CharField(max_length=600, default="xx")
    esdo = models.CharField(max_length=600, default="VERACRUZ")
    pais_direc = models.ForeignKey(Country, related_name="pais_de_direccion", default=1)
    referencia = models.TextField(max_length=600, blank = True, null = True)
    tel = models.CharField(max_length=255)
    cel = models.CharField(max_length=255)
    email_personal = models.CharField(max_length=600)
    edad = models.IntegerField(blank = False)
    foto = models.ImageField(upload_to = 'profiles/')
    acta_nacimiento = models.ImageField(upload_to = 'actas_nacimiento/')
    tipo_documento_identidad = models.ForeignKey(TipoDocumentoIdentidad, related_name="tipo_docu_ident")
    docu_ident_front = models.ImageField(upload_to = 'documentos_identidad/')
    docu_ident_back = models.ImageField(upload_to = 'documentos_identidad/', blank = True)
    pasaporte = models.BigIntegerField(blank = True,null = True)
    pasaporte_valido = models.DateTimeField('fecha de vencimiento', auto_now_add = False, blank = True,null = True)
    imagen_pasaporte = models.ImageField(upload_to = 'pasaportes/', blank = True, null = True)
    status = models.IntegerField(blank = False, default=1)
    
    activo= models.CharField(max_length=2,default='SI', blank = True, null = True)
    fecha_baja = models.DateTimeField('Fecha de baja', auto_now_add = True, blank = True, null = True)
    motivo = models.TextField('Motivo',max_length=200, blank = True, null = True)
    tipo_baja = models.CharField('Tipo de baja',max_length=8, blank = True, null = True)


    # ETAPA 2
    curp = models.CharField(max_length=600, blank = True, null = True)
    imagen_curp = models.ImageField(upload_to = 'curps/', blank = True, null = True)
    rfc = models.CharField(max_length=600, blank = True, null = True)
    imagen_rfc = models.ImageField(upload_to = 'rfcs/', blank = True, null = True)
    sat = models.CharField(max_length=600, blank = True, null = True)
    imagen_sat = models.ImageField(upload_to = 'sats/', blank = True)
    infonavit = models.CharField(max_length=600, blank = True, null = True)
    imagen_infonavit = models.ImageField(upload_to = 'infonavits/', blank = True, null = True)
    imss = models.IntegerField(blank = True, null = True)
    imagen_imss = models.ImageField(upload_to = 'imss/', blank = True, null = True)
    # ETAPA 3
    estado_civil = models.CharField(max_length=600, blank = True, null = True)
    # ESTAPA 4
    numero_hijos = models.IntegerField(blank = False, default=0)

    def __str__(self):
        return str ((self.user.first_name)+" "+(self.user.last_name))

class Nacionalidad(models.Model):
    user = models.ForeignKey(Empleado, related_name="user_de")
    pais = models.ForeignKey(Country, related_name="nacionalidad_de")

    def __str__(self):
        return str ((self.user.user.first_name)+" "+(self.user.user.last_name)+" "+(self.pais.pais))

class visas(models.Model):
    user = models.ForeignKey(Empleado, related_name="user_de_visas")
    pais = models.ForeignKey(Country, related_name="nacionalidad_de_visas")
    fecha_vigencia = models.DateTimeField('Fecha de termino de vigencia', auto_now_add = False)
    imagen_visa = models.ImageField(upload_to = 'visas/')

    def __str__(self):
        return str ((self.user.user.first_name)+" "+(self.user.user.last_name)+" "+(self.pais.pais))

class LicenciasConducir(models.Model):
    user = models.ForeignKey(Empleado, related_name="user_de_licencia")
    fecha_vigencia = models.DateTimeField('Fecha de termino de vigencia', auto_now_add = False)
    imagen_lic_anverso = models.ImageField(upload_to = 'licencias_conducir/')
    imagen_lic_reverso = models.ImageField(upload_to = 'licencias_conducir/')
    permanente = models.BooleanField(default=False)
    estado_emision = models.CharField(max_length=600)
    licencia = models.CharField(max_length=600, unique=True)

    def __str__(self):
        return str ((self.user.user.first_name)+" "+(self.user.user.last_name))

class Conyugue(models.Model):
    user = models.ForeignKey(Empleado, related_name="user_de_conyugue")
    acta = models.ImageField('Acta de Matrimonio / Unión Libre',upload_to = 'acta_matrimonio/')
    acta_nacimiento = models.ImageField('Acta de Nacimiento / Conyuge',upload_to = 'acta_nacimiento/',default="")
    nombre = models.CharField('Nombre del conyugue', max_length=60)
    apellido_paterno = models.CharField('Apellido paterno del conyugue', max_length=60)
    apellido_materno = models.CharField('Apellido materno del conyugue', max_length=60)
    fecha_nacimiento = models.DateTimeField('Fecha de nacimiento del conyugue', auto_now_add = False)
    profesion = models.CharField(max_length=60)
    tlf = models.CharField('Tel',max_length=15)
    email = models.CharField(max_length=60)
    email_trabajo = models.CharField(max_length=60, blank = True, null = True)
    lugar_de_trabajo = models.CharField(max_length=200, blank = True, null = True)

    def __str__(self):
        return str ((self.nombre)+" "+(self.apellido_paterno)+" "+(self.apellido_materno))

class Preguntas(models.Model):
    user = models.ForeignKey(Empleado, related_name="user_de_preguntas")
    extranjero = models.BooleanField('¿Es Extranjero?',default=False)
    fecha_llegada = models.DateTimeField('Fecha de llegada al país', auto_now_add = False)
    permiso_trabajo = models.BooleanField('¿Tiene permiso de trabajo?',default=False)
    solicitud_permiso_trabajo = models.BooleanField('¿Ya ha solicitado el permiso de trabajo?',default=False)

    def __str__(self):
        return str ((self.user.user.first_name)+" "+(self.user.user.last_name))

class Hijo(models.Model):
    user = models.ForeignKey(Empleado, related_name="user_de_hijos")
    nombre = models.CharField('Nombre', max_length=600)
    apellido_paterno = models.CharField('Apellido paterno', max_length=600)
    apellido_materno = models.CharField('Apellido materno', max_length=600)
    fecha_nacimiento = models.DateTimeField('Fecha de nacimiento', auto_now_add = False)
    edad = models.IntegerField('Edad')
    
    def __str__(self):
        return str ((self.user.user.first_name)+" "+(self.user.user.last_name))

class Estudio(models.Model):
    user = models.ForeignKey(Empleado, related_name='user_de_nivel_estudios')
    nivel_estudios = models.CharField('Nivel de estudios máximo', max_length=60, choices=NIVEL_ESTUDIOS, default=Profesional)
    universidad = models.CharField('Universidad de donde es (o será) títulado',max_length=100, blank=True, null=True)
    titulo = models.CharField('Título universitario obtenido o a obtener', max_length=100, blank=True, null=True)
    carrera = models.CharField('Carrera o profesión', max_length=100, blank=True, null=True)
    cedula_profesional = CedulaProfesional()
    constacia_de_estudio = models.ImageField('Constancia de estudio o diploma universitario',upload_to = 'cedulas_profesionales/', blank=True, null=True)

    def extension(self):
        extension = os.path.splitext(self.constacia_de_estudio.url)
        return extension

    def __str__ (self):
        return str ((self.user.user.first_name)+" "+(self.user.user.last_name))

class Capacitaciones(models.Model):
    user = models.ForeignKey(Empleado, related_name='user_de_curso')
    tipo_curso = models.CharField('Tipo de curso', max_length=60, choices=TIPOS_CURSOS, default=Curso)
    nombre_curso = models.CharField('Título o descripción',max_length=100)
    certificado = models.FileField('Certificado / Constancia',upload_to = 'certificados/', blank=True, null=True)

    def __str__ (self):
        return str ((self.user.user.first_name)+" "+(self.user.user.last_name))+" "+(self.nombre_curso)

class Idioma(models.Model):
    user = models.ForeignKey(Empleado, related_name='user_de_idioma')
    idioma = models.CharField('Idioma', max_length=60)
    nivel_escrito = models.CharField('Nivel Escrito', max_length=60, choices=NIVELES_IDIOMA, default=nivel_bajo)
    nivel_hablado = models.CharField('Nivel Hablado', max_length=60, choices=NIVELES_IDIOMA, default=nivel_bajo)
    conversacion = models.CharField('Entablar conversación', max_length=60, choices=RES_IDIOMA, default="No")
    info_tecnica = models.CharField('Leer información técnica', max_length=60, choices=RES_IDIOMA, default="No")
    redactar = models.CharField('Puede redactar', max_length=60, choices=RES_IDIOMA, default="No")
    leer = models.CharField('Puede leer', max_length=60, choices=RES_IDIOMA, default="No")

    def __str__ (self):
        return str ((self.user.user.first_name)+" "+(self.user.user.last_name))+" "+(self.idioma)

class Domicilio(models.Model):
    user = models.ForeignKey(Empleado, related_name='user_de_domicilio')
    tipo_comprobante = models.CharField('Tipo de comprobante de domicilio', max_length=60, choices=TIPOS_COMPROBANTES, default=Agua)
    comprobante_domicilio = models.FileField('Comprobante de domicilio',upload_to = 'comprobantes_domicilio/')
    tlf_residencial = models.CharField('Teléfono residencial',max_length=255)
    def __str__ (self):
        return str ((self.user.user.first_name)+" "+(self.user.user.last_name))

class Recomendaciones(models.Model):
    user = models.ForeignKey(Empleado, related_name='user_de_recomendaciones')
    carta_recomendacion = models.FileField('Carta de recomendación',upload_to = 'cartas_recomendacion/', blank=True, null=True)
    def __str__ (self):
        return str ((self.user.user.first_name)+" "+(self.user.user.last_name))

class Banco(models.Model):
    user = models.ForeignKey(Empleado, related_name='user_de_banco')
    banco = models.CharField('Entidad bancaria', max_length=60, choices=BANCOS, default=Banco_Nacional_de_Mexico_Banamex)
    contrato = models.FileField('Cabecera de contrato bancario',upload_to = 'bancos/')
    clabe = models.PositiveIntegerField('Clabe', validators=[MaxValueValidator(999999999999999999)]) 
    def __str__ (self):
        return str ((self.user.user.first_name)+" "+(self.user.user.last_name))