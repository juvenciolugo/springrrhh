#-*- coding: utf-8 -*-
from django import forms
from empleados.models import *
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
 
years_to_display = range(datetime.datetime.now().year - 100, datetime.datetime.now().year + 1) 

class ExtensionValidator(RegexValidator):
    def __init__(self, extensions, message=None):
        print("entro1")
        if not hasattr(extensions,'__iter__'):
            extensions = [extensions]
        regex ='\.(%s)$' % '|'.join(extensions)
        if message is None:
            message='Archivo no soportado. Tipos aceptados: %s.' % ', '.join(extensions)
        super(ExtensionValidator, self).__init__(regex, message)

    def _call__(self, value):
        print("entro2")
        super(ExtensionValidator, self).__call__(value.name)

def validate_file_extension(value):
    import os 
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['jpg','bmp','png']
    if not ext in valid_extensions:
        raise ValidationError(u'Archivo no soportado')


class Formulario1(forms.Form):
    nombre = forms.CharField(label = 'nombre', required = True, widget = forms.TextInput(attrs={'class': 'form-control soloLetras','maxlength':'60'}))
    apellido_paterno = forms.CharField(label = 'apellido_paterno', required = True, widget = forms.TextInput(attrs={'class': 'form-control soloLetras','maxlength':'60'}))
    apellido_materno = forms.CharField(label = 'apellido_materno', required = True, widget = forms.TextInput(attrs={'class': 'form-control soloLetras','maxlength':'60'}))
    fecha_nacimiento = forms.DateField(label = 'fecha_nacimiento', input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
    pais_nacimiento = forms.ModelChoiceField(label = 'pais_nacimiento', required = True, queryset=Country.objects.all().order_by('pais'), initial=1,  widget = forms.Select(attrs={'class': 'form-control'}))
    nacionalidad = forms.ModelMultipleChoiceField(label = 'nacionalidad', required = False, queryset=Country.objects.all().order_by('pais'), widget = forms.SelectMultiple(attrs={'class': 'chosen-select', 'data-placeholder':'Seleccione los paises de los cuales posee nacionalidad', 'multiple style':'width:350px'}))
    edad = forms.IntegerField(label = 'edad', required = True, widget = forms.TextInput(attrs={'class': 'touchspin1 soloNumeros', 'name':'demo1','maxlength':'3'}))
    foto = forms.ImageField(label='foto', required = True)
    #foto = forms.FileField(label='foto', required = True, validators=[validate_file_extension])
    acta_nacimiento = forms.FileField(label='acta_nacimiento', required = True)
    #direccion = forms.CharField(label = 'dirección', widget = forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
    tipo = forms.ChoiceField(label = 'tipo_de_habitacion', required = True, initial=1, choices = TIPO_HABITACION,  widget = forms.Select(attrs={'class': 'form-control'}))
    calle = forms.CharField(label = 'dirección', widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'100'}))
    num_ext = forms.CharField(label = 'numero_exterior', widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'7'}))
    num_int = forms.CharField(label = 'numero_interior',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'7'}))
    calle_uno = forms.CharField(label = 'entre_calle', widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'100'}))
    calle_dos = forms.CharField(label = 'y_calle', widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'100'}))
    piso = forms.CharField(label = 'piso',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'6'}))
    depto = forms.CharField(label = 'depto',required = False, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'60'}))
    cp = forms.IntegerField(label = 'CP', required = True, widget = forms.NumberInput(attrs={'class': 'form-control soloNumeros','maxlength':'5'}))
    colonia = forms.CharField(label = 'colonia_fraccionamiento', widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','maxlength':'60'}))
    esdo = forms.ChoiceField(label = 'estado_de_direccion', required = True, initial=1, choices = STATUS_CHOICES,  widget = forms.Select(attrs={'class': 'form-control'}))
    pais_direc = forms.ModelChoiceField(label = 'pais_direccion', required = True, queryset=Country.objects.all().order_by('pais'), initial='MÉXICO',  widget = forms.Select(attrs={'class': 'form-control'}))
    referencia = forms.CharField(label = 'Referencia', widget = forms.Textarea(attrs={'class': 'form-control sololetrasynumeros','cols':'40','rows':'3','maxlength':'100'}))
    tel = forms.CharField(label = 'tlf', widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)'}))
    cel = forms.CharField(label = 'cel', widget = forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(999) (999-9999)'}))
    email_personal = forms.EmailField(label = "email_personal", required = True, widget = forms.TextInput(attrs={'class': 'form-control' ,'maxlength':'60'}))
    tipo_documento_identidad = forms.ModelChoiceField(label = 'tipo_documento_identidad', queryset=TipoDocumentoIdentidad.objects.all(), required=True, initial=1, widget = forms.Select(attrs={'class': 'form-control'}))
    docu_ident_front = forms.FileField(label='documento_identidad_front', required = True)
    docu_ident_back = forms.FileField(label='documento_identidad_back', required = True)
    pasaporte = forms.IntegerField(label = 'pasaporte', required = False, widget = forms.TextInput(attrs={'class': 'form-control soloNumeros','maxlength':'6'}))
    fecha_vencimiento_pasaporte = forms.DateField(label = 'fecha_vencimiento_pasaporte', required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
    imagen_pasaporte = forms.FileField(label='imagen_pasaporte', required = False)

    def __init__(self, *args, **kwargs):
        super(Formulario1, self).__init__(*args, **kwargs)
        # Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
        for field in self.fields.values():
            field.error_messages = {'required':'Ingrese {fieldname}'.format(
                fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
                fieldname=field.label), 'invalid':'Valor Inválido'.format(
                fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
                fieldname=field.label)}

class Formulario_etapa_2(forms.Form):
    visa_1 = forms.ModelChoiceField(label = 'visa_1', required = False, queryset=Country.objects.all().order_by('pais'),  widget = forms.Select(attrs={'class': 'form-control'}))
    visa_2 = forms.ModelChoiceField(label = 'visa_2', required = False, queryset=Country.objects.all().order_by('pais'),  widget = forms.Select(attrs={'class': 'form-control'}))
    visa_3 = forms.ModelChoiceField(label = 'visa_3', required = False, queryset=Country.objects.all().order_by('pais'),  widget = forms.Select(attrs={'class': 'form-control'}))
    visa_4 = forms.ModelChoiceField(label = 'visa_4', required = False, queryset=Country.objects.all().order_by('pais'),  widget = forms.Select(attrs={'class': 'form-control'}))
    visa_5 = forms.ModelChoiceField(label = 'visa_5', required = False, queryset=Country.objects.all().order_by('pais'),  widget = forms.Select(attrs={'class': 'form-control'}))
    vigencia_visa_1 = forms.DateField(label = 'vigencia_visa_1', required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control fechas_visa', 'placeholder': 'DD/MM/AA'}))
    vigencia_visa_2 = forms.DateField(label = 'vigencia_visa_2', required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control fechas_visa', 'placeholder': 'DD/MM/AA'}))
    vigencia_visa_3 = forms.DateField(label = 'vigencia_visa_3', required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control fechas_visa', 'placeholder': 'DD/MM/AA'}))
    vigencia_visa_4 = forms.DateField(label = 'vigencia_visa_4', required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control fechas_visa', 'placeholder': 'DD/MM/AA'}))
    vigencia_visa_5 = forms.DateField(label = 'vigencia_visa_5', required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control fechas_visa', 'placeholder': 'DD/MM/AA'}))
    img_visa_1 = forms.FileField(label='img_visa_1', required = False)
    img_visa_2 = forms.FileField(label='img_visa_2', required = False)
    img_visa_3 = forms.FileField(label='img_visa_3', required = False)
    img_visa_4 = forms.FileField(label='img_visa_4', required = False)
    img_visa_5 = forms.FileField(label='img_visa_5', required = False)
    #attrs={'style': 'text-transform:lowercase;'}
    curp = forms.CharField(label = 'curp', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','style':'text-transform:uppercase'}))
    imagen_curp = forms.FileField(label='imagen_curp', required = True)
    rfc = forms.CharField(label = 'rfc', required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros','style':'text-transform:uppercase'}))
    imagen_rfc = forms.FileField(label='imagen_rfc', required = True)
    sat = forms.CharField(label = 'sat', required = True, widget = forms.TextInput(attrs={'class': 'form-control soloNumeros'}))
    imagen_sat = forms.FileField(label='imagen_sat', required = True)
    infonavit = forms.CharField(label = 'infonavit', required = True, widget = forms.TextInput(attrs={'class': 'form-control soloNumeros','data-mask': '9999999999'}))
    imagen_infonavit = forms.FileField(label='imagen_infonavit', required = True)
    imss = forms.IntegerField(label = 'imss', required = True, widget = forms.TextInput(attrs={'class': 'form-control soloNumeros','data-mask': '99999999999'}))
    imagen_imss = forms.FileField(label='imagen_imss', required = True)
    licencia_conducir = forms.CharField(label = 'licencia_conducir', required = False, widget = forms.TextInput(attrs={'class': 'form-control soloNumeros'}))
    vigencia_licencia_conducir = forms.DateField(label = 'vigencia_licencia_conducir', required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
    estado_emision_licencia = forms.ChoiceField(label = 'estado_emision_licencia', required = False, initial=1, choices = STATUS_CHOICES,  widget = forms.Select(attrs={'class': 'form-control'}))
    permanente = forms.BooleanField(label = 'permanente',required=False, initial = False, widget = forms.RadioSelect(choices=[(True, 'Si'),(False, 'No')],attrs={'class': 'radio-info'}))
    img_lic_anverso = forms.FileField(label='img_lic_anverso', required = False)
    img_lic_reverso= forms.FileField(label='img_lic_reverso', required = False)
    def __init__(self, *args, **kwargs):
        super(Formulario_etapa_2, self).__init__(*args, **kwargs)
        # Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
        for field in self.fields.values():
            field.error_messages = {'required':'Ingrese {fieldname}'.format(
                fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
                fieldname=field.label), 'invalid':'Valor Inválido'.format(
                fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
                fieldname=field.label)}

class FormConyugue(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormConyugue, self).__init__(*args, **kwargs)
        # change a widget attribute: ,'maxlength':'60','onkeypress':'return soloLetras(event)'
        self.fields['acta'].widget.attrs["class"] = 'form-control'
        self.fields['acta_nacimiento'].widget.attrs["class"] = 'form-control'
        self.fields['nombre'].widget.attrs["class"] = 'form-control soloLetras'
        self.fields['nombre'].widget.attrs["maxlength"] = '60'
        #self.fields['nombre'].widget.attrs["onkeypress"] = 'return soloLetras(event)'
        self.fields['apellido_paterno'].widget.attrs["class"] = 'form-control soloLetras'
        self.fields['apellido_paterno'].widget.attrs["maxlength"] = '60'
        #self.fields['apellido_paterno'].widget.attrs["onkeypress"] = 'return soloLetras(event)'
        self.fields['apellido_materno'].widget.attrs["class"] = 'form-control soloLetras'
        self.fields['apellido_materno'].widget.attrs["maxlength"] = '60'
        #self.fields['apellido_materno'].widget.attrs["onkeypress"] = 'return soloLetras(event)'
        self.fields['fecha_nacimiento'].widget.attrs["class"] = 'form-control'
        self.fields['fecha_nacimiento'].widget.initial = timezone.now()
        self.fields['profesion'].widget.attrs["class"] = 'form-control soloLetras'
        self.fields['profesion'].widget.attrs["maxlength"] = '60'
        self.fields['tlf'].widget.attrs["class"] = 'form-control soloNumeros'
        self.fields['tlf'].widget.attrs["data-mask"] = '(99) 9999-9999)'
        self.fields['tlf'].widget.attrs["maxlength"] = '15'
        
        self.fields['email'].widget.attrs["class"] = 'form-control emailconyu'
        self.fields['tlf'].widget.attrs["maxlength"] = '15'
        self.fields['lugar_de_trabajo'].widget.attrs["class"] = 'form-control sololetrasynumeros'
        self.fields['lugar_de_trabajo'].widget.attrs["maxlength"] = '200'
        self.fields['email_trabajo'].widget.attrs["class"] = 'form-control emailconyu'
        self.fields['email_trabajo'].widget.attrs["maxlength"] = '60'
        # REQUIRED
        self.fields['acta'].required = False
        self.fields['acta_nacimiento'].required = False
        self.fields['nombre'].required = False
        self.fields['apellido_paterno'].required = False
        self.fields['apellido_materno'].required = False
        self.fields['fecha_nacimiento'].required = False
        self.fields['profesion'].required = False
        self.fields['tlf'].required = False
        self.fields['email'].required = False
        self.fields['lugar_de_trabajo'].required = False
        self.fields['email_trabajo'].required = False
    class Meta:
        model = Conyugue
        fields = ('acta','acta_nacimiento','nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'profesion', 'lugar_de_trabajo', 'tlf', 'email', 'email_trabajo',)
        widgets = {
            'lugar_de_trabajo': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'fecha_nacimiento': forms.SelectDateWidget(years=years_to_display),
        }

class EstadoCivil(forms.Form):
    #estado_civil = forms.ChoiceField(label = 'estado_civil', required = True, choices=ESTADO_CIVIL, initial=Soltero, widget = forms.Select(attrs={'onclick':'javascript:yesnoCheck();'}))
    estado_civil = forms.ChoiceField(label = 'estado_civil', required = True, choices=ESTADO_CIVIL, initial=Soltero, widget = forms.Select(attrs={}))

    def __init__(self, *args, **kwargs):
        super(EstadoCivil, self).__init__(*args, **kwargs)
        # Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
        for field in self.fields.values():
            field.error_messages = {'required':'Ingrese {fieldname}'.format(
                fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
                fieldname=field.label), 'invalid':'Valor Inválido'.format(
                fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
                fieldname=field.label)}

class PreguntasEtapa3(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PreguntasEtapa3, self).__init__(*args, **kwargs)

        self.fields['fecha_llegada'].widget.attrs["class"] = 'form-control'

    class Meta:
        model = Preguntas
        fields = ('fecha_llegada', 'permiso_trabajo', 'solicitud_permiso_trabajo',)
        widgets = {
            'fecha_llegada' : forms.SelectDateWidget(years=years_to_display),
            'permiso_trabajo' : forms.CheckboxInput(attrs={'onclick':'javascript:yesnoCheck();'}),
            #'solicitud_permiso_trabajo' : forms.CheckboxInput(attrs={'style':'display:none;'}),
            'solicitud_permiso_trabajo' : forms.CheckboxInput(attrs={}),
        }

class ExtranjeroSiNo(forms.Form):
    SiNo = forms.ChoiceField(label = 'SiNo', required = True, choices=EXTRANJERO, initial=No, widget = forms.RadioSelect(attrs={'onclick':'javascript:yesnoCheck();'}))
    def __init__(self, *args, **kwargs):
        super(ExtranjeroSiNo, self).__init__(*args, **kwargs)
        # Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
        for field in self.fields.values():
            field.error_messages = {'required':'Ingrese {fieldname}'.format(
                fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
                fieldname=field.label), 'invalid':'Valor Inválido'.format(
                fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
                fieldname=field.label)}

class numero_hijos(forms.Form):
    cantidad = forms.IntegerField(label = 'Cantidad de hijos', initial=0, required = True, widget = forms.TextInput(attrs={'class': 'touchspin1', 'name':'demo1'}))
    def __init__(self, *args, **kwargs):
        super(numero_hijos, self).__init__(*args, **kwargs)
        # Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
        for field in self.fields.values():
            field.error_messages = {'required':'Ingrese {fieldname}'.format(
                fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
                fieldname=field.label), 'invalid':'Valor Inválido'.format(
                fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
                fieldname=field.label)}

class FormHijos(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormHijos, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs["class"] = 'form-control soloLetras'
        self.fields['nombre'].widget.attrs["maxlength"] = '60'
        self.fields['apellido_paterno'].widget.attrs["class"] = 'form-control soloLetras'
        self.fields['apellido_paterno'].widget.attrs["maxlength"] = '60'
        self.fields['apellido_materno'].widget.attrs["class"] = 'form-control soloLetras'
        self.fields['apellido_materno'].widget.attrs["maxlength"] = '60'
        self.fields['fecha_nacimiento'].widget.attrs["class"] = 'form-control fecnac'
        self.fields['edad'].widget.attrs["class"] = 'form-control soloNumeros'
        self.fields['edad'].widget.attrs["maxlength"] = '3'
        
        
        # REQUIRED
        self.fields['nombre'].widget.attrs["required"] = 'true'
        self.fields['apellido_paterno'].widget.attrs["required"] = 'true'
        self.fields['apellido_materno'].widget.attrs["required"] = 'true'
        self.fields['fecha_nacimiento'].widget.attrs["required"] = 'true'
        self.fields['edad'].widget.attrs["required"] = 'true'
        

    class Meta:
        model = Hijo
        fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'edad',)
        widgets = {
            'fecha_nacimiento' : forms.SelectDateWidget(years=years_to_display),
            
            'edad' : forms.TextInput(attrs={'class': 'touchspin1', 'name':'demo1'}),
        }

class FormLic(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormLic, self).__init__(*args, **kwargs)
        self.fields['fecha_vigencia'].widget.attrs["class"] = 'form-control'
        self.fields['permanente'].widget.attrs["class"] = 'form-control'
        self.fields['estado_emision'].widget.attrs["class"] = 'form-control'
        self.fields['licencia'].widget.attrs["class"] = 'form-control soloNumeros'
        
        
        # REQUIRED
        self.fields['fecha_vigencia'].widget.attrs["required"] = 'true'
        self.fields['permanente'].widget.attrs["required"] = 'true'
        self.fields['estado_emision'].widget.attrs["required"] = 'true'
        self.fields['licencia'].widget.attrs["required"] = 'true'
        
        

    class Meta:
        model = LicenciasConducir
        fields = ('fecha_vigencia', 'permanente', 'estado_emision', 'licencia',)
        widgets = {
            'fecha_vigencia' : forms.SelectDateWidget(years=years_to_display),
            
            
        }	



class EstudiosForm(forms.ModelForm):
    class Meta:
        model = Estudio
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(EstudiosForm, self).__init__(*args, **kwargs)
        self.fields['nivel_estudios'].widget.attrs["class"] = 'form-control'
        self.fields['universidad'].widget.attrs["class"] = 'form-control soloLetras'
        self.fields['universidad'].widget.attrs["maxlength"] = '100'
        self.fields['titulo'].widget.attrs["class"] = 'form-control soloLetras'
        self.fields['titulo'].widget.attrs["maxlength"] = '100'
        self.fields['carrera'].widget.attrs["class"] = 'form-control soloLetras'
        self.fields['carrera'].widget.attrs["maxlength"] = '100'
        self.fields['cedula_profesional_cedula'].widget.attrs["class"] = 'form-control soloNumeros'
        self.fields['cedula_profesional_cedula'].widget.attrs["maxlength"] = '8'
        self.fields['cedula_profesional_imagen_cedula_profesional'].widget.attrs["class"] = 'form-control'
        
        self.fields['constacia_de_estudio'].widget.attrs["class"] = 'form-control'

        
        
        #for campos in self.fields:
        #    self.fields[campos].widget.attrs.update({'class': 'form-control'})

class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = Capacitaciones
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(CapacitacionForm, self).__init__(*args, **kwargs)
        self.fields['tipo_curso'].widget.attrs["class"] = 'form-control'
        self.fields['nombre_curso'].widget.attrs["class"] = 'form-control soloLetras'
        self.fields['nombre_curso'].widget.attrs["maxlength"] = '100'
        self.fields['certificado'].widget.attrs["class"] = 'form-control'

        self.fields['nombre_curso'].widget.attrs["required"] = 'true'
        self.fields['certificado'].widget.attrs["required"] = 'true'
        #for campos in self.fields:
        #    self.fields[campos].widget.attrs.update({'class': 'form-control'})

class IdiomasForm(forms.ModelForm):
    class Meta:
        model = Idioma
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(IdiomasForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
        self.fields['idioma'].widget.attrs["maxlength"] = '60'
        self.fields['idioma'].widget.attrs["class"] = 'form-control soloLetras'

class DomicilioForm(forms.ModelForm):
    class Meta:
        model = Domicilio
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(DomicilioForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
        
        

class RecomendacionesForm(forms.ModelForm):
    class Meta:
        model = Recomendaciones
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(RecomendacionesForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control','accept':'image/*'})
            self.fields[campos].widget.attrs["required"] = 'true'

class BancoForm(forms.ModelForm): 
    class Meta:
        model = Banco
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(BancoForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
        self.fields['clabe'].widget.attrs["maxlength"] = '18'
        self.fields['clabe'].widget.attrs["class"] = 'form-control soloNumeros'

class NacionForm(forms.ModelForm): 
    class Meta:
        model = Nacionalidad
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(NacionForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})

class DomicilioForm2(forms.Form):
        tipo_comprobante = forms.ModelChoiceField(label = 'tipo_comprobante', required = True, queryset=Country.objects.all().order_by('pais'), initial=1,  widget = forms.Select(attrs={'class': 'form-control'}))
        comprobante_domicilio = forms.FileField(label='comprobante_domicilio', required = True)
        tlf_residencial = forms.CharField(label = 'tel', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono', 'data-mask': '(99) (9999-9999)'}))
        
        def __init__(self, *args, **kwargs):
            super(DomicilioForm2, self).__init__(*args, **kwargs)
            # Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
            for field in self.fields.values():
                field.error_messages = {'required':'Ingrese {fieldname}'.format(
                fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
                fieldname=field.label), 'invalid':'Valor Inválido'.format(
                fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
                fieldname=field.label)}
        


            

class VisasForm(forms.Form):
        pais = forms.ModelChoiceField(label = 'pais_nacimiento', required = True, queryset=Country.objects.all().order_by('pais'), initial=1,  widget = forms.Select(attrs={'class': 'form-control'}))
        fecha_vigencia = forms.DateField(label = 'vigencia_visa', required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
        imagen_visa = forms.FileField(label='img_vis', required = False)
        
        def __init__(self, *args, **kwargs):
            super(VisasForm, self).__init__(*args, **kwargs)
            # Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
            for field in self.fields.values():
                field.error_messages = {'required':'Ingrese {fieldname}'.format(
                fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
                fieldname=field.label), 'invalid':'Valor Inválido'.format(
                fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
                fieldname=field.label)}
        

class PreguntasFormet3(forms.ModelForm):
    class Meta:
        model = Preguntas
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(PreguntasFormet3, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})
        self.fields['permiso_trabajo'].widget.attrs.update({'onclick':'javascript:yesnoCheck();'})

        
class Formulario_baja(forms.Form):
    motivo = forms.CharField(label = 'Motivo', widget = forms.Textarea(attrs={'class': 'form-control sololetras','cols':'40','rows':'3','maxlength':'200'}))
    fecha_baja = forms.DateField(label = 'Fecha de baja',required = True, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_baja = forms.ChoiceField(label = 'Tipo de baja', required = True,initial='Renuncia', choices=TIPO_BAJA, widget = forms.Select(attrs={'class': 'form-control'}))
    

    def __init__(self, *args, **kwargs):
        super(Formulario_baja, self).__init__(*args, **kwargs)