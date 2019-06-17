#-*- coding: utf-8 -*-
from django import forms
from empleados.models import *
from candidatos.models import *
from empleados.opciones import *
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import *
from django.conf import settings
from django.forms import ModelChoiceField, ModelMultipleChoiceField
from django.core.files import File
from django.core.validators import RegexValidator, ValidationError
from django.utils.safestring import mark_safe
from django.forms import extras
from django.contrib.admin import widgets
from django.forms import formset_factory
import datetime
from .opciones import *



class CandidatoSecunoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CandidatoSecunoForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
            self.fields[campos].required = False
            
        
        
    class Meta:
        model = Candidato
        fields = ('emp_id','fuente_recluta','puesto_solicitado','sueldo_deseado','nombre', 'apellido_paterno', 'apellido_materno','sexo',
                  'estado_civil','edad','fecha_nac','lugar_nac','pais_nacimiento','tel','cel','tipo','calle','num_ext','num_int',
                  'calle_uno','calle_dos','piso','depto','cp','colonia','esdo','pais_direc','referencia','trayectoria_de_casa',
                  'email_personal','rfc','curp','imss','cartilla','tipo_licencia','licencia')


class CandidatoSecdosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CandidatoSecdosForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
            self.fields[campos].required = False
            
        
        
    class Meta:
        model = Candidato
        fields = ('primaria','primaria_annios','primaria_inicio', 'primaria_termino', 'primaria_documento',
                  'secundaria','secundaria_annios','secundaria_inicio', 'secundaria_termino', 'secundaria_documento',
                  'preparatoria','preparatoria_annios','preparatoria_inicio', 'preparatoria_termino', 'preparatoria_documento',
                  'tecnica','tecnica_annios','tecnica_inicio', 'tecnica_termino', 'tecnica_documento',
                  'estudia_actualmente','estudia_que','estudia_donde','estudia_horario','estudia_termino','maquinas_equipos'
        )

class CandidatoSectresForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CandidatoSectresForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
            self.fields[campos].required = False
            
        
        
    class Meta:
        model = Candidato
        fields = ('padre_nombre','padre_apellido_paterno','padre_apellido_materno','padre_edad', 'padre_ocupacion', 'padre_lugar_trabajo','padre_domicilio','padre_tel','padre_vive',
                  'madre_nombre','madre_apellido_paterno','madre_apellido_materno','madre_edad', 'madre_ocupacion', 'madre_lugar_trabajo','madre_domicilio','madre_tel','madre_vive',
                  'conyuge_nombre','conyuge_apellido_paterno','conyuge_apellido_materno','conyuge_edad', 'conyuge_ocupacion', 'conyuge_lugar_trabajo','conyuge_domicilio','conyuge_tel','conyuge_vive',
        
        )

class CandidatoSeccuatroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CandidatoSeccuatroForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
            self.fields[campos].required = False
        
    class Meta:
        model = Candidato
        fields = ('vivienda_propia','credito_infonavit','pago_infonavit','auto_propio', 'auto_marca', 'auto_modelo','seguro_vida','seguro_monto',
                  'afianzado','afianzado_monto','afiliado_sindicato','sindicato_nombre', 'sindicato_cargo', 'tiempo_libre','embarazo','religion',
                  'disposicion_rolar','estado_salud','fuma','bebe', 'tatuajes', 'perforaciones','disposicion_viajar','ingreso_extra',
                  'ingreso_monto','ingreso_fuente','labora_conocido','conocido_nombre', 'conocido_depto', 'fecha_disponible'
        
        )

class IdiomaSecdosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IdiomaSecdosForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
            self.fields[campos].required = False
        
    class Meta:
        model = Idioma_candidato
        fields = ('idioma','idioma_porcentaje')

class EstudioSecdosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EstudioSecdosForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
            self.fields[campos].required = False
        
    class Meta:
        model = Estudios_pro
        fields = ('estudios_tipo','estudios_escuela','estudios_nombre','estudios_annios','estudios_inicio','estudios_termino','estudios_documento','estudios_tesis','estudios_forma','estudios_cedula')

class EstudioOtroSecdosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EstudioOtroSecdosForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
            self.fields[campos].required = False
        
    class Meta:
        model = Estudios_otros
        fields = ('estudios_tipo','estudios_nombre','estudios_inicio','estudios_termino','estudios_documento')

class HijoSectresForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HijoSectresForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
            self.fields[campos].required = False
        
    class Meta:
        model = Hijo_candidato
        fields = ('hijo_nombre','hijo_apellido_paterno','hijo_apellido_materno','hijo_edad','hijo_ocupacion','hijo_lugar_ocupacion','hijo_domicilio','hijo_tel')

class HermanoSectresForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HermanoSectresForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
            self.fields[campos].required = False
        
    class Meta:
        model = Hermano_candidato
        fields = ('hermano_nombre','hermano_apellido_paterno','hermano_apellido_materno','hermano_edad','hermano_ocupacion','hermano_lugar_ocupacion','hermano_domicilio','hermano_tel'
        )

class ExperienciaSeccincoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExperienciaSeccincoForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
            self.fields[campos].required = False
        
    class Meta:
        model = Experiencia
        fields = ('empresa_nombre','empresa_direccion','empresa_tel','empresa_giro','empresa_nombre_jefe','empresa_jefe_puesto',
                  'empresa_fecha_ingreso','empresa_salario_inicio','empresa_fecha_separacion','empresa_salario_final','empresa_puesto_ultimo','empresa_puesto_ultimo_tiempo','empresa_actual',
                  'empresa_puesto_ultimo_depto','empresa_puesto_anterior','empresa_puesto_anterior_tiempo','empresa_puesto_anterior_depto','experiencia_supervision','experiencia_supervision_num','separacion_motivo'
                  )

class ReferenciaSecseisForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReferenciaSecseisForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
            self.fields[campos].required = False
        
    class Meta:
        model = Referencia
        fields = ('referencia_nombre','referencia_domicilio','referencia_tel','referencia_ocupacion','referencia_annios_conocer')

