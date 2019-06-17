# -*- coding: utf-8 -*-
#from empleados.views import *
from empleados.models import *
from candidatos.models import *
from empleados.forms import *
from dashboard.forms import CreaEmpleado2
from django.contrib.auth.models import User
import unicodedata

def set_values (usuario):
    form = Formulario1()
    
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        form.fields['referencia'].initial = empleado.referencia
        form.fields['nombre'].initial = empleado.nombre
        form.fields['apellido_paterno'].initial = empleado.apellido_paterno
        form.fields['apellido_materno'].initial = empleado.apellido_materno
        form.fields['fecha_nacimiento'].initial = empleado.fecha_nacimiento.strftime('%d/%m/%Y')
        form.fields['pais_nacimiento'].initial = empleado.pais_nacimiento
        form.fields['edad'].initial = empleado.edad
        form.fields['tipo_documento_identidad'].initial = empleado.tipo_documento_identidad
        if (empleado.pasaporte_valido):
            form.fields['fecha_vencimiento_pasaporte'].initial = empleado.pasaporte_valido.strftime('%d/%m/%Y')
        form.fields['pasaporte'].initial = empleado.pasaporte
        form.fields['imagen_pasaporte'].initial = empleado.imagen_pasaporte
        form.fields['tel'].initial = empleado.tel
        form.fields['cel'].initial = empleado.cel
        form.fields['email_personal'].initial = empleado.email_personal
        #form.fields['direccion'].initial = empleado.direccion
        form.fields['tipo'].initial = empleado.tipo
        form.fields['calle'].initial = empleado.calle
        form.fields['num_ext'].initial = empleado.num_ext
        form.fields['num_int'].initial = empleado.num_int
        form.fields['calle_uno'].initial = empleado.calle_uno
        form.fields['calle_dos'].initial = empleado.calle_dos
        form.fields['piso'].initial = empleado.piso
        form.fields['depto'].initial = empleado.depto
        form.fields['cp'].initial = empleado.cp
        form.fields['colonia'].initial = empleado.colonia
        form.fields['esdo'].initial = empleado.esdo
        form.fields['pais_dir'].initial = empleado.pais_dir
        form.fields['foto'].initial = empleado.foto
        form.fields['docu_ident_front'].initial = empleado.docu_ident_front
        form.fields['docu_ident_back'].initial = empleado.docu_ident_back
        
        form.fields['acta_nacimiento'].initial = empleado.acta_nacimiento
        nacionalidades = Nacionalidad.objects.filter(user=empleado)
        form.fields['nacionalidad'].initial = nacionalidades
        
    except:
        pass
    return form



def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',cadena) if unicodedata.category(c) != 'Mn'))
    return s

def set_values_emp (id):
    form = CreaEmpleado2()
    try:
        cand = Candidato.objects.get(id = id)
        form.fields['username'].initial = cand.nombre.lower()
        form.fields['first_name'].initial = cand.nombre
        form.fields['last_name'].initial = cand.apellido_paterno+' '+cand.apellido_materno
        form.fields['email'].initial = elimina_tildes(cand.nombre.lower())+'.'+elimina_tildes(cand.apellido_paterno.lower())+'@springlabs.net'
    except:
        pass
    return form


def set_Candvalues_etapa2 (usuario):
    form = Formulario_etapa_2()
    try:
        cand = Candidato.objects.get(emp_id = usuario.pk)
        form.fields['curp'].initial = cand.curp
        form.fields['rfc'].initial = cand.rfc
        form.fields['imss'].initial = cand.imss
        form.fields['licencia_conducir'].initial = cand.licencia
    except:
        pass
    return form

def set_values_2 (usuario):
    
    form = Formulario_etapa_2()
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        lic = LicenciasConducir.objects.get(user = usuario.pk)
        form.fields['curp'].initial = empleado.curp
        form.fields['imagen_curp'].initial = empleado.imagen_curp
        form.fields['rfc'].initial = empleado.rfc
        form.fields['imagen_rfc'].initial = empleado.imagen_rfc
        form.fields['sat'].initial = empleado.sat
        form.fields['imagen_sat'].initial = empleado.imagen_sat
        form.fields['infonavit'].initial = empleado.infonavit
        form.fields['imagen_infonavit'].initial = empleado.imagen_infonavit
        form.fields['imss'].initial = empleado.imss
        form.fields['imagen_imss'].initial = empleado.imagen_imss
        
        form.fields['licencia_conducir'].initial = lic.licencia
        form.fields['vigencia_licencia_conducir'].initial = lic.fecha_vigencia.strftime('%d/%m/%Y')
        form.fields['permanente'].initial = lic.permanente
        form.fields['estado_emision_licencia'].initial = lic.estado_emision
        form.fields['img_lic_anverso'].initial = lic.imagen_lic_anverso
        form.fields['img_lic_reverso'].initial = lic.imagen_lic_reverso


    except:
        pass
    return form

def set_values_conyugue (usuario):
    form = FormConyugue()
    try:
        try:
            conyugue = Conyugue.objects.get(user = usuario.pk)
        except ObjectDoesNotExist:
            conyugue=None
        if conyugue:
            form.fields['acta'].initial = conyugue.acta
            form.fields['acta_nacimiento'].initial = conyugue.acta_nacimiento
            form.fields['nombre'].initial = conyugue.nombre
            form.fields['apellido_paterno'].initial = conyugue.apellido_paterno
            form.fields['apellido_materno'].initial = conyugue.apellido_materno
            form.fields['fecha_nacimiento'].initial = conyugue.fecha_nacimiento.strftime('%d/%m/%Y')
            form.fields['profesion'].initial = conyugue.profesion
            form.fields['tlf'].initial = conyugue.tlf
            form.fields['email'].initial = conyugue.email
            form.fields['email_trabajo'].initial = conyugue.email_trabajo
            form.fields['lugar_de_trabajo'].initial = conyugue.lugar_de_trabajo
    except:
        pass
    return form

def set_Candvalues(usuario):
    form = Formulario1()
    try:
        try:
            cand = Candidato.objects.get(emp_id = usuario.pk)
        except ObjectDoesNotExist:
            cand=None
        
        if cand:
            form.fields['referencia'].initial = cand.referencia
            form.fields['nombre'].initial = cand.nombre
            form.fields['apellido_paterno'].initial = cand.apellido_paterno
            form.fields['apellido_materno'].initial = cand.apellido_materno
            form.fields['fecha_nacimiento'].initial = cand.fecha_nac.strftime('%d/%m/%Y')
            form.fields['pais_nacimiento'].initial = cand.pais_nacimiento
            form.fields['edad'].initial = cand.edad
            form.fields['tel'].initial = cand.tel
            form.fields['cel'].initial = cand.cel
            form.fields['email_personal'].initial = cand.email_personal
            form.fields['tipo'].initial = cand.tipo
            form.fields['calle'].initial = cand.calle
            form.fields['num_ext'].initial = cand.num_ext
            form.fields['num_int'].initial = cand.num_int
            form.fields['calle_uno'].initial = cand.calle_uno
            form.fields['calle_dos'].initial = cand.calle_dos
            form.fields['piso'].initial = cand.piso
            form.fields['depto'].initial = cand.depto
            form.fields['cp'].initial = cand.cp
            form.fields['colonia'].initial = cand.colonia
            form.fields['esdo'].initial = cand.esdo
            form.fields['pais_direc'].initial = cand.pais_direc
            form.fields['nacionalidad'].initial = cand.pais_nacimiento
        
            
            
    except Exception as e:
        print(e)
    return form

def set_Candvalues_etapa3 (usuario):
    form = FormConyugue()
    try:
        cand = Candidato.objects.get(emp_id = usuario.pk)
        form.fields['nombre'].initial = cand.conyuge_nombre
        form.fields['apellido_paterno'].initial = cand.conyuge_apellido_paterno
        form.fields['apellido_materno'].initial = cand.conyuge_apellido_materno
        form.fields['profesion'].initial = cand.conyuge_ocupacion
        form.fields['tlf'].initial = cand.conyuge_tel
        form.fields['lugar_de_trabajo'].initial = cand.conyuge_lugar_trabajo
    except:
        pass
    return form

    
def set_Candvalues_etapa3_civil (usuario):
    form = EstadoCivil()
    try:
        cand = Candidato.objects.get(emp_id = usuario.pk)
        form.fields['estado_civil'].initial = cand.estado_civil
    except ObjectDoesNotExist:
        pass
    return form

def set_values_preguntas (usuario):
    form = PreguntasFormet3()
    try:
        preg = Preguntas.objects.get(user_id = usuario.user_id)
        form.fields['extranjero'].initial = preg.extranjero
        form.fields['fecha_llegada'].initial = preg.fecha_llegada.strftime('%d/%m/%Y')
        form.fields['permiso_trabajo'].initial = preg.permiso_trabajo
        form.fields['solicitud_permiso_trabajo'].initial = preg.solicitud_permiso_trabajo
    except Exception as e:
        print("error en : "+e) 	
    #except:
    #	pass
    return form

def set_values_hijo (usuario):
    form = FormHijos()
    try:
        hijo = Hijo.objects.get(user_id = usuario.user_id)
        form.fields['nombre'].initial = hijo.nombre
        form.fields['apellido_paterno'].initial = hijo.apellido_paterno
        form.fields['apellido_materno'].initial = hijo.apellido_materno
        form.fields['fecha_nacimiento'].initial = hijo.fecha_nacimiento.strftime('%d/%m/%Y')
        form.fields['edad'].initial = hijo.edad
    except Exception as e:
        print("error en : "+e) 	
    #except:
    #	pass
    return form

def set_values_estudios (usuario):
    form = EstudiosForm()
    try:
        estudio = Estudio.objects.get(user_id = usuario.user_id)
        form.fields['nivel_estudios'].initial = estudio.nivel_estudios
        form.fields['universidad'].initial = estudio.universidad
        form.fields['titulo'].initial = estudio.titulo
        form.fields['carrera'].initial = estudio.carrera
        form.fields['cedula_profesional_cedula'].initial = estudio.cedula_profesional_cedula
        form.fields['cedula_profesional_imagen_cedula_profesional'].initial = estudio.cedula_profesional_imagen_cedula_profesional
        form.fields['constacia_de_estudio'].initial = estudio.constacia_de_estudio
        
    except Exception as e:
        print("error en : "+e) 	
    #except:
    #	pass
    return form

def set_values_comprobante (usuario):
    form = DomicilioForm()
    try:
        dom = Domicilio.objects.get(user_id = usuario.user_id)
        form.fields['tipo_comprobante'].initial = dom.tipo_comprobante
        form.fields['comprobante_domicilio'].initial = dom.comprobante_domicilio
        form.fields['tlf_residencial'].initial = dom.tlf_residencial
        
    except Exception as e:
        print("error en : "+e) 	
    #except:
    #	pass
    return form

def set_values_banco (usuario):
    form = BancoForm()
    try:
        banco = Banco.objects.get(user_id = usuario.user_id)
        form.fields['banco'].initial = banco.banco
        form.fields['contrato'].initial = banco.contrato
        form.fields['clabe'].initial = banco.clabe
    except Exception as e:
        print("error en : "+e) 	
    #except:
    #	pass
    return form