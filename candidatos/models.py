#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
#from .opciones import *
from composite_field import CompositeField
from os.path import splitext, basename
from django.core.validators import MaxValueValidator
from empleados.models import Country



# Create your models here.

class TipoDocumentoIdentidad(models.Model):
    tipo_documento = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return str(self.tipo_documento)

class Candidato(models.Model):
    #sección 1(datos personales)
    emp_id=models.IntegerField('ID de empleado',blank = True, null = True)
    fecha_solicitud = models.DateTimeField('Fecha de solicitud', auto_now_add = True)
    fuente_recluta = models.CharField('Fuente de reclutamiento',max_length=100,null = True)
    puesto_solicitado = models.CharField('Puesto solicitado',max_length=100,null = True)
    sueldo_deseado = models.CharField('Sueldo deseado',max_length=6,null = True)
    ###datos personales
    nombre = models.CharField('Nombre',null = False,max_length=60)
    apellido_paterno = models.CharField('Apellido paterno',null = False,max_length=60)
    apellido_materno = models.CharField('Apellido materno',null = False,max_length=60)
    sexo = models.CharField('Sexo',max_length=9)
    estado_civil = models.CharField('Estado civil',max_length=11)
    edad = models.CharField('Edad',max_length=3)
    fecha_nac = models.DateTimeField('Fecha de nacimiento', auto_now_add = False,null = True)
    lugar_nac = models.CharField('Lugar de nacimiento',null = True,max_length=60)
    pais_nacimiento = models.ForeignKey(Country, null = True, related_name="pais_nacimiento_cand")
    tel = models.CharField('Teléfono',max_length=16,blank = True, null = True)
    cel = models.CharField('Celular',max_length=16,null = True)
    tipo = models.CharField('Tipo de casa habitación',max_length=12)
    calle = models.CharField('Calle',max_length=60,null = True)
    num_ext = models.CharField('Número exterior',max_length=7,null = True)
    num_int = models.CharField('Número interior',max_length=7,null =True,blank=True)
    calle_uno = models.CharField('Entre calle',max_length=60,null = True)
    calle_dos = models.CharField('Y calle',max_length=60,null = True)
    piso = models.CharField('Piso',max_length=6, null=True, blank=True)
    depto =models.CharField('Departamento',max_length=6, null=True, blank=True)
    cp = models.IntegerField('Código postal',blank = False, default=0,null = True)
    colonia = models.CharField('Colonia',max_length=60,null = True)
    esdo = models.CharField('Estado',max_length=60, blank=True,null = True)
    pais_direc = models.ForeignKey(Country, related_name="pais_de_direccion_cand", default=1,null = True)
    referencia = models.TextField('Referencia',max_length=200, blank = True, null = True)
    trayectoria_de_casa=models.CharField('Tiempo de trayectoria desde casa',max_length=60, null = True)
    email_personal = models.CharField('Correo personal',max_length=60, blank = True, null = True)
    rfc = models.CharField('RFC',max_length=15, blank = True, null = True)
    curp = models.CharField('CURP',max_length=18, blank = True, null = True)
    imss = models.IntegerField('Afiliación IMSS',blank = True, null = True)
    cartilla=models.IntegerField('Número de Cartilla',blank = True, null = True)
    tipo_licencia = models.CharField('Tipo de licencia',max_length=20)
    licencia=models.CharField('Número de licencia',blank = True, null = True,max_length=12)
    ###############campos agregados
    activo= models.CharField(max_length=2,default='SI', blank = True, null = True)
    fecha_baja = models.DateTimeField('Fecha de baja', auto_now_add = True, blank = True, null = True)
    motivo = models.TextField('Motivo',max_length=200, blank = True, null = True)
    tipo_baja = models.CharField('Tipo de baja',max_length=9, blank = True, null = True)
    tipo_documento_identidad = models.ForeignKey(TipoDocumentoIdentidad, related_name="tipo_docu_ident", blank = True, null = True)


    ####imagenes
    #personal de base
    curriculum = models.FileField(upload_to = 'curriculums/', blank = True, null = True)
    docu_ident_front = models.ImageField(upload_to = 'documentos_identidad/', blank = True, null = True)
    docu_ident_back = models.ImageField(upload_to = 'documentos_identidad/', blank = True, null = True)
    acta_nacimiento = models.ImageField(upload_to = 'actas_nacimiento/', blank = True, null = True)
    imagen_curp = models.ImageField(upload_to = 'curps/', blank = True, null = True)
    imagen_rfc = models.ImageField(upload_to = 'rfcs/', blank = True, null = True)
    comprobante_domicilio = models.FileField(upload_to = 'comprobantes_domicilio/', blank = True, null = True)
    imagen_imss = models.ImageField(upload_to = 'imss/', blank = True, null = True)
    carta1_recomendacion = models.FileField(upload_to = 'cartas_recomendacion/', blank=True, null=True)
    carta2_recomendacion = models.FileField(upload_to = 'cartas_recomendacion/', blank=True, null=True)
    contrato = models.FileField(upload_to = 'bancos/', blank = True, null = True)
    imagen_infonavit = models.ImageField(upload_to = 'infonavit/', blank = True, null = True)
    imagen_lic_anverso = models.ImageField(upload_to = 'licencias_conducir/', blank = True, null = True)
    imagen_lic_reverso = models.ImageField(upload_to = 'licencias_conducir/', blank = True, null = True)
    imagen_cartilla = models.ImageField(upload_to = 'documentos_identidad/', blank = True, null = True)
    #extranjeros
    permiso = models.ImageField(upload_to = 'permisos/', blank = True, null = True)
    
    #becarios
    oficio = models.ImageField(upload_to = 'oficios/', blank = True, null = True)
    #menores
    carta_menor = models.ImageField(upload_to = 'cartas_menor/', blank = True, null = True)
    INE_frenteTut = models.ImageField(upload_to = 'documentos_identidad/', blank = True, null = True)
    INE_atrasTut = models.ImageField(upload_to = 'documentos_identidad/', blank = True, null = True)



    ##################################################

    #email_personal = models.EmailField(max_length=600)

    #sección 2(antecedentes académicos)
    primaria = models.CharField('Primaria',max_length=100,null = True,blank = True)