class Formulario_candidato(forms.Form):
    #sección 1(datos personales)
    #con_id = forms.HiddenInput()
    con_id = forms.CharField(label='reset', max_length=20, widget=forms.HiddenInput())
    fecha_solicitud = forms.DateField(label = 'Fecha_solicitud',required = True, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
    fuente_recluta = forms.CharField(label = 'Fuente de reclutamiento', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'100'}))
    puesto_solicitado = forms.CharField(label = 'Puesto solicitado', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'100'}))
    sueldo_deseado = forms.CharField(label = 'Sueldo deseado( Mensual )', required = True, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'6','onkeypress':'return soloNumeros(event)'}))
    nombre = forms.CharField(label = 'Nombre', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    apellido_paterno = forms.CharField(label = 'Apellido paterno', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    apellido_materno = forms.CharField(label = 'Apellido materno', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    
    sexo = forms.ChoiceField(label = 'Sexo', required = True,initial=1,choices = SEXO, widget = forms.Select(attrs={'class': 'form-control'}))
    estado_civil = forms.ChoiceField(label = 'Estado civil', choices=ESTADO_CIVIL,required = True, initial=Soltero, widget = forms.Select(attrs={'class': 'form-control'}))
    edad = forms.IntegerField(label = 'Edad', required = True, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','MAX':'90','onkeypress':'return soloNumeros(event)'}))
    fecha_nac = forms.DateField(label = 'Fecha de nacimiento', required = True,input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'10', 'placeholder': 'DD/MM/AAAA'}))
    lugar_nac = forms.CharField(label = 'Lugar de nacimiento', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    pais_nacimiento = forms.ModelChoiceField(label = 'País de nacimiento', required = True, queryset=Country.objects.all().order_by('pais'), initial=1,  widget = forms.Select(attrs={'class': 'form-control'}))
    
    tel = forms.CharField(label = 'Teléfono de casa', required = False,widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)', 'placeholder': 'Número de teléfono con lada'}))
    cel = forms.CharField(label = 'Celular', required = True,widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)', 'placeholder': 'Ingresa los 10 digitos'}))
    tipo = forms.ChoiceField(label = 'Tipo de casa habitación', required = True, initial=1, choices = TIPO_HABITACION,  widget = forms.Select(attrs={'class': 'form-control'}))
    
    calle = forms.CharField(label = 'Calle', required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'60'}))
    num_ext = forms.CharField(label = '#Exterior', required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'7'}))
    num_int = forms.CharField(label = '#Interior',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'7'}))
    calle_uno = forms.CharField(label = 'Entre', required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'60'}))
    
    calle_dos = forms.CharField(label = 'Y calle',required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'60'}))
    piso = forms.CharField(label = 'Piso',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'6'}))
    depto = forms.CharField(label = 'Departamento',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'6'}))
    cp = forms.CharField(label = 'CP', required = True, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'5', 'data-mask': '99999','onkeypress':'return soloNumeros(event)', 'placeholder': 'Ingresa los 5 digitos'}))
    
    colonia = forms.CharField(label = 'Colonia o fraccionamiento',required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'60'}))
    esdo = forms.ChoiceField(label = 'Estado', required = True, initial=1, choices = STATUS_CHOICES,  widget = forms.Select(attrs={'class': 'form-control'}))
    pais_direc = forms.ModelChoiceField(label = 'País', required = True, queryset=Country.objects.all().order_by('pais'), initial=6,  widget = forms.Select(attrs={'class': 'form-control'}))
    
    referencia = forms.CharField(label = 'Referencia',required = True, widget = forms.Textarea(attrs={'class': 'form-control sololetrasynumeros','cols':'40','rows':'3','maxlength':'200', 'placeholder': '¿Cómo llegar?, si se encuentra cerca de algún negocio, escuela, etc'}))
    trayectoria_de_casa = forms.CharField(label = 'Tiempo de trayectoria desde casa',required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'60'}))
    #trayectoria_de_casa = forms.ChoiceField(label = 'Tiempo de trayectoria desde casa', choices=TIEMPO_TRAYECTO,required = True, initial=1, widget = forms.Select(attrs={'class': 'form-control'}))
    email_personal = forms.EmailField(label = "Correo personal", required = False, widget = forms.TextInput(attrs={'class': 'form-control' }))
    
    rfc = forms.CharField(label = 'RFC', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'15'}))
    curp = forms.CharField(label = 'CURP', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'18', 'placeholder': 'Lo encuentra puedes encontrar en el INE'}))
    imss = forms.CharField(label = 'IMSS', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'11','onkeypress':'return soloNumeros(event)', 'placeholder': 'Ingrese los 12 digitos de tu NSS'}))
    cartilla = forms.CharField(label = 'Cartilla', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'10','onkeypress':'return soloNumeros(event)'}))
    #tipo_licencia = forms.CharField(label = 'Tipo de licencia', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'20'}))
    tipo_licencia = forms.ChoiceField(label = 'Tipo de licencia', choices=TIPO_LICENCIA,required = True, initial=5, widget = forms.Select(attrs={'class': 'form-control sololetras'}))
    licencia = forms.CharField(label = 'Número de licencia', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'12','onkeypress':'return soloNumeros(event)'}))
    
    #sección 2(antecedentes académicos)
    primaria = forms.CharField(label = 'Primaria', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'100'}))
    #primaria_domicilio = forms.CharField(label = 'Dirección', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'200'}))
    primaria_annios = forms.CharField(label = 'Años', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))
  
    primaria_inicio = forms.DateField(label = 'Fecha de inicio',required = False, input_formats=settings.YEAR_FORMAT, widget=forms.TextInput(attrs={'class': 'form-control year','maxlength':'4'}))
    primaria_termino = forms.DateField(label = 'Fecha de término',required = False, input_formats=settings.YEAR_FORMAT, widget=forms.TextInput(attrs={'class': 'form-control year','maxlength':'4'}))
    primaria_documento = forms.ChoiceField(label = 'Documento recibido', required = False,initial=0, choices=TIPO_DOCU, widget = forms.Select(attrs={'class': 'form-control'}))
    
    secundaria = forms.CharField(label = 'Secundaria', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'100'}))
    #secundaria_domicilio = forms.CharField(label = 'Dirección', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'200'}))
    secundaria_annios = forms.CharField(label = 'Años', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))
    secundaria_inicio = forms.DateField(label = 'Fecha de inicio',required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control year','maxlength':'4'}))
    secundaria_termino = forms.DateField(label = 'Fecha de término',required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control year','maxlength':'4'}))
    #secundaria_documento = forms.CharField(label = 'Documento recibido', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'50' }))
    secundaria_documento = forms.ChoiceField(label = 'Documento recibido', required = False,initial=0, choices=TIPO_DOCU, widget = forms.Select(attrs={'class': 'form-control'}))
    
    preparatoria = forms.CharField(label = 'Preparatoria', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'100'}))
    #preparatoria_domicilio = forms.CharField(label = 'Dirección', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'200'}))
    preparatoria_annios = forms.CharField(label = 'Años', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))
    preparatoria_inicio = forms.DateField(label = 'Fecha de inicio',required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control year','maxlength':'4'}))
    preparatoria_termino = forms.DateField(label = 'Fecha de término',required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control year','maxlength':'4'}))
    #preparatoria_documento = forms.CharField(label = 'Documento recibido', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'50' }))
    preparatoria_documento = forms.ChoiceField(label = 'Documento recibido', required = False,initial=0, choices=TIPO_DOCU, widget = forms.Select(attrs={'class': 'form-control'}))
    
    tecnica = forms.CharField(label = 'Técnica', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'100','onkeypress':'return soloLetrasyNumeros(event)'}))
    #tecnica_domicilio = forms.CharField(label = 'Dirección', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'200'}))
    tecnica_annios = forms.CharField(label = 'Años', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'2'}))
    tecnica_inicio = forms.DateField(label = 'Fecha de inicio',required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control year','maxlength':'4'}))
    tecnica_termino = forms.DateField(label = 'Fecha de término',required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control year','maxlength':'4'}))
    #tecnica_documento = forms.CharField(label = 'Documento recibido', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'50' }))
    tecnica_documento = forms.ChoiceField(label = 'Documento recibido', required = False,initial=0, choices=TIPO_DOCU, widget = forms.Select(attrs={'class': 'form-control'}))
    
    estudia_actualmente = forms.ChoiceField(label = '¿Estudia actualmente?', required = False, initial=1, choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))
    estudia_que = forms.CharField(label = '¿Qué estudia?', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'60' }))
    estudia_donde = forms.CharField(label = '¿Dónde estudia?', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'60'}))
    estudia_horario = forms.CharField(label = 'Horario', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'20'}))
    estudia_termino = forms.DateField(label = 'Fecha de termino',required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'10','id':'fec_ter', 'placeholder': 'DD/MM/AAAA'}))
    maquinas_equipos = forms.CharField(label = 'Máquinas o equipos que maneja', required = False, widget = forms.Textarea(attrs={'class': 'form-control sololetrasynumeros','maxlength':'200'}))

    #sección 3(datos familiares, padre, madre, conyuge)

    padre_nombre = forms.CharField(label = 'Nombre del padre',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    padre_apellido_paterno = forms.CharField(label = 'Apellido paterno',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    padre_apellido_materno = forms.CharField(label = 'Apellido materno',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    padre_edad = forms.CharField(label = 'Edad',required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))
    
    padre_ocupacion = forms.CharField(label = 'Ocupación',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    padre_lugar_trabajo = forms.CharField(label = 'Lugar de trabajo',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    padre_domicilio = forms.CharField(label = 'Domicilio',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'200'}))
    padre_tel = forms.CharField(label = 'Teléfono o celular',required = False, widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)'}))
    padre_vive = forms.ChoiceField(label = '', required = False, initial=1, choices = TIPO_VIVE, widget = forms.Select(attrs={'class': 'form-control'}))
    
    madre_nombre = forms.CharField(label = 'Nombre de la madre',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    madre_apellido_paterno = forms.CharField(label = 'Apellido paterno',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    madre_apellido_materno = forms.CharField(label = 'Apellido materno',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    madre_edad = forms.CharField(label = 'Edad',required = False,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))
    madre_ocupacion = forms.CharField(label = 'Ocupación',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    madre_lugar_trabajo = forms.CharField(label = 'Lugar de trabajo',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    madre_domicilio = forms.CharField(label = 'Domicilio',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'200'}))
    madre_tel = forms.CharField(label = 'Teléfono o celular',required = False, widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)'}))
    madre_vive = forms.ChoiceField(label = '', required = True, initial=1, choices = TIPO_VIVE, widget = forms.Select(attrs={'class': 'form-control'}))
    
    conyuge_nombre = forms.CharField(label = 'Nombre del conyuge',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    conyuge_apellido_paterno = forms.CharField(label = 'Apellido paterno',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    conyuge_apellido_materno = forms.CharField(label = 'Apellido materno',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    conyuge_edad = forms.CharField(label = 'Edad',required = False,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))
    conyuge_ocupacion = forms.CharField(label = 'Ocupación',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    conyuge_lugar_trabajo = forms.CharField(label = 'Lugar de trabajo',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    conyuge_domicilio = forms.CharField(label = 'Domicilio',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'200'}))
    conyuge_tel = forms.CharField(label = 'Teléfono o celular',required = False, widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)'}))
    conyuge_vive = forms.ChoiceField(label = '', required = True, initial=1, choices = TIPO_VIVE, widget = forms.Select(attrs={'class': 'form-control'}))
    hijos = forms.ChoiceField(label = '¿Tiene hijos?', required = True, choices=SI_NO, initial="No", widget = forms.RadioSelect(attrs={}))
    hermanos = forms.ChoiceField(label = '¿Tiene hermanos?', required = True, choices=SI_NO, initial="No", widget = forms.RadioSelect(attrs={}))


    #sección 4(datos generales)
    vivienda_propia = forms.ChoiceField(label = 'Vive en casa', required = True, initial=1, choices = VIVE_EN_CASA, widget = forms.Select(attrs={'class': 'form-control','maxlength':'8'}))
    credito_infonavit = forms.ChoiceField(label = '¿Tiene crédito infonavit?', required = True, initial=1, choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))
    pago_infonavit = forms.CharField(label = 'Pago mensual',required = False,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'6','onkeypress':'return soloNumeros(event)'}))
    
    auto_propio = forms.ChoiceField(label = '¿Cuenta con automóvil?', required = True, initial=1, choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))
    auto_marca = forms.CharField(label = 'Marca del automóvil',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'20' }))
    auto_modelo = forms.CharField(label = 'Modelo del automóvil',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'20'}))
    
    seguro_vida = forms.ChoiceField(label = '¿Cuenta con seguro de vida?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))
    seguro_monto = forms.CharField(label = 'Monto del seguro de vida',required = False,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'10','onkeypress':'return soloNumeros(event)'}))     
    afianzado = forms.ChoiceField(label = '¿Ha sido afianzado?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))
    afianzado_monto = forms.CharField(label = 'Monto afianzado',required = False,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'10','onkeypress':'return soloNumeros(event)'}))     
    
    afiliado_sindicato = forms.ChoiceField(label = '¿Esta afiliado a algún sindicato?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))
    sindicato_nombre = forms.CharField(label = 'Nombre del sindicato',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' }))     
    sindicato_cargo = forms.CharField(label = 'Cargo en el sindicato',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' }))     
    
    tiempo_libre = forms.CharField(label = '¿A qué dedica su tiempo libre?',required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' }))     
    embarazo = forms.ChoiceField(label = '¿Está embarazada?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))
    religion = forms.CharField(label = 'Religión',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' })) 
    
    
    #estado_salud = forms.ChoiceField(label = 'Estado de salud', choices=ESTADO_SALUD,required = True, initial=1, widget = forms.Select(attrs={'class': 'form-control'}))
    estado_salud = forms.CharField(label = 'Estado de salud',required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'20' }))
    fuma = forms.ChoiceField(label = '¿Fuma?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    bebe = forms.ChoiceField(label = '¿Bebe?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    tatuajes = forms.ChoiceField(label = '¿Tiene tatuajes?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    perforaciones = forms.ChoiceField(label = '¿Tiene perforaciones?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    
    disposicion_rolar = forms.ChoiceField(label = '¿Dispuesto a rolar turnos?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))       
    disposicion_viajar = forms.ChoiceField(label = '¿Dispuesto a viajar?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    
    ingreso_extra = forms.ChoiceField(label = '¿Tiene otros ingresos?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    ingreso_monto = forms.CharField(label = 'Monto del ingreso extra',required = False,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'6','onkeypress':'return soloNumeros(event)'}))
    ingreso_fuente = forms.CharField(label = 'Fuente del ingreso extra',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' }))
    
    labora_conocido = forms.ChoiceField(label = '¿Labora un familiar o conocido con nosotros?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    conocido_nombre = forms.CharField(label = 'Nombre del familiar o conocido',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'180'  }))
    conocido_depto = forms.CharField(label = 'Departamento donde labora',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' }))
    fecha_disponible = forms.DateField(label = 'Fecha disponible para laborar',required = True, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'10','id':'fec_dis', 'placeholder': 'DD/MM/AAAA'}))
    
    def __init__(self, *args, **kwargs):

        super(Formulario_candidato, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required':'Ingrese {fieldname}'.format(
				fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
				fieldname=field.label), 'invalid':'Valor Inválido'.format(
				fieldname=field.label), 'min_length':'Acomplete el mínimo requerido {fieldname}'.format(
				fieldname=field.label)}


class Formulario_estudios(forms.Form):
    estudios_tipo = forms.ChoiceField(label = 'Tipo de estudio', required = True, initial=1, choices = TIPO_ESTUDIO,  widget = forms.Select(attrs={'class': 'form-control'}))
    estudios_escuela = forms.CharField(label = 'Lugar', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'100'}))
    estudios_nombre = forms.CharField(label = 'Estudio', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'50'}))
    estudios_annios = forms.CharField(label = 'Años', required = True, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))
    estudios_inicio = forms.DateField(label = 'Fecha de inicio',required = True, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control year','maxlength':'4'}))
    estudios_termino = forms.DateField(label = 'Fecha de término',required = True, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control year','maxlength':'4'}))
    estudios_documento = forms.ChoiceField(label = 'Documento recibido', required = True,initial=1, choices=TIPO_DOCU, widget = forms.Select(attrs={'class': 'form-control'}))
    estudios_tesis = forms.CharField(label = 'Nombre de tésis', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'50'}))
    estudios_forma = forms.CharField(label = 'Forma de titulación', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'50'}))
    estudios_cedula = forms.CharField(label = 'Número de cédula', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'8','onkeypress':'return soloNumeros(event)'}))
    

    def __init__(self, *args, **kwargs):
        super(Formulario_estudios, self).__init__(*args, **kwargs)

