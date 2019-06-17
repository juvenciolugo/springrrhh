#-*- coding: utf-8 -*-
from django import forms
from empleados.models import *
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import *
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.forms import ModelChoiceField
from django.core.files import File

Colector = "Colector"
Administrador = "Administrador"
GRUPO = (
        (Colector, 'Colector'),
        (Administrador, 'Administrador'), 
    )

class ActivaEmpleado(forms.Form):
	username = forms.CharField(label = "usuario", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
	email = forms.EmailField(label = "correo", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}))
	password = forms.CharField(label = "contraseña", required = True, widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))

	def __init__(self, *args, **kwargs):
		super(ActivaEmpleado, self).__init__(*args, **kwargs)
		# Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes 
		for field in self.fields.values():
			field.error_messages = {'required':'Ingrese {fieldname}'.format(
				fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
				fieldname=field.label), 'invalid':'Valor Inválido'.format(
				fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
				fieldname=field.label)} 

class EditEmpleado(forms.Form):
	username = forms.CharField(label = "usuario", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
	first_name = forms.CharField(label = "nombre", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
	last_name = forms.CharField(label = "apellidos", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}))
	#email = forms.EmailField(label = "correo", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
	email = forms.EmailField(label = "correo", required = True, widget = forms.TextInput(attrs={'pattern':'.+@springlabs.net','class': 'form-control', 'placeholder': 'Correo'}))
	password1 = forms.CharField(label = "contraseña", required = True, widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
	password2 = forms.CharField(label = "confirma", required = True, widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirma'}))
	is_admin = forms.TypedChoiceField(coerce=lambda x: bool(int(x)),choices=((0,'Administrador'),(1,'RRHH'),(2,'Editor'),(3,'Empleado'),(4,'Becario'),(5,'Consultor')),widget=forms.Select())
	is_active = forms.TypedChoiceField(coerce=lambda x: bool(int(x)),choices=((0,'No'),(1,'YES')),widget=forms.Select())
	is_superuser = forms.TypedChoiceField(coerce=lambda x: bool(int(x)),choices=((0,'No'),(1,'YES')),widget=forms.Select())

	def __init__(self, *args, **kwargs):
		super(EditEmpleado, self).__init__(*args, **kwargs)
		# Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes 
		for field in self.fields.values():
			field.error_messages = {'required':'Ingrese {fieldname}'.format(
				fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
				fieldname=field.label), 'invalid':'Valor Inválido'.format(
				fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
				fieldname=field.label)} 

class CreaEmpleado(UserCreationForm):
	username = forms.CharField(label = "Usuario", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
	first_name = forms.CharField(label = "Nombre", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
	last_name = forms.CharField(label = "Apellidos", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}))
	email = forms.EmailField(label = "Correo", required = True, widget = forms.TextInput(attrs={'pattern':'.+@springlabs.net','class': 'form-control', 'placeholder': 'Correo'}))
	password1 = forms.CharField(label = "Contraseña", required = True, widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
	password2 = forms.CharField(label = "Confirma", required = True, widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirma'}))
	is_active = forms.TypedChoiceField(coerce=lambda x: bool(int(x)),choices=((0,'No'),(1,'YES')),widget=forms.Select())
	is_superuser = forms.TypedChoiceField(coerce=lambda x: bool(int(x)),choices=((0,'No'),(1,'YES')),widget=forms.Select())

	def __init__(self, *args, **kwargs):
		super(CreaEmpleado, self).__init__(*args, **kwargs)
		# Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes 
		for field in self.fields.values():
			field.error_messages = {'required':'Ingrese {fieldname}'.format(
				fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
				fieldname=field.label), 'invalid':'Valor Inválido'.format(
				fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
				fieldname=field.label)} 

 

class CreaEmpleado2(UserCreationForm):
	username = forms.CharField(label = "Usuario", required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetrasynumeros', 'placeholder': 'Usuario'}))
	first_name = forms.CharField(label = "Nombre", required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetras', 'placeholder': 'Nombre'}))
	last_name = forms.CharField(label = "Apellidos", required = True, widget = forms.TextInput(attrs={'class': 'form-control sololetras', 'placeholder': 'Apellidos'}))
	email = forms.EmailField(label = "Correo", required = True, widget = forms.TextInput(attrs={'pattern':'.+@springlabs.net','class': 'form-control sololetrasEmail', 'placeholder': 'ejemplo@springlabs.net'}))
	password1 = forms.CharField(label = "Contraseña", required = True, widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
	password2 = forms.CharField(label = "Confirma", required = True, widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirma'}))
	is_active = forms.TypedChoiceField(coerce=lambda x: bool(int(x)),choices=((0,'No'),(1,'YES')),widget=forms.Select())
	is_admin = forms.TypedChoiceField(coerce=lambda x: bool(int(x)),choices=((0,'Administrador'),(1,'RRHH'),(2,'Editor'),(3,'Empleado'),(4,'Becario'),(5,'Consultor')),widget=forms.Select())

	def __init__(self, *args, **kwargs):
		super(CreaEmpleado2, self).__init__(*args, **kwargs)
		# Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes 
		for field in self.fields.values():
			field.error_messages = {'required':'Ingrese {fieldname}'.format(
				fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
				fieldname=field.label), 'invalid':'Valor Inválido'.format(
				fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
				fieldname=field.label)} 


	class Meta:
		
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
			'is_active',
			'is_admin',
			
		]
		

		def clean_password2(self):
			# Check that the two password entries match
			password1 = self.cleaned_data.get("password1")
			password2 = self.cleaned_data.get("password2")
			if password1 and password2 and password1 != password2:
				raise forms.ValidationError("Passwords don't match")
			return password2

		def save2(self, commit=True):
			# Save the provided password in hashed format
			user = super().save(commit=False)
			user.set_password(self.cleaned_data["password1"])
			if commit:
				user.save()
				user.groups.add(Group.objects.get(name='Administrador'))
			return user

class TipoEmpleado(forms.Form):
	#tipo_empleado = forms.ChoiceField(label = 'tipo_empleado', required = True, choices=TIPO_EMP, initial=1, widget = forms.Select(attrs={'onclick':'javascript:tipoemp();'}))
	tipo_empleado = forms.ChoiceField(label = 'Personal', required = True, choices=TIPO_EMP, initial=1, widget = forms.Select(attrs={'onchange':'this.form.submit();'}))
#widget = forms.Select(attrs={'class': 'form-control'}
	def __init__(self, *args, **kwargs):
		super(TipoEmpleado, self).__init__(*args, **kwargs)
		# Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
		for field in self.fields.values():
			field.error_messages = {'required':'Ingrese {fieldname}'.format(
				fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
				fieldname=field.label), 'invalid':'Valor Inválido'.format(
				fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
				fieldname=field.label)}