#    primaria_domicilio = models.CharField('Domicilio de primaria',max_length=200,null = True)
    primaria_annios=models.IntegerField('Años cursados',blank = True, null = True)
    primaria_inicio = models.CharField('Fecha de inicio',max_length=4, null = True,blank = True)
    primaria_termino = models.CharField('Fecha de término',max_length=4, null = True,blank = True)
    primaria_documento = models.CharField('Documento recibido',max_length=50,null = True,blank = True)
    
    secundaria = models.CharField('Secundaria',max_length=100,null = True,blank = True)
    #secundaria_domicilio = models.CharField('Domicilio',max_length=200,null = True)
    secundaria_annios=models.IntegerField('Años cursados',blank = True, null = True)
    secundaria_inicio = models.CharField('Fecha de inicio',max_length=4,null = True,blank = True)
    secundaria_termino = models.CharField('Fecha de término',max_length=4,null = True,blank = True)
    secundaria_documento = models.CharField('Documento recibido',max_length=50,null = True,blank = True)
    preparatoria = models.CharField('Preparatoria',max_length=100,null = True,blank = True)
    #preparatoria_domicilio = models.CharField('Domicilio',max_length=200,null = True)
    preparatoria_annios=models.IntegerField('Años cursados',blank = True, null = True)
    preparatoria_inicio = models.CharField('Fecha de inicio',max_length=4,null = True,blank = True)
    preparatoria_termino = models.CharField('Fecha de término',max_length=4,null = True,blank = True)
    preparatoria_documento = models.CharField('Documento recibido',max_length=50,null = True,blank = True)
    tecnica = models.CharField('Técnica',max_length=100,null = True,blank = True)
    #tecnica_domicilio = models.CharField('Domicilio',max_length=200,null = True)
    tecnica_annios=models.IntegerField('Años cursados',blank = True, null = True)
    tecnica_inicio = models.CharField('Fecha de inicio',max_length=4,null = True,blank = True)
    tecnica_termino = models.CharField('Fecha de término',max_length=4,null = True,blank = True)
    tecnica_documento = models.CharField('Documento recibido',max_length=50,null = True,blank = True)
    
    estudia_actualmente = models.CharField('¿Estudia actualmente?',max_length=2,null = True,blank = True)
    estudia_que = models.CharField('¿Qué estudia?',max_length=60,null = True,blank = True)
    estudia_donde = models.CharField('¿Dónde estudia?',max_length=60,null = True,blank = True)
    estudia_horario = models.CharField('Horario',max_length=20,null = True,blank = True)
    estudia_termino = models.DateTimeField('Fecha de término', auto_now_add = False,null = True,blank = True)
    maquinas_equipos= models.CharField('Maquinas o equipos que maneja',max_length=200,null = True,blank = True)


    #sección 3(datos familiares, padre, madre, conyuge)
    padre_nombre = models.CharField('Nombre del padre',null = True,max_length=60,blank = True)
    padre_apellido_paterno = models.CharField('Apellido paterno del padre',null = True,max_length=60,blank = True)
    padre_apellido_materno = models.CharField('Apellido materno del padre',null = True,max_length=60,blank = True)
    padre_edad = models.IntegerField('Edad del padre',blank=True, null=True)
    padre_ocupacion = models.CharField('Ocupación del padre',null = True,max_length=60,blank = True)
    padre_lugar_trabajo = models.CharField('Lugar de trabajo del padre',null = True,max_length=60,blank = True)
    padre_domicilio = models.CharField('Domicilio del padre',null = True,max_length=200,blank = True)
    padre_tel = models.CharField('Teléfono o celular del padre',max_length=16,null = True,blank = True)
    padre_vive=models.CharField('',blank = True, null = True,max_length=6)
    
    madre_nombre = models.CharField('Nombre de la madre',null = True,max_length=60,blank = True)
    madre_apellido_paterno = models.CharField('Apellido paterno de la madre',null = True,max_length=60,blank = True)
    madre_apellido_materno = models.CharField('Apellido materno de la madre',null = True,max_length=60,blank = True)
    madre_edad = models.IntegerField('Edad de la madre',blank=True, null=True)
    madre_ocupacion = models.CharField('Ocupación de la madre',null = True,max_length=60,blank = True)
    madre_lugar_trabajo = models.CharField('Lugar de trabajo de la madre',null = True,max_length=60,blank = True)
    madre_domicilio = models.CharField('Domicilio de la madre',null = True,max_length=200,blank = True)
    madre_tel = models.CharField('Teléfono o celular de la madre',max_length=16,blank = True)
    madre_vive=models.CharField('',blank = True, null = True,max_length=6)

    conyuge_nombre = models.CharField('Nombre del conyuge',null = True,max_length=60,blank = True)
    conyuge_apellido_paterno = models.CharField('Apellido paterno del conyuge',null = True,max_length=60,blank = True)
    conyuge_apellido_materno = models.CharField('Apellido materno del conyuge',null = True,max_length=60,blank = True)
    conyuge_edad = models.IntegerField('Edad del conyuge',blank=True, null=True)
    conyuge_ocupacion = models.CharField('Ocupación del conyuge',null = True,max_length=60,blank = True)
    conyuge_lugar_trabajo = models.CharField('Lugar de trabajo del conyuge',null = True,max_length=60,blank = True)
    conyuge_domicilio = models.CharField('Domicilio del conyuge',null = True,max_length=200,blank = True)
    conyuge_tel = models.CharField('Teléfono o celular del conyuge',max_length=16,blank = True)
    conyuge_vive=models.CharField('',blank = True, null = True,max_length=6)

    #sección 4(datos generales)
    vivienda_propia = models.CharField('Vive en casa',null = True,max_length=8,blank = True)
    credito_infonavit = models.CharField('¿Tiene crédito infonavit?',null = True,max_length=2,blank = True)
    pago_infonavit = models.CharField('Pago mensual de infonavit',null = True,max_length=6,blank = True)
    auto_propio = models.CharField('¿Cuenta con automóvil?',null = True,max_length=2,blank = True)
    auto_marca = models.CharField('Marca del automóvil',null = True,max_length=20,blank = True)
    auto_modelo = models.CharField('Modelo del automóvil',null = True,max_length=20,blank = True)
    seguro_vida = models.CharField('¿Cuenta con seguro de vida?',null = True,max_length=2,blank = True)
    seguro_monto = models.CharField('Monto del seguro de vida',null = True,max_length=10,blank = True)     
    afianzado = models.CharField('¿Ha sido afianzado?',null = True,max_length=2,blank = True)     
    afianzado_monto = models.CharField('Monto afianzado',null = True,max_length=10,blank = True)     
    afiliado_sindicato = models.CharField('¿Esta afiliado a algún sindicato?',null = True,max_length=2,blank = True)
    sindicato_nombre = models.CharField('Nombre del sindicato',null = True,max_length=50,blank = True)     
    sindicato_cargo = models.CharField('Cargo en el sindicato',null = True,max_length=50,blank = True)     
    tiempo_libre = models.CharField('¿A qué dedica su tiempo libre?',null = True,max_length=50,blank = True)     
    embarazo = models.CharField('¿Está embarazada?',null = True,max_length=2,blank = True)     
    religion = models.CharField('Religión',null = True,max_length=50,blank = True)     
    disposicion_rolar = models.CharField('¿Dispuesto a rolar turnos?',null = True,max_length=2,blank = True)
    estado_salud = models.CharField('Estado de salud',null = True,max_length=20,blank = True)
    fuma = models.CharField('¿Fuma?',null = True,max_length=2,blank = True)
    bebe = models.CharField('¿Tiene bebe?(de 0 a 3 años)',null = True,max_length=2,blank = True)
    tatuajes = models.CharField('¿Tiene tatuajes?',null = True,max_length=2,blank = True)
    perforaciones = models.CharField('¿Tiene perforaciones?',null = True,max_length=2,blank = True)
    disposicion_viajar = models.CharField('¿Dispuesto a viajar?',null = True,max_length=2,blank = True)
    ingreso_extra = models.CharField('¿Tiene otros ingresos?',null = True,max_length=2,blank = True)
    ingreso_monto = models.CharField('Monto del ingreso extra',null = True,max_length=6,blank = True)
    ingreso_fuente = models.CharField('Fuente del ingreso extra',null = True,max_length=50,blank = True)
    labora_conocido = models.CharField('¿Labora un familiar o conocido con nosotros?',null = True,max_length=2,blank = True)
    conocido_nombre = models.CharField('Nombre del familiar o conocido',null = True,max_length=180,blank = True)
    conocido_depto = models.CharField('Departamento donde labora',null = True,max_length=50,blank = True)
    fecha_disponible = models.DateTimeField('Fecha disponible para iniciar', auto_now_add = False,null = True,blank = True)
    
    def __str__(self):
        return str ((self.nombre)+" "+(self.apellido_paterno)+" "+(self.apellido_materno))