class Formulario_estudiosotros(forms.Form):
    estudios_tipo = forms.ChoiceField(label = 'Tipo de estudio', required = True, initial=1, choices = TIPO_OTROESTUDIO,  widget = forms.Select(attrs={'class': 'form-control'}))
    estudios_nombre = forms.CharField(label = 'Estudio', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'50'}))
    estudios_inicio = forms.DateField(label = 'Fecha de inicio',required = True, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control year','maxlength':'4'}))
    estudios_termino = forms.DateField(label = 'Fecha de término',required = True, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control year','maxlength':'4'}))
    estudios_documento = forms.ChoiceField(label = 'Documento recibido', required = True,initial=1, choices=TIPO_DOCU, widget = forms.Select(attrs={'class': 'form-control'}))
    

    def __init__(self, *args, **kwargs):
        super(Formulario_estudiosotros, self).__init__(*args, **kwargs)

class Formulario_idioma(forms.Form):
    idioma = forms.CharField(label = 'Idioma',required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    idioma_porcentaje = forms.CharField(label = 'Porcentaje',required = True,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'3','onkeypress':'return soloNumeros(event)'}))
    
    def __init__(self, *args, **kwargs):
        super(Formulario_idioma, self).__init__(*args, **kwargs)
        

class Formulario_referencia(forms.Form):
    referencia_nombre = forms.CharField(label = 'Nombre de contacto(no incluir parientes)',required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'100' }))
    referencia_domicilio = forms.CharField(label = 'Domicilio de la referencia',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'200'}))
    referencia_tel = forms.CharField(label = 'Teléfono',required = False, widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)'}))
    referencia_ocupacion = forms.CharField(label = 'Ocupación',required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'100' }))
    referencia_annios_conocer = forms.CharField(label = 'Años de conocerlo',required = True,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))

    def __init__(self, *args, **kwargs):
        super(Formulario_referencia, self).__init__(*args, **kwargs)
        
        
        
    