class Idioma_candidato(models.Model):
    candidato = models.ForeignKey(Candidato, related_name='idioma_candidato')
    idioma = models.CharField('Idioma', max_length=60)
    idioma_porcentaje=models.IntegerField('Porcentaje',blank = True, null = True)
    #nivel_escrito = models.CharField('Nivel Escrito', max_length=60, choices=NIVELES_IDIOMA, default=nivel_bajo)
    #nivel_hablado = models.CharField('Nivel Hablado', max_length=60, choices=NIVELES_IDIOMA, default=nivel_bajo)
    #conversacion = models.CharField('Entablar conversación', max_length=60, choices=RES_IDIOMA, default="No")
    #info_tecnica = models.CharField('Leer información técnica', max_length=60, choices=RES_IDIOMA, default="No")
    #redactar = models.CharField('Puede redactar', max_length=60, choices=RES_IDIOMA, default="No")
    #leer = models.CharField('Puede leer', max_length=60, choices=RES_IDIOMA, default="No")

    def __str__ (self):
        return str (self.idioma)
    
class Estudios_pro(models.Model):
    candidato = models.ForeignKey(Candidato, related_name='estudios_candidato')
    estudios_tipo = models.CharField('Tipo de estudio',max_length=12,null = False)
    estudios_escuela = models.CharField('Lugar',max_length=100,null = False)
    estudios_nombre = models.CharField('Estudio',max_length=50,null = False)
    estudios_annios=models.IntegerField('Años cursados',blank = True, null = False)
    estudios_inicio = models.CharField('Fecha de inicio',max_length=4,null = False)
    estudios_termino = models.CharField('Fecha de término',max_length=4,null = False)
    estudios_documento = models.CharField('Documento recibido',max_length=50,null = False)
    estudios_tesis = models.CharField('Nombre de tesis',max_length=50,null = True)
    estudios_forma = models.CharField('Forma de titulación',max_length=50,null = True)
    estudios_cedula=models.CharField('Número de cédula',max_length=8,null = True)
    comprobante = models.FileField(upload_to = 'compro_est_pro/', blank = True, null = True)
    def __str__ (self):
        return str (self.estudios_nombre)

class Estudios_otros(models.Model):
    candidato = models.ForeignKey(Candidato, related_name='estudiosotros_candidato')
    estudios_tipo = models.CharField('Tipo de estudio',max_length=12,null = False)
    estudios_nombre = models.CharField('Estudio',max_length=50,null = False)
    estudios_inicio = models.CharField('Fecha de inicio',max_length=4,null = False)
    estudios_termino = models.CharField('Fecha de término',max_length=4,null = False)
    estudios_documento = models.CharField('Documento recibido',max_length=50,null = False)
    comprobante = models.FileField(upload_to = 'compro_est_otros/', blank = True, null = True)
    def __str__ (self):
        return str (self.estudios_nombre)

#sección 3(datos familiares, hermanos)
class Hermano_candidato(models.Model):
    candidato = models.ForeignKey(Candidato, related_name='hermano_candidato')
    hermano_nombre = models.CharField('Nombre del hermano',null = False,max_length=120)
    hermano_apellido_paterno = models.CharField('Apellido paterno del hermano',blank = True, null = True,max_length=60)
    hermano_apellido_materno = models.CharField('Apellido materno del hermano',blank = True, null = True,max_length=60)
    hermano_edad = models.CharField('Edad del hermano',blank = True, null = True,max_length=2)
    hermano_ocupacion = models.CharField('Ocupación del hermano',blank = True, null = True,max_length=60)
    hermano_lugar_ocupacion = models.CharField('Lugar de trabajo del hermano',blank = True, null = True,max_length=60)
    hermano_domicilio = models.CharField('Domicilio del hermano',blank = True, null = True,max_length=200)
    hermano_tel = models.CharField('Teléfono o celular del hermano',blank = True, null = True,max_length=16)

    def __str__ (self):
        return str (self.hermano_nombre)

#sección 3(datos familiares, hijos)
class Hijo_candidato(models.Model):
    candidato = models.ForeignKey(Candidato, related_name='hijo_candidato')
    hijo_nombre = models.CharField('Nombre del hijo',null = False,max_length=120)
    hijo_apellido_paterno = models.CharField('Apellido paterno del hijo',blank = True, null = True,max_length=60)
    hijo_apellido_materno = models.CharField('Apellido materno del hijo',blank = True, null = True,max_length=60)
    hijo_edad = models.CharField('Edad del hijo',blank = True, null = True,max_length=2)
    hijo_ocupacion = models.CharField('Ocupación del hijo',blank = True, null = True,max_length=60)
    hijo_lugar_ocupacion = models.CharField('Lugar de trabajo del hijo',blank = True, null = True,max_length=60)
    hijo_domicilio = models.CharField('Domicilio del hijo',blank = True, null = True,max_length=200)
    hijo_tel = models.CharField('Teléfono o celular del hijo',blank = True, null = True,max_length=16)
    def __str__ (self):
        return str (self.hijo_nombre)

#sección 5(experiencia laboral)
class Experiencia(models.Model):
    candidato = models.ForeignKey(Candidato, related_name='experiencia_candidato')
    empresa_nombre = models.CharField('Empresa actual última',null = False,max_length=100)
    empresa_direccion = models.CharField('Dirección',blank = True,null = True,max_length=100)
    empresa_tel = models.CharField('Teléfono',max_length=16,blank = True,null = True)
    empresa_giro = models.CharField('Giro',null = False,max_length=100)
    empresa_nombre_jefe = models.CharField('Nombre del jefe inmediato',null = False,max_length=100)
    empresa_jefe_puesto = models.CharField('Puesto del jefe inmediato',null = False,max_length=100)
    empresa_fecha_ingreso = models.DateTimeField('Fecha de ingreso en la empresa', auto_now_add = False,null = False)
    empresa_salario_inicio = models.CharField('Salario inicial',null = False,max_length=6)
    empresa_fecha_separacion = models.DateTimeField('Fecha de separación de la empresa', auto_now_add = False,blank = True,null = True)
    empresa_salario_final = models.CharField('Salario final',null = False,max_length=6)
    empresa_puesto_ultimo = models.CharField('Último puesto desempeñado',null = False,max_length=50)
    empresa_puesto_ultimo_tiempo = models.CharField('Tiempo del ultimo puesto',null = False,max_length=20)
    empresa_puesto_ultimo_depto = models.CharField('Departamento del último puesto desempeñado',null = False,max_length=50)
    empresa_puesto_anterior = models.CharField('Anterior puesto desempeñado',blank = True,null = True,max_length=50)
    empresa_puesto_anterior_tiempo = models.CharField('Tiempo del anterior puesto',blank = True,null = True,max_length=20)
    empresa_puesto_anterior_depto = models.CharField('Departamento del anterior puesto desempeñado',blank = True,null = True,max_length=50)
    experiencia_supervision = models.CharField('¿Tiene experiencia en supervisión?',null = False,max_length=2)
    empresa_actual = models.CharField('¿Empresa actual?',null = False,max_length=2)
    experiencia_supervision_num = models.CharField('Número de personas que superviso',blank = True,null = True,max_length=3)
    separacion_motivo = models.CharField('¿Cuál fué el motivo de la separación?',null = True,max_length=100)

    def __str__ (self):
        return str (self.empresa_nombre)

#sección 6(referencias)
class Referencia(models.Model):
    candidato = models.ForeignKey(Candidato, related_name='referencia_candidato')
    referencia_nombre = models.CharField('Nombre de la persona que lo conoce(no incluir parientes o jefes anteriores)',null = False,max_length=100)
    referencia_domicilio = models.CharField('Domicilio de la referencia',null = True,max_length=200)
    referencia_tel = models.CharField('Teléfono',null = True,max_length=16)
    referencia_ocupacion = models.CharField('¿A qué se dedica?',null = False,max_length=100)
    referencia_annios_conocer = models.CharField('Años de conocerlo',null = False,max_length=2)

    def __str__ (self):
        return str (self.referencia_nombre)

class Cand_docs(models.Model):
    candidato = models.ForeignKey(Candidato, related_name='docs_candidato')
    INE = models.BooleanField('INE',default=False)
    Acta = models.BooleanField('Acta de nacimiento',default=False)
    CURP = models.BooleanField('CURP',default=False)
    RFC = models.BooleanField('RFC',default=False)
    Comp_dom = models.BooleanField('Comprobante de domicilio',default=False)
    Comp_grado = models.BooleanField('Comprobante de último grado',default=False)
    Comp_cursos = models.BooleanField('Comprobantes de cursos, certificaciones, etc.',default=False)
    Comp_permiso = models.BooleanField('Comprobante de permiso laboral(solo extranjero)',default=False)
    IMSS = models.BooleanField('Afiliación al IMSS',default=False)
    Cartas = models.BooleanField('Cartas de recomendación',default=False)
    Esdo_cuenta = models.BooleanField('Esdo. cuenta bancario, tarjeta y CLABE',default=False)
    Esdo_info = models.BooleanField('Esdo. cuenta Infonacot/infonavit',default=False)
    Lic_manejo = models.BooleanField('Lic. de manejo',default=False)
    Observaciones = models.TextField('Observaciones',max_length=200,blank=True,null = True)
    def __str__ (self):
        return str ()