class Formulario_hermano_candidato(forms.Form):
    hermano_nombre = forms.CharField(label = 'Nombre',required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'120' }))
    hermano_apellido_paterno = forms.CharField(label = 'Apellido paterno',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    hermano_apellido_materno = forms.CharField(label = 'Apellido materno',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    hermano_edad = forms.CharField(label = 'Edad',required = False,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))
    hermano_ocupacion = forms.CharField(label = 'Ocupación',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    hermano_lugar_ocupacion = forms.CharField(label = 'Lugar de trabajo o escuela',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    hermano_domicilio = forms.CharField(label = 'Domicilio',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'200'}))
    hermano_tel = forms.CharField(label = 'Teléfono o celular',required = False, widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)'}))

    def __init__(self, *args, **kwargs):
        super(Formulario_hermano_candidato, self).__init__(*args, **kwargs)
    

class Formulario_hijo_candidato(forms.Form):
    hijo_nombre = forms.CharField(label = 'Nombre(s)',required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'120' }))
    hijo_apellido_paterno = forms.CharField(label = 'Apellido paterno',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    hijo_apellido_materno = forms.CharField(label = 'Apellido materno',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    hijo_edad = forms.CharField(label = 'Edad',required = False,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))
    hijo_ocupacion = forms.CharField(label = 'Ocupación',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    hijo_lugar_ocupacion = forms.CharField(label = 'Lugar de trabajo o escuela',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    hijo_domicilio = forms.CharField(label = 'Domicilio',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'200'}))
    hijo_tel = forms.CharField(label = 'Teléfono o celular',required = False, widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)'}))

    def __init__(self, *args, **kwargs):
        super(Formulario_hijo_candidato, self).__init__(*args, **kwargs)
        
       


class Formulario_experiencia(forms.Form):
    empresa_nombre = forms.CharField(label = 'Empresa actual o última',required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'100' }))
    empresa_direccion = forms.CharField(label = 'Dirección',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'100'}))
    empresa_tel = forms.CharField(label = 'Teléfono',required = False, widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)'}))     
    
    empresa_giro = forms.CharField(label = 'Giro',required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'100' }))
    empresa_nombre_jefe = forms.CharField(label = 'Nombre del jefe inmediato',required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'100' }))
    empresa_jefe_puesto = forms.CharField(label = 'Puesto del jefe inmediato',required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'100' }))
    
    empresa_fecha_ingreso = forms.DateField(label = 'Fecha de ingreso en la empresa',required = True, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'10', 'placeholder': 'DD/MM/AAAA'}))
    empresa_salario_inicio = forms.CharField(label = 'Salario inicial',required = True,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'6','onkeypress':'return soloNumeros(event)'}))
    empresa_fecha_separacion = forms.DateField(label = 'Fecha de separación de la empresa',required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'10', 'placeholder': 'DD/MM/AAAA'}))
    empresa_salario_final = forms.CharField(label = 'Salario final',required = True,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'6','onkeypress':'return soloNumeros(event)'}))
    
    empresa_puesto_ultimo = forms.CharField(label = 'Último puesto desempeñado',required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' }))
    empresa_puesto_ultimo_tiempo = forms.CharField(label = 'Tiempo del ultimo puesto',required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'20'}))
    empresa_puesto_ultimo_depto = forms.CharField(label = 'Departamento del último puesto desempeñado',required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' }))
    
    empresa_puesto_anterior = forms.CharField(label = 'Anterior puesto desempeñado',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' }))
    empresa_puesto_anterior_tiempo = forms.CharField(label = 'Tiempo del anterior puesto',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'20'}))
    empresa_puesto_anterior_depto = forms.CharField(label = 'Departamento del anterior puesto desempeñado',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' }))
    
    experiencia_supervision = forms.ChoiceField(label = '¿Tiene experiencia en supervisión?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    empresa_actual = forms.ChoiceField(label = '¿Empresa actual?', required = True,initial="Si",choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    
    experiencia_supervision_num = forms.CharField(label = 'Número de personas que superviso',required = True,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'3','onkeypress':'return soloNumeros(event)'}))
    separacion_motivo = forms.CharField(label = '¿Cuál fué el motivo de la separación?',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'100' }))

    def __init__(self, *args, **kwargs):
        super(Formulario_experiencia, self).__init__(*args, **kwargs)



class Cand_docsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Cand_docsForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
            self.fields[campos].required = False
        
    class Meta:
        model = Cand_docs
        fields = ('INE','Acta','CURP', 'RFC', 'Comp_dom','Comp_grado',
                  'Comp_cursos','Comp_permiso','IMSS','Cartas','Esdo_cuenta',
                  'Esdo_info','Lic_manejo','Observaciones')

class Formulario_est_comp(forms.Form):
    comprobante = forms.FileField(label='Comprobante', required = False)
    
    def __init__(self, *args, **kwargs):
        super(Formulario_est_comp, self).__init__(*args, **kwargs)

class Formulario_cand_docs(forms.Form):
    #INE = forms.ChoiceField(label = 'INE', required = False, choices=bol, initial=false, widget = forms.CheckboxInput())
    #personal de base
    curriculum = forms.FileField(label='Curriculum', required = False)
    INE_frente = forms.FileField(label='Frente', required = False)
    INE_atras = forms.FileField(label='Atrás', required = False)
    acta = forms.FileField(label='Acta de nacimiento', required = False)
    curp = forms.FileField(label='CURP', required = False)
    rfc = forms.FileField(label='RFC', required = False)
    comprobante_domicilio = forms.FileField(label='Comprobante', required = False)
    imss = forms.FileField(label='IMSS', required = False)
    carta1 = forms.FileField(label='Carta de reco.', required = False)
    carta2 = forms.FileField(label='Carta de reco.', required = False)
    contrato = forms.FileField(label='Contrato', required = False)
    infonavit = forms.FileField(label='Infonavit/Infonacot', required = False)

    #extranjero
    permiso = forms.FileField(label='Permiso de trabajo', required = False)
    
    #becarios
    oficio = forms.FileField(label='Oficio expedido por la institución', required = False)
    #menores
    carta_menor = forms.FileField(label='Carta de permiso para laborar', required = False)
    INE_frenteTut = forms.FileField(label='Frente', required = False)
    INE_atrasTut = forms.FileField(label='Atrás', required = False)
    #lic_frente = forms.FileField(label='Frente', required = False)
    #lic_atras= forms.FileField(label='Atrás', required = False)


    #Acta = forms.ChoiceField(label = 'Acta de nacimiento', required = False, choices=bol, initial=false, widget = forms.CheckboxInput())
    
    #CURP = forms.ChoiceField(label = 'CURP', required = False, choices=bol, initial=false, widget = forms.CheckboxInput())
    
    #RFC = forms.ChoiceField(label = 'RFC', required = False, choices=bol, initial=false, widget = forms.CheckboxInput())
    
    #Comp_dom = forms.ChoiceField(label = 'Comprobante de domicilio', required = False, choices=bol, initial=false, widget = forms.CheckboxInput())
    #Comp_grado = forms.ChoiceField(label = 'Comprobante de último grado', required = False, choices=bol, initial=false, widget = forms.CheckboxInput())
    #Comp_cursos = forms.ChoiceField(label = 'Comprobantes de cursos, certificaciones, etc.', required = False, choices=bol, initial=false, widget = forms.CheckboxInput())
    #Comp_permiso = forms.ChoiceField(label = 'Comprobante de permiso laboral(solo extranjero)', required = False, choices=bol, initial=false, widget = forms.CheckboxInput())
    #IMSS = forms.ChoiceField(label = 'Afiliación al IMSS', required = False, choices=bol, initial=false, widget = forms.CheckboxInput())
    
    #Cartas = forms.ChoiceField(label = 'Cartas de recomendación', required = False, choices=bol, initial=false, widget = forms.CheckboxInput())
    #Esdo_cuenta = forms.ChoiceField(label = 'Esdo. cuenta bancario, tarjeta y CLABE', required = False, choices=bol, initial=false, widget = forms.CheckboxInput())
    #Esdo_info = forms.ChoiceField(label = 'Esdo. cuenta Infonacot/infonavit', required = False, choices=bol, initial=false, widget = forms.CheckboxInput())
    
    #Lic_manejo = forms.ChoiceField(label = 'Lic. de manejo', required = False, choices=bol, initial=false, widget = forms.CheckboxInput())
    
    #Observaciones = forms.CharField(label = 'Observaciones', required = False, widget = forms.Textarea(attrs={'class': 'form-control sololetrasynumeros','cols':'20','rows':'4','maxlength':'200'}))
    
    
    def __init__(self, *args, **kwargs):
        super(Formulario_cand_docs, self).__init__(*args, **kwargs)


###########COLABORADOR
class FormularioCol_candidato(forms.Form):
    #sección 1(datos personales)
    #con_id = forms.HiddenInput()
    ######### CAMPOS AGREGADOS
    tipo_documento_identidad = forms.ModelChoiceField(label = 'Tipo de identificación', queryset=TipoDocumentoIdentidad.objects.all(), required=True, initial=1, widget = forms.Select(attrs={'class': 'form-control'}))
    ##Imagenes
    imagen_curp = forms.FileField(label='IMG/PDF de curp', required = True)
    imagen_rfc = forms.FileField(label='IMG/PDF de rfc', required = True)
    imagen_imss = forms.FileField(label='IMG/PDF de imss', required = True)
    img_lic_anverso = forms.FileField(label='IMG/PDF de Licencia Frente', required = False)
    img_lic_reverso= forms.FileField(label='IMG/PDF de Licencia Atrás', required = False)
    docu_ident_front = forms.FileField(label='IMG/PDF de INE frente', required = True)
    docu_ident_back = forms.FileField(label='IMG/PDF de INE atrás', required = True)
    imagen_cartilla = forms.FileField(label='IMG/PDF de cartilla', required = False)

    ########
    con_id = forms.CharField(label='reset', max_length=20, widget=forms.HiddenInput())
    fecha_solicitud = forms.DateField(label = 'Fecha_solicitud',required = True, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
    fuente_recluta = forms.CharField(label = 'Fuente de reclutamiento', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'100'}))
    puesto_solicitado = forms.CharField(label = 'Puesto solicitado', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'100'}))
    sueldo_deseado = forms.CharField(label = 'Sueldo deseado', required = True, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'6','onkeypress':'return soloNumeros(event)'}))
    nombre = forms.CharField(label = 'Nombre', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    apellido_paterno = forms.CharField(label = 'Apellido paterno', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    apellido_materno = forms.CharField(label = 'Apellido materno', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    
    sexo = forms.ChoiceField(label = 'Sexo', required = True,initial=1,choices = SEXO, widget = forms.Select(attrs={'class': 'form-control'}))
    estado_civil = forms.ChoiceField(label = 'Estado civil', choices=ESTADO_CIVIL,required = True, initial=Soltero, widget = forms.Select(attrs={'class': 'form-control'}))
    edad = forms.IntegerField(label = 'Edad', required = True, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','MAX':'90','onkeypress':'return soloNumeros(event)'}))
    fecha_nac = forms.DateField(label = 'Fecha de nacimiento', required = True,input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'10', 'placeholder': 'DD/MM/AAAA'}))
    lugar_nac = forms.CharField(label = 'Lugar de nacimiento', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    pais_nacimiento = forms.ModelChoiceField(label = 'País de nacimiento', required = True, queryset=Country.objects.all().order_by('pais'), initial=1,  widget = forms.Select(attrs={'class': 'form-control'}))
    
    tel = forms.CharField(label = 'Teléfono de casa', required = False,widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)'}))
    cel = forms.CharField(label = 'Celular', required = True,widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)'}))
    tipo = forms.ChoiceField(label = 'Tipo de casa habitación', required = True, initial=1, choices = TIPO_HABITACION,  widget = forms.Select(attrs={'class': 'form-control'}))
    
    calle = forms.CharField(label = 'Calle', required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'60'}))
    num_ext = forms.CharField(label = '#Exterior', required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'7'}))
    num_int = forms.CharField(label = '#Interior',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'7'}))
    calle_uno = forms.CharField(label = 'Entre', required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'60'}))
    
    calle_dos = forms.CharField(label = 'Y calle',required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'60'}))
    piso = forms.CharField(label = 'Piso',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'6'}))
    depto = forms.CharField(label = 'Departamento',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'6'}))
    cp = forms.CharField(label = 'CP', required = True, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'5', 'data-mask': '99999','onkeypress':'return soloNumeros(event)'}))
    
    colonia = forms.CharField(label = 'Colonia o fraccionamiento',required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'60'}))
    esdo = forms.ChoiceField(label = 'Estado', required = True, initial=1, choices = STATUS_CHOICES,  widget = forms.Select(attrs={'class': 'form-control'}))
    pais_direc = forms.ModelChoiceField(label = 'País', required = True, queryset=Country.objects.all().order_by('pais'), initial=6,  widget = forms.Select(attrs={'class': 'form-control'}))
    
    referencia = forms.CharField(label = 'Referencia',required = True, widget = forms.Textarea(attrs={'class': 'form-control sololetrasynumeros','cols':'40','rows':'3','maxlength':'200'}))
    trayectoria_de_casa = forms.CharField(label = 'Tiempo de trayectoria desde casa',required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'60'}))
    #trayectoria_de_casa = forms.ChoiceField(label = 'Tiempo de trayectoria desde casa', choices=TIEMPO_TRAYECTO,required = True, initial=1, widget = forms.Select(attrs={'class': 'form-control'}))
    email_personal = forms.EmailField(label = "Correo personal", required = False, widget = forms.TextInput(attrs={'class': 'form-control' }))
    
    rfc = forms.CharField(label = 'RFC', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'15'}))
    curp = forms.CharField(label = 'CURP', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'18'}))
    imss = forms.CharField(label = 'IMSS', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'11','onkeypress':'return soloNumeros(event)'}))
    cartilla = forms.CharField(label = 'Cartilla', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'10','onkeypress':'return soloNumeros(event)'}))
    #tipo_licencia = forms.CharField(label = 'Tipo de licencia', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'20'}))
    tipo_licencia = forms.ChoiceField(label = 'Tipo de licencia', choices=TIPO_LICENCIA,required = True, initial=5, widget = forms.Select(attrs={'class': 'form-control sololetras'}))
    licencia = forms.CharField(label = 'Número de licencia', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'12','onkeypress':'return soloNumeros(event)'}))
    
    #sección 2(antecedentes académicos)
    primaria = forms.CharField(label = 'Primaria', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'100'}))
    #primaria_domicilio = forms.CharField(label = 'Dirección', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'200'}))
    primaria_annios = forms.CharField(label = 'Años', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))
  
    primaria_inicio = forms.DateField(label = 'Fecha de inicio',required = False, input_formats=settings.YEAR_FORMAT, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'4'}))
    primaria_termino = forms.DateField(label = 'Fecha de término',required = False, input_formats=settings.YEAR_FORMAT, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'4'}))
    primaria_documento = forms.ChoiceField(label = 'Documento recibido', required = False,initial=0, choices=TIPO_DOCU, widget = forms.Select(attrs={'class': 'form-control'}))
    
    secundaria = forms.CharField(label = 'Secundaria', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'100'}))
    #secundaria_domicilio = forms.CharField(label = 'Dirección', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'200'}))
    secundaria_annios = forms.CharField(label = 'Años', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))
    secundaria_inicio = forms.DateField(label = 'Fecha de inicio',required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'4'}))
    secundaria_termino = forms.DateField(label = 'Fecha de término',required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'4'}))
    #secundaria_documento = forms.CharField(label = 'Documento recibido', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'50' }))
    secundaria_documento = forms.ChoiceField(label = 'Documento recibido', required = False,initial=0, choices=TIPO_DOCU, widget = forms.Select(attrs={'class': 'form-control'}))
    
    preparatoria = forms.CharField(label = 'Preparatoria', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'100'}))
    #preparatoria_domicilio = forms.CharField(label = 'Dirección', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'200'}))
    preparatoria_annios = forms.CharField(label = 'Años', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))
    preparatoria_inicio = forms.DateField(label = 'Fecha de inicio',required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'4'}))
    preparatoria_termino = forms.DateField(label = 'Fecha de término',required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'4'}))
    #preparatoria_documento = forms.CharField(label = 'Documento recibido', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'50' }))
    preparatoria_documento = forms.ChoiceField(label = 'Documento recibido', required = False,initial=0, choices=TIPO_DOCU, widget = forms.Select(attrs={'class': 'form-control'}))
    
    tecnica = forms.CharField(label = 'Técnica', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'100','onkeypress':'return soloLetrasyNumeros(event)'}))
    #tecnica_domicilio = forms.CharField(label = 'Dirección', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'200'}))
    tecnica_annios = forms.CharField(label = 'Años', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'2'}))
    tecnica_inicio = forms.DateField(label = 'Fecha de inicio',required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'4'}))
    tecnica_termino = forms.DateField(label = 'Fecha de término',required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'4'}))
    #tecnica_documento = forms.CharField(label = 'Documento recibido', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'50' }))
    tecnica_documento = forms.ChoiceField(label = 'Documento recibido', required = False,initial=0, choices=TIPO_DOCU, widget = forms.Select(attrs={'class': 'form-control'}))
    
    estudia_actualmente = forms.ChoiceField(label = '¿Estudia actualmente?', required = False, initial=1, choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))
    estudia_que = forms.CharField(label = '¿Qué estudia?', required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'60' }))
    estudia_donde = forms.CharField(label = '¿Dónde estudia?', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'60'}))
    estudia_horario = forms.CharField(label = 'Horario', required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'20'}))
    estudia_termino = forms.DateField(label = 'Fecha de termino',required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'10','id':'fec_ter', 'placeholder': 'DD/MM/AAAA'}))
    maquinas_equipos = forms.CharField(label = 'Máquinas o equipos que maneja', required = False, widget = forms.Textarea(attrs={'class': 'form-control sololetrasynumeros','maxlength':'200'}))

    #sección 3(datos familiares, padre, madre, conyuge)

    padre_nombre = forms.CharField(label = 'Nombre del padre',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    padre_apellido_paterno = forms.CharField(label = 'Apellido paterno',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    padre_apellido_materno = forms.CharField(label = 'Apellido materno',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    padre_edad = forms.CharField(label = 'Edad',required = False, widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))
    
    padre_ocupacion = forms.CharField(label = 'Ocupación',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    padre_lugar_trabajo = forms.CharField(label = 'Lugar de trabajo',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    padre_domicilio = forms.CharField(label = 'Domicilio',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'200'}))
    padre_tel = forms.CharField(label = 'Teléfono o celular',required = False, widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)'}))
    padre_vive = forms.ChoiceField(label = '', required = False, initial=1, choices = TIPO_VIVE, widget = forms.Select(attrs={'class': 'form-control'}))
    
    madre_nombre = forms.CharField(label = 'Nombre de la madre',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    madre_apellido_paterno = forms.CharField(label = 'Apellido paterno',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    madre_apellido_materno = forms.CharField(label = 'Apellido materno',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    madre_edad = forms.CharField(label = 'Edad',required = False,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))
    madre_ocupacion = forms.CharField(label = 'Ocupación',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    madre_lugar_trabajo = forms.CharField(label = 'Lugar de trabajo',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    madre_domicilio = forms.CharField(label = 'Domicilio',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'200'}))
    madre_tel = forms.CharField(label = 'Teléfono o celular',required = False, widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)'}))
    madre_vive = forms.ChoiceField(label = '', required = True, initial=1, choices = TIPO_VIVE, widget = forms.Select(attrs={'class': 'form-control'}))
    
    conyuge_nombre = forms.CharField(label = 'Nombre del conyuge',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    conyuge_apellido_paterno = forms.CharField(label = 'Apellido paterno',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    conyuge_apellido_materno = forms.CharField(label = 'Apellido materno',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    conyuge_edad = forms.CharField(label = 'Edad',required = False,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'2','onkeypress':'return soloNumeros(event)'}))
    conyuge_ocupacion = forms.CharField(label = 'Ocupación',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    conyuge_lugar_trabajo = forms.CharField(label = 'Lugar de trabajo',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'60' }))
    conyuge_domicilio = forms.CharField(label = 'Domicilio',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'200'}))
    conyuge_tel = forms.CharField(label = 'Teléfono o celular',required = False, widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)'}))
    conyuge_vive = forms.ChoiceField(label = '', required = True, initial=1, choices = TIPO_VIVE, widget = forms.Select(attrs={'class': 'form-control'}))
    hijos = forms.ChoiceField(label = '¿Tiene hijos?', required = True, choices=SI_NO, initial="No", widget = forms.RadioSelect(attrs={}))
    hermanos = forms.ChoiceField(label = '¿Tiene hermanos?', required = True, choices=SI_NO, initial="No", widget = forms.RadioSelect(attrs={}))


    #sección 4(datos generales)
    vivienda_propia = forms.ChoiceField(label = 'Vive en casa', required = True, initial=1, choices = VIVE_EN_CASA, widget = forms.Select(attrs={'class': 'form-control','maxlength':'8'}))
    credito_infonavit = forms.ChoiceField(label = '¿Tiene crédito infonavit?', required = True, initial=1, choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))
    pago_infonavit = forms.CharField(label = 'Pago mensual',required = False,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'6','onkeypress':'return soloNumeros(event)'}))
    
    auto_propio = forms.ChoiceField(label = '¿Cuenta con automóvil?', required = True, initial=1, choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))
    auto_marca = forms.CharField(label = 'Marca del automóvil',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'20' }))
    auto_modelo = forms.CharField(label = 'Modelo del automóvil',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'20'}))
    
    seguro_vida = forms.ChoiceField(label = '¿Cuenta con seguro de vida?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))
    seguro_monto = forms.CharField(label = 'Monto del seguro de vida',required = False,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'10','onkeypress':'return soloNumeros(event)'}))     
    afianzado = forms.ChoiceField(label = '¿Ha sido afianzado?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))
    afianzado_monto = forms.CharField(label = 'Monto afianzado',required = False,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'10','onkeypress':'return soloNumeros(event)'}))     
    
    afiliado_sindicato = forms.ChoiceField(label = '¿Esta afiliado a algún sindicato?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))
    sindicato_nombre = forms.CharField(label = 'Nombre del sindicato',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' }))     
    sindicato_cargo = forms.CharField(label = 'Cargo en el sindicato',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' }))     
    
    tiempo_libre = forms.CharField(label = '¿A qué dedica su tiempo libre?',required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' }))     
    embarazo = forms.ChoiceField(label = '¿Está embarazada?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))
    religion = forms.CharField(label = 'Religión',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' })) 
    
    
    #estado_salud = forms.ChoiceField(label = 'Estado de salud', choices=ESTADO_SALUD,required = True, initial=1, widget = forms.Select(attrs={'class': 'form-control'}))
    estado_salud = forms.CharField(label = 'Estado de salud',required = True,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'20' }))
    fuma = forms.ChoiceField(label = '¿Fuma?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    bebe = forms.ChoiceField(label = '¿Bebe?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    tatuajes = forms.ChoiceField(label = '¿Tiene tatuajes?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    perforaciones = forms.ChoiceField(label = '¿Tiene perforaciones?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    
    disposicion_rolar = forms.ChoiceField(label = '¿Dispuesto a rolar turnos?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))       
    disposicion_viajar = forms.ChoiceField(label = '¿Dispuesto a viajar?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    
    ingreso_extra = forms.ChoiceField(label = '¿Tiene otros ingresos?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    ingreso_monto = forms.CharField(label = 'Monto del ingreso extra',required = False,widget = forms.TextInput(attrs={'class': 'form-control','maxlength':'6','onkeypress':'return soloNumeros(event)'}))
    ingreso_fuente = forms.CharField(label = 'Fuente del ingreso extra',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' }))
    
    labora_conocido = forms.ChoiceField(label = '¿Labora un familiar o conocido con nosotros?', required = True,initial=1,choices = SI_NO, widget = forms.Select(attrs={'class': 'form-control','maxlength':'2'}))    
    conocido_nombre = forms.CharField(label = 'Nombre del familiar o conocido',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'180'  }))
    conocido_depto = forms.CharField(label = 'Departamento donde labora',required = False,widget = forms.TextInput(attrs={'class': 'form-control sololetras','maxlength':'50' }))
    fecha_disponible = forms.DateField(label = 'Fecha disponible para laborar',required = True, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'10','id':'fec_dis', 'placeholder': 'DD/MM/AAAA'}))
    
    def __init__(self, *args, **kwargs):

        super(FormularioCol_candidato, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required':'Ingrese {fieldname}'.format(
				fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
				fieldname=field.label), 'invalid':'Valor Inválido'.format(
				fieldname=field.label), 'min_length':'Acomplete el mínimo requerido {fieldname}'.format(
				fieldname=field.label)}