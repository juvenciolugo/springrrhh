# -*- coding: utf-8 -*-
import json
from django.db.models import Q
from django.shortcuts import render
from django.template import loader
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.sessions.backends.db import SessionStore

#from django.contrib.auth.models import User, Group
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
#from django.shortcuts import render_to_response
#from django.template import RequestContext
#from django.contrib.auth.decorators import login_required
#from .models import *
from candidatos.models import *
from empleados.models import *
from .forms import *
from candidatos.metodos import *
import time
#import os
#from os.path import splitext, basename
#from candidatos.forms import *

#from .forms import *
from datetime import datetime, timedelta
#from django.db import IntegrityError

# Create your views here.

#@login_required(login_url = '/login/')
def home_candidato(request, template_name = "candidatos/home-candidato.html"):

    return render(request, template_name, locals(),)


def registro_cv(request, template_name = "candidatos/captura_cv.html"):
    

    if request.method == 'POST':
        form = Formulario_candidato(request.POST)
        #if form.is_valid():
        #else:
        
    else:
        status_con="False"
        con_id=""
        form_candidato=Formulario_candidato()
        form_idioma=Formulario_idioma()
        form_editidioma=Formulario_idioma()
        form_hermano=Formulario_hermano_candidato()
        form_edithermano=Formulario_hermano_candidato()
        form_hijo=Formulario_hijo_candidato
        form_edithijo=Formulario_hijo_candidato
        form_referencia=Formulario_referencia()
        form_editreferencia=Formulario_referencia()
        form_experiencia=Formulario_experiencia()
        form_editexperiencia=Formulario_experiencia()
        form_estudio=Formulario_estudios()
        form_estudiootro=Formulario_estudiosotros()
        form_editestudio=Formulario_estudios()
        form_editestudiootro=Formulario_estudiosotros()

        ############investigar si hay registro guardado
        #if request.session['cand_reg'] not in [None,'']:
        if 'cand_reg' in request.session:
            print (request.session['cand_reg'])
            
            
            try:
                candId=request.session['cand_reg']
                candidato= Candidato.objects.get(id=candId)
                form_candidato=set_values_candidato(candidato)
                experiencias = Experiencia.objects.filter(candidato=candidato)
                referencias = Referencia.objects.filter(candidato=candidato)
                hijos = Hijo_candidato.objects.filter(candidato=candidato)
                hermanos = Hermano_candidato.objects.filter(candidato=candidato)
                idiomas = Idioma_candidato.objects.filter(candidato=candidato)
                estudios = Estudios_pro.objects.filter(candidato=candidato)
                estudiosotros = Estudios_otros.objects.filter(candidato=candidato)
            except Exception as e:
                print("No encontro archivo candidato")
                print(e)
                pass
            
        
        form_idioma.fields['idioma'].widget.attrs['style'] ="text-transform: uppercase;"
        form_editidioma.fields['idioma'].widget.attrs['style'] ="text-transform: uppercase;"

        

        #form_candidato.fields['edad'].widget.attrs['disabled'] ='disabled'
        
        form_candidato.fields['edad'].widget.attrs['readonly'] ='readonly'
        form_candidato.fields['piso'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['depto'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['estudia_que'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['estudia_donde'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['estudia_horario'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['estudia_termino'].widget.attrs['disabled'] ='disabled'

        form_candidato.fields['primaria_annios'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['primaria_inicio'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['primaria_termino'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['primaria_documento'].widget.attrs['disabled'] ='disabled'
        
        form_candidato.fields['secundaria_annios'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['secundaria_inicio'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['secundaria_termino'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['secundaria_documento'].widget.attrs['disabled'] ='disabled'
        
        form_candidato.fields['preparatoria_annios'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['preparatoria_inicio'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['preparatoria_termino'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['preparatoria_documento'].widget.attrs['disabled'] ='disabled'
        
        form_candidato.fields['tecnica_annios'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['tecnica_inicio'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['tecnica_termino'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['tecnica_documento'].widget.attrs['disabled'] ='disabled'

        
        form_candidato.fields['pago_infonavit'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['auto_marca'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['auto_modelo'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['seguro_monto'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['sindicato_nombre'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['sindicato_cargo'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['ingreso_monto'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['ingreso_fuente'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['conocido_nombre'].widget.attrs['disabled'] ='disabled'
        form_candidato.fields['conocido_depto'].widget.attrs['disabled'] ='disabled'

        form_experiencia.fields['experiencia_supervision_num'].widget.attrs['disabled'] ='disabled'
    
    return render(request, template_name, locals(),)


def cv_secuno(request):#agregar secuno
    if not request.POST._mutable:
        request.POST._mutable = True
    request.POST['fecha_nac']=mod_fecha(request.POST.get('fecha_nac'))
    paisdirec=request.POST['pais_direc']

    if not paisdirec=="1":
        request.POST['esdo']=""
    form = CandidatoSecunoForm(request.POST)
    response=""
    
    if form.is_valid():
        emp_id=request.POST.get('emp_id')
        print("emp_id "+emp_id)

        id_n = request.POST.get('id_n')
        print("id_n "+id_n)
       
        con_id = request.POST.get('con_id')
        print("con_id "+con_id)
       
        if con_id:# es actualizacion x parte de RRHH
            id_n=con_id


        if 'cand_reg' in request.session:
            id_n=request.session['cand_reg']

        if id_n or emp_id:##es actualización por parte del candidato o del colaborador
            if emp_id:
                candidato= Candidato.objects.get(emp_id=emp_id)
                id_n=candidato.id
            else:
                candidato= Candidato.objects.get(id=id_n)
            
            candidato.fuente_recluta=form.cleaned_data['fuente_recluta']
            candidato.puesto_solicitado=form.cleaned_data['puesto_solicitado']
            candidato.sueldo_deseado=form.cleaned_data['sueldo_deseado']
            candidato.puesto_solicitado=form.cleaned_data['puesto_solicitado']
            candidato.nombre=form.cleaned_data['nombre']
            candidato.apellido_paterno=form.cleaned_data['apellido_paterno']
            candidato.apellido_materno=form.cleaned_data['apellido_materno']
            candidato.sexo=form.cleaned_data['sexo']
            candidato.estado_civil=form.cleaned_data['estado_civil']
            candidato.edad=form.cleaned_data['edad']
            candidato.fecha_nac=form.cleaned_data['fecha_nac']
            candidato.lugar_nac=form.cleaned_data['lugar_nac']
            candidato.pais_nacimiento=form.cleaned_data['pais_nacimiento']
            candidato.tel=form.cleaned_data['tel']
            candidato.cel=form.cleaned_data['cel']
            candidato.tipo=form.cleaned_data['tipo']
            candidato.calle=form.cleaned_data['calle']
            candidato.num_ext=form.cleaned_data['num_ext']
            candidato.num_int=form.cleaned_data['num_int']
            candidato.calle_uno=form.cleaned_data['calle_uno']
            candidato.calle_dos=form.cleaned_data['calle_dos']
            candidato.piso=form.cleaned_data['piso']
            candidato.depto=form.cleaned_data['depto']
            candidato.cp=form.cleaned_data['cp']
            candidato.colonia=form.cleaned_data['colonia']
            candidato.esdo=form.cleaned_data['esdo']
            candidato.pais_direc=form.cleaned_data['pais_direc']
            candidato.referencia=form.cleaned_data['referencia']
            candidato.trayectoria_de_casa=form.cleaned_data['trayectoria_de_casa']
            #candidato.email_personal=request.POST.get('email_personal')
            candidato.email_personal=form.cleaned_data['email_personal']
            candidato.rfc=form.cleaned_data['rfc']
            candidato.curp=form.cleaned_data['curp']
            candidato.imss=form.cleaned_data['imss']
            candidato.cartilla=form.cleaned_data['cartilla']
            candidato.tipo_licencia=form.cleaned_data['tipo_licencia']
            candidato.licencia=form.cleaned_data['licencia']
            
            candidato.save()
            data = {
                'result': 'OK',
                'id':id_n
            }
            response=data
        else:
            #print("edad:")
            #print(form.cleaned_data['edad'])
            #print(request.POST)
            #candidato= Candidato.objects.get(id=cand_id)
            post=form.save()
            ##guardar el ID en una variable de sesion

            request.session['cand_reg'] = post.id
            #print(post.id)
            data = {
                    'result': 'OK',
                    'id':post.id
                    #'id':13
            }
            response=data

    else:
        #pas_err=form.errors['password2']
        print(form.errors)
        #data = {
        #    'result': 'datos',
        #    'message': pas_err
        #}
        data = {
                'result': 'errores'
            }
        response=data
    return JsonResponse(response)

def del_session(request):#Elimina session de CV
    if request.is_ajax():
        del request.session['cand_reg']
    return HttpResponse('OK')

def mod_fecha(fec):
    if fec not in [None,'']:
        return (datetime.strptime(fec, '%d/%m/%Y').strftime('%Y-%m-%d'))
    else:
        return fec


def cv_secdos(request):#agregar secdos
    #tomar Id del input oculto
    cand_id = request.POST.get('candId2')
    print(cand_id)
    if 'cand_reg' in request.session:
        cand_id=request.session['cand_reg']
    #cand_id=13
    if not request.POST._mutable:
        request.POST._mutable = True
    
    
    request.POST['estudia_termino']=mod_fecha(request.POST.get('estudia_termino'))

    #print(request.POST)
    form = CandidatoSecdosForm(request.POST)
    #print(form)
    if form.is_valid():
        try:
            #buscar candidato en base de datos
            candidato= Candidato.objects.get(id=cand_id)
            #candidato= Candidato.objects.get(id=37)
            
            ##asignar valores
            candidato.primaria=form.cleaned_data['primaria']
            candidato.primaria_annios=form.cleaned_data['primaria_annios']
            candidato.primaria_inicio=form.cleaned_data['primaria_inicio']
            candidato.primaria_termino=form.cleaned_data['primaria_termino']
            candidato.primaria_documento=form.cleaned_data['primaria_documento']
            candidato.secundaria=form.cleaned_data['secundaria']
            candidato.secundaria_annios=form.cleaned_data['secundaria_annios']
            candidato.secundaria_inicio=form.cleaned_data['secundaria_inicio']
            candidato.secundaria_termino=form.cleaned_data['secundaria_termino']
            candidato.secundaria_documento=form.cleaned_data['secundaria_documento']
            candidato.preparatoria=form.cleaned_data['preparatoria']
            candidato.preparatoria_annios=form.cleaned_data['preparatoria_annios']
            candidato.preparatoria_inicio=form.cleaned_data['preparatoria_inicio']
            candidato.preparatoria_termino=form.cleaned_data['preparatoria_termino']
            candidato.preparatoria_documento=form.cleaned_data['preparatoria_documento']
            candidato.tecnica=form.cleaned_data['tecnica']
            candidato.tecnica_annios=form.cleaned_data['tecnica_annios']
            candidato.tecnica_inicio=form.cleaned_data['tecnica_inicio']
            candidato.tecnica_termino=form.cleaned_data['tecnica_termino']
            candidato.tecnica_documento=form.cleaned_data['tecnica_documento']
            
            candidato.estudia_actualmente=form.cleaned_data['estudia_actualmente']
            candidato.estudia_que=form.cleaned_data['estudia_que']
            candidato.estudia_donde=form.cleaned_data['estudia_donde']
            candidato.estudia_horario=form.cleaned_data['estudia_horario']
            candidato.estudia_termino=form.cleaned_data['estudia_termino']
            candidato.maquinas_equipos=form.cleaned_data['maquinas_equipos']
            
            candidato.save()
            
            data = {
                'result': 'OK'
            }
            response=data
        except Exception as e:
            print(e)
            data = {
                'result': 'errores'
            }
            response=data
    else:
        print(form.errors)
        data = {
                'result': 'errores'
        }
        response=data

    return JsonResponse(response)

def lst_idioma(request):#buscar idioma
    #print(request.GET.get('id'))
    id=request.GET.get('id')
    
    idioma= Idioma_candidato.objects.get(pk=id)
    data = {
        'status':"OK",
        'id': idioma.id,
        'idioma': idioma.idioma,
        'porcentaje': idioma.idioma_porcentaje,
    }

    return JsonResponse(data)

def del_idioma(request):#elimina idioma
    data = dict()
    id=request.GET.get('id')
    
    idioma= Idioma_candidato.objects.get(pk=id)
    candidato=idioma.candidato
    idioma.delete()
    data['form_is_valid'] = True
    idiomas = Idioma_candidato.objects.filter(candidato=candidato)
    data['html_idiomas_lista'] = render_to_string('candidatos/idiomas_lista.html', {
        'idiomas': idiomas
    })
    return JsonResponse(data)

def edit_idioma(request):#editar idioma
    data = dict()
    if not request.POST._mutable:
        request.POST._mutable = True
    id=request.POST.get('idi_id')
    
    request.POST['idioma']=request.POST.get('idioma').upper()
    
    f_idioma=request.POST.get('idioma')
    
    f_porcentaje=request.POST.get('idioma_porcentaje')
    cand_id = request.POST.get('candId_editidioma')
    #cand_id =13
    candidato= Candidato.objects.get(id=cand_id)
    #investiga si existe el nombre
    try:
        
        idi=Idioma_candidato.objects.filter(~Q(id=id),candidato=candidato,idioma=f_idioma)
        if idi:
            data={
                    'form_is_valid' : False,
                    'error':'Idioma ya existe!'
                }
        else:
            idioma= Idioma_candidato.objects.get(pk=id)
            candidato=idioma.candidato

            idioma.idioma=f_idioma.upper()
            idioma.idioma_porcentaje=f_porcentaje
            idioma.save()
            data['form_is_valid'] = True
            idiomas = Idioma_candidato.objects.filter(candidato=candidato)
            data['html_idiomas_lista'] = render_to_string('candidatos/idiomas_lista.html', {
               'idiomas': idiomas
            })
       # print("encontro")
    except Exception as e:
        print(e)
        
    
    
    return JsonResponse(data)



def add_idioma(request):#agregar o modificar idioma
    data = dict()
    if not request.POST._mutable:
        request.POST._mutable = True
    form = IdiomaSecdosForm(request.POST)
    request.POST['idioma']=request.POST.get('idioma').upper()
    bidioma = request.POST.get('idioma')
    cand_id = request.POST.get('candId2_idi')
    #cand_id =13
    response=""
    if form.is_valid():
        id=request.POST.get('idi_id')
        candidato= Candidato.objects.get(id=cand_id)
        if (id in [None,'']):#nuevo idioma
            try:
                idi=Idioma_candidato.objects.get(candidato=candidato,idioma=bidioma)
                if idi:
                    data={
                        'form_is_valid' : False,
                        'error':'Idioma ya existe!'
                    }
            except Exception as e:
                idi = form.save(commit=False)
                idi.candidato=candidato
                idi.save()
                data['form_is_valid'] = True
                idiomas = Idioma_candidato.objects.filter(candidato=candidato)
                data['html_idiomas_lista'] = render_to_string('candidatos/idiomas_lista.html', {
                    'idiomas': idiomas
                },request=request)
            response=data     
        else:#actualizar idioma
            try:
                
                idioma= Idioma_candidato.objects.get(pk=id)
                #idioma = form.save(commit=False)
                idioma.idioma=form.cleaned_data['idioma']
                idioma.idioma_porcentaje=form.cleaned_data['idioma_porcentaje']
                idioma.save()
                data['form_is_valid'] = True
                idiomas = Idioma_candidato.objects.filter(candidato=candidato)
                data['html_idiomas_lista'] = render_to_string('candidatos/idiomas_lista.html', {
                    'idiomas': idiomas
                },request=request)
                response=data
            except Exception as e:
                print(e)
                data = {
                    'result': 'errores'
                }

    else:
        print(form.errors)
        data = {
                'result': 'errores'
        }
        response=data
              
    return JsonResponse(response)


def cv_sectres(request):#agregar sectres
    #tomar Id del input oculto
    cand_id = request.POST.get('candId3')
    if 'cand_reg' in request.session:
        cand_id=request.session['cand_reg']
    
    #cand_id=13
    form = CandidatoSectresForm(request.POST)
    if form.is_valid():
        try:
            #buscar candidato en base de datos
            candidato= Candidato.objects.get(id=cand_id)
            ##asignar valores
            candidato.padre_nombre=form.cleaned_data['padre_nombre']
            candidato.padre_apellido_paterno=form.cleaned_data['padre_apellido_paterno']
            candidato.padre_apellido_materno=form.cleaned_data['padre_apellido_materno']
            candidato.padre_edad=form.cleaned_data['padre_edad']
            candidato.padre_ocupacion=form.cleaned_data['padre_ocupacion']
            candidato.padre_lugar_trabajo=form.cleaned_data['padre_lugar_trabajo']
            candidato.padre_domicilio=form.cleaned_data['padre_domicilio']
            candidato.padre_tel=form.cleaned_data['padre_tel']
            candidato.padre_vive=form.cleaned_data['padre_vive']

            candidato.madre_nombre=form.cleaned_data['madre_nombre']
            candidato.madre_apellido_paterno=form.cleaned_data['madre_apellido_paterno']
            candidato.madre_apellido_materno=form.cleaned_data['madre_apellido_materno']
            candidato.madre_edad=form.cleaned_data['madre_edad']
            candidato.madre_ocupacion=form.cleaned_data['madre_ocupacion']
            candidato.madre_lugar_trabajo=form.cleaned_data['madre_lugar_trabajo']
            candidato.madre_domicilio=form.cleaned_data['madre_domicilio']
            candidato.madre_tel=form.cleaned_data['madre_tel']
            candidato.madre_vive=form.cleaned_data['madre_vive']

            candidato.conyuge_nombre=form.cleaned_data['conyuge_nombre']
            candidato.conyuge_apellido_paterno=form.cleaned_data['conyuge_apellido_paterno']
            candidato.conyuge_apellido_materno=form.cleaned_data['conyuge_apellido_materno']
            candidato.conyuge_edad=form.cleaned_data['conyuge_edad']
            candidato.conyuge_ocupacion=form.cleaned_data['conyuge_ocupacion']
            candidato.conyuge_lugar_trabajo=form.cleaned_data['conyuge_lugar_trabajo']
            candidato.conyuge_domicilio=form.cleaned_data['conyuge_domicilio']
            candidato.conyuge_tel=form.cleaned_data['conyuge_tel']
            candidato.conyuge_vive=form.cleaned_data['conyuge_vive']
            candidato.save()
            
            data = {
                'result': 'OK'
            }
            response=data
        except Exception as e:
           # print(e)
            data = {
                'result': 'errores'
            }
            response=data
    else:
        print(form.errors)
        data = {
                'result': 'errores'
        }
        response=data

    return JsonResponse(response)

def lst_estudio(request):#buscar estudio
    #print(request.GET.get('id'))
    id=request.GET.get('id')
    #id=13
    estudio= Estudios_pro.objects.get(pk=id)
    data = {
        'status':"OK",
        'id': estudio.id,
        'tipo': estudio.estudios_tipo,
        'escuela': estudio.estudios_escuela,
        'nombre': estudio.estudios_nombre,
        'annios': estudio.estudios_annios,
        'inicio': estudio.estudios_inicio,
        'termino': estudio.estudios_termino,
        'documento': estudio.estudios_documento,
        'tesis': estudio.estudios_tesis,
        'forma': estudio.estudios_forma,
        'cedula': estudio.estudios_cedula,
    }

    return JsonResponse(data)

def lst_otroestudio(request):#buscar estudiootro
    #print(request.GET.get('id'))
    id=request.GET.get('id')
    
    estudio= Estudios_otros.objects.get(pk=id)
    data = {
        'status':"OK",
        'id': estudio.id,
        'tipo': estudio.estudios_tipo,
        'nombre': estudio.estudios_nombre,
        'inicio': estudio.estudios_inicio,
        'termino': estudio.estudios_termino,
        'documento': estudio.estudios_documento,
    }

    return JsonResponse(data)

def add_otroestudio(request):#agregar estudiootro sec dos
    data = dict()
    form = EstudioOtroSecdosForm(request.POST)
    cand_id = request.POST.get('candId2_estotro')
   # cand_id =13
    response=""
    if form.is_valid():
        candidato= Candidato.objects.get(id=cand_id)
        estudio = form.save(commit=False)
        estudio.candidato=candidato
        estudio.save()
        data['form_is_valid'] = True
        estudiosotros = Estudios_otros.objects.filter(candidato=candidato)
        data['html_estudiosotros_lista'] = render_to_string('candidatos/estudiosotros_lista.html', {
            'estudiosotros': estudiosotros
        })
        response=data
    else:
        print(form.errors)
        data = {
                'result': 'errores'
        }
        response=data
              
    return JsonResponse(response)

def edit_otroestudio(request):#editar estudio
    data = dict()
    id=request.POST.get('estotro_id')

    try:
        estudio= Estudios_otros.objects.get(pk=id)
        candidato=estudio.candidato
        estudio.estudios_tipo=request.POST.get('estudios_tipo')
        estudio.estudios_nombre=request.POST.get('estudios_nombre')
        estudio.estudios_inicio=request.POST.get('estudios_inicio')
        estudio.estudios_termino=request.POST.get('estudios_termino')
        estudio.estudios_documento=request.POST.get('estudios_documento')
    
        estudio.save()
        data['form_is_valid'] = True
        estudiosotros = Estudios_otros.objects.filter(candidato=candidato)
        data['html_estudiosotros_lista'] = render_to_string('candidatos/estudiosotros_lista.html', {
            'estudiosotros': estudiosotros
        })
        response=data
    except Exception as e:
        print(e)
        data = {
            'result': 'errores'
        }
        response=data
    
    
    return JsonResponse(data)

def del_otroestudio(request):#Eliminar estudiootro
    data = dict()
    id=request.GET.get('id')
    estudio= Estudios_otros.objects.get(pk=id)
    candidato=estudio.candidato
    estudio.delete()
    data['form_is_valid'] = True
    estudiosotros = Estudios_otros.objects.filter(candidato=candidato)
    data['html_estudiosotros_lista'] = render_to_string('candidatos/estudiosotros_lista.html', {
        'estudiosotros': estudiosotros
    })

    return JsonResponse(data)

def add_estudio(request):#agregar estudio sec dos
    data = dict()
    form = EstudioSecdosForm(request.POST)
    cand_id = request.POST.get('candId2_est')
    #cand_id =13
    response=""
    if form.is_valid():
        candidato= Candidato.objects.get(id=cand_id)
        estudio = form.save(commit=False)
        estudio.candidato=candidato
        estudio.save()
        data['form_is_valid'] = True
        estudios = Estudios_pro.objects.filter(candidato=candidato)
        data['html_estudios_lista'] = render_to_string('candidatos/estudios_lista.html', {
            'estudios': estudios
        })
        response=data
    else:
        print(form.errors)
        data = {
                'result': 'errores'
        }
        response=data
              
    return JsonResponse(response)

def edit_estudio(request):#editar estudio
    data = dict()
    id=request.POST.get('est_id')

    try:
        estudio= Estudios_pro.objects.get(pk=id)
        candidato=estudio.candidato
        estudio.estudios_tipo=request.POST.get('estudios_tipo')
        estudio.estudios_escuela=request.POST.get('estudios_escuela')
        estudio.estudios_nombre=request.POST.get('estudios_nombre')
        estudio.estudios_annios=request.POST.get('estudios_annios')
        estudio.estudios_inicio=request.POST.get('estudios_inicio')
        estudio.estudios_termino=request.POST.get('estudios_termino')
        estudio.estudios_documento=request.POST.get('estudios_documento')
        estudio.estudios_tesis=request.POST.get('estudios_tesis')
        estudio.estudios_forma=request.POST.get('estudios_forma')
        estudio.estudios_cedula=request.POST.get('estudios_cedula')
    
        estudio.save()
        data['form_is_valid'] = True
        estudios = Estudios_pro.objects.filter(candidato=candidato)
        data['html_estudios_lista'] = render_to_string('candidatos/estudios_lista.html', {
            'estudios': estudios
        })
        response=data
    except Exception as e:
        print(e)
        data = {
            'result': 'errores'
        }
        response=data
    
    
    return JsonResponse(data)

def del_estudio(request):#Eliminar estudio
    data = dict()
    id=request.GET.get('id')
    estudio= Estudios_pro.objects.get(pk=id)
    candidato=estudio.candidato
    estudio.delete()
    data['form_is_valid'] = True
    estudios = Estudios_pro.objects.filter(candidato=candidato)
    data['html_estudios_lista'] = render_to_string('candidatos/estudios_lista.html', {
        'estudios': estudios
    })

    return JsonResponse(data)

def lst_hijo(request):#buscar hijo
    id=request.GET.get('id')
    hijo= Hijo_candidato.objects.get(pk=id)

    data = {
        'status':"OK",
        'id': hijo.id,
        'nombre': hijo.hijo_nombre,
        'paterno': hijo.hijo_apellido_paterno,
        'materno': hijo.hijo_apellido_materno,
        'edad': hijo.hijo_edad,
        'ocupacion': hijo.hijo_ocupacion,
        'lugar': hijo.hijo_lugar_ocupacion,
        'domicilio': hijo.hijo_domicilio,
        'telefono': hijo.hijo_tel,
    }

    return JsonResponse(data)

def del_hijo(request):#borrar hijo
    data = dict()
    id=request.GET.get('id')
    hijo= Hijo_candidato.objects.get(pk=id)
    candidato=hijo.candidato
    hijo.delete()
    data['form_is_valid'] = True
    hijos = Hijo_candidato.objects.filter(candidato=candidato)
    data['html_hijos_lista'] = render_to_string('candidatos/hijos_lista.html', {
        'hijos': hijos
    })
    return JsonResponse(data)

def edit_hijo(request):#editar hijo
    data = dict()
    id=request.POST.get('hijo_id')
    cand_id=request.POST.get('candId_edithijo')
    #cand_id=13
    bnombre = request.POST.get('hijo_nombre')
    candidato= Candidato.objects.get(id=cand_id)
    try:
        hij=Hijo_candidato.objects.filter(~Q(id=id),candidato=candidato,hijo_nombre=bnombre)
        if hij:
            data={
                'form_is_valid' : False,
                'error':'Hijo ya existe!'
            }
        else:
            hijo= Hijo_candidato.objects.get(pk=id)
            candidato=hijo.candidato
            hijo.hijo_nombre=bnombre
            hijo.hijo_edad=request.POST.get('hijo_edad')
            hijo.hijo_ocupacion=request.POST.get('hijo_ocupacion')
    
            hijo.save()
            data['form_is_valid'] = True
            hijos = Hijo_candidato.objects.filter(candidato=candidato)
            data['html_hijos_lista'] = render_to_string('candidatos/hijos_lista.html', {
                  'hijos': hijos
            })
    except Exception as e:
        print(e)
        
    
    return JsonResponse(data)

def add_hijocv(request):#agregar hijo sec tres
    data = dict()
    form = HijoSectresForm(request.POST)
    bnombre = request.POST.get('hijo_nombre')
    bpaterno = request.POST.get('hijo_apellido_paterno')
    bmaterno = request.POST.get('hijo_apellido_materno')
    
    cand_id = request.POST.get('candId3_hijo')
    #cand_id =13
    response=""
    if form.is_valid():
        candidato= Candidato.objects.get(id=cand_id)
        try:
            hij=Hijo_candidato.objects.get(candidato=candidato,hijo_nombre=bnombre,hijo_apellido_paterno=bpaterno,hijo_apellido_materno=bmaterno)
            if hij:
                data={
                    'form_is_valid' : False,
                    'error':'Hijo ya existe!'
                }
        except Exception as e:
            #print(e)
            hijo = form.save(commit=False)
            hijo.candidato=candidato
            hijo.save()
            data['form_is_valid'] = True
            hijos = Hijo_candidato.objects.filter(candidato=candidato)
            data['html_hijos_lista'] = render_to_string('candidatos/hijos_lista.html', {
                'hijos': hijos
            })
        response=data
    else:
       # print(form.errors)
        data = {
                'result': 'errores'
        }
        response=data
              
    return JsonResponse(response)

def lst_hermano(request):#buscar hermano
    id=request.GET.get('id')
    hermano= Hermano_candidato.objects.get(pk=id)
    
    data = {
        'status':"OK",
        'id': hermano.id,
        'nombre': hermano.hermano_nombre,
        'paterno': hermano.hermano_apellido_paterno,
        'materno': hermano.hermano_apellido_materno,
        'edad': hermano.hermano_edad,
        'ocupacion': hermano.hermano_ocupacion,
        'lugar': hermano.hermano_lugar_ocupacion,
        'domicilio': hermano.hermano_domicilio,
        'telefono': hermano.hermano_tel,
    }

    return JsonResponse(data)

def del_hermano(request):#borrar hermano
    data = dict()
    id=request.GET.get('id')
    hermano= Hermano_candidato.objects.get(pk=id)
    candidato=hermano.candidato
    hermano.delete()
    data['form_is_valid'] = True
    hermanos = Hermano_candidato.objects.filter(candidato=candidato)
    data['html_hermanos_lista'] = render_to_string('candidatos/hermanos_lista.html', {
        'hermanos': hermanos
    })
    return JsonResponse(data)

def edit_hermano(request):#editar hermano
    data = dict()
    id=request.POST.get('hermano_id')
    cand_id = request.POST.get('candId_edithermano')
    #cand_id =13
    candidato= Candidato.objects.get(id=cand_id)
    bnombre = request.POST.get('hermano_nombre')
    try:
        her=Hermano_candidato.objects.filter(~Q(id=id),candidato=candidato,hermano_nombre=bnombre)
        if her:
            data={
                'form_is_valid' : False,
                'error':'Hermano ya existe!'
            }
        else:
            hermano= Hermano_candidato.objects.get(pk=id)
            candidato=hermano.candidato
            hermano.hermano_nombre=request.POST.get('hermano_nombre')
            hermano.hermano_edad=request.POST.get('hermano_edad')
            hermano.hermano_ocupacion=request.POST.get('hermano_ocupacion')
    
            hermano.save()
            data['form_is_valid'] = True
            hermanos = Hermano_candidato.objects.filter(candidato=candidato)
            data['html_hermanos_lista'] = render_to_string('candidatos/hermanos_lista.html', {
                'hermanos': hermanos
            })

    except Exception as e:
        print(e)
       
    
    return JsonResponse(data)

def add_hermanocv(request):#agregar hermano sec tres
    data = dict()
    form = HermanoSectresForm(request.POST)
    bnombre = request.POST.get('hermano_nombre')
    bpaterno = request.POST.get('hermano_apellido_paterno')
    bmaterno = request.POST.get('hermano_apellido_materno')
    cand_id = request.POST.get('candId3_hermano')
    #cand_id =13
    response=""
    if form.is_valid():
        candidato= Candidato.objects.get(id=cand_id)
        try:
            her=Hermano_candidato.objects.get(candidato=candidato,hermano_nombre=bnombre,hermano_apellido_paterno=bpaterno,hermano_apellido_materno=bmaterno)
            if her:
                data={
                    'form_is_valid' : False,
                    'error':'Hermano ya existe!'
                }
        except Exception as e:            
            hermano = form.save(commit=False)
            hermano.candidato=candidato
            hermano.save()
            data['form_is_valid'] = True
            hermanos = Hermano_candidato.objects.filter(candidato=candidato)
            data['html_hermanos_lista'] = render_to_string('candidatos/hermanos_lista.html', {
                'hermanos': hermanos
            })
        response=data
    else:
        #print(form.errors)
        data = {
                'result': 'errores'
        }
        response=data
    return JsonResponse(response)


def cv_seccuatro(request):#agregar secdos
    #tomar Id del input oculto
    cand_id = request.POST.get('candId4')
    if 'cand_reg' in request.session:
        cand_id=request.session['cand_reg']
    #cand_id =13
    if not request.POST._mutable:
        request.POST._mutable = True
    request.POST['fecha_disponible']=mod_fecha(request.POST.get('fecha_disponible'))
    form = CandidatoSeccuatroForm(request.POST)
    if form.is_valid():
        try:
            #buscar candidato en base de datos
            candidato= Candidato.objects.get(id=cand_id)
            ##asignar valores
            candidato.vivienda_propia=form.cleaned_data['vivienda_propia']
            candidato.credito_infonavit=form.cleaned_data['credito_infonavit']
            candidato.pago_infonavit=form.cleaned_data['pago_infonavit']
            candidato.auto_propio=form.cleaned_data['auto_propio']
            candidato.auto_marca=form.cleaned_data['auto_marca']
            candidato.auto_modelo=form.cleaned_data['auto_modelo']
            candidato.seguro_vida=form.cleaned_data['seguro_vida']
            candidato.seguro_monto=form.cleaned_data['seguro_monto']

            candidato.afianzado=form.cleaned_data['afianzado']
            candidato.afianzado_monto=form.cleaned_data['afianzado_monto']
            candidato.afiliado_sindicato=form.cleaned_data['afiliado_sindicato']
            candidato.sindicato_nombre=form.cleaned_data['sindicato_nombre']
            candidato.sindicato_cargo=form.cleaned_data['sindicato_cargo']
            candidato.tiempo_libre=form.cleaned_data['tiempo_libre']
            candidato.embarazo=form.cleaned_data['embarazo']
            candidato.religion=form.cleaned_data['religion']

            candidato.estado_salud=form.cleaned_data['estado_salud']
            candidato.fuma=form.cleaned_data['fuma']
            candidato.bebe=form.cleaned_data['bebe']
            candidato.tatuajes=form.cleaned_data['tatuajes']
            candidato.perforaciones=form.cleaned_data['perforaciones']
            candidato.disposicion_rolar=form.cleaned_data['disposicion_rolar']
            candidato.disposicion_viajar=form.cleaned_data['disposicion_viajar']
            candidato.ingreso_extra=form.cleaned_data['ingreso_extra']
            candidato.ingreso_monto=form.cleaned_data['ingreso_monto']
            candidato.ingreso_fuente=form.cleaned_data['ingreso_fuente']
            candidato.labora_conocido=form.cleaned_data['labora_conocido']
            candidato.conocido_nombre=form.cleaned_data['conocido_nombre']
            candidato.conocido_depto=form.cleaned_data['conocido_depto']
            candidato.fecha_disponible=form.cleaned_data['fecha_disponible']
            candidato.save()
            
            data = {
                'result': 'OK'
            }
            response=data
        except Exception as e:
           # print(e)
            data = {
                'result': 'errores'
            }
            response=data
    else:
        #print(form.errors)
        data = {
                'result': 'errores'
        }
        response=data

    return JsonResponse(response)

def lst_experiencia(request):#buscar hermano
    try:
       # print(request.GET.get('id'))
        id=request.GET.get('id')
        exp= Experiencia.objects.get(pk=id)
    except Exception as e:
        print(e)
    
    
    try:
        data = {
        'status':"OK",
        'id': exp.id,
        'nombre': exp.empresa_nombre,
        'direccion': exp.empresa_direccion,
        'telefono': exp.empresa_tel,
        'giro': exp.empresa_giro,
        'jefe': exp.empresa_nombre_jefe,
        'puesto': exp.empresa_jefe_puesto,
        'ingreso': exp.empresa_fecha_ingreso,
        'salario_inicial': exp.empresa_salario_inicio,
        'separacion': exp.empresa_fecha_separacion,
        'salario_final': exp.empresa_salario_final,
        'puesto_ultimo': exp.empresa_puesto_ultimo,
        'puesto_ultimo_tiempo': exp.empresa_puesto_ultimo_tiempo,
        'depto_ultimo': exp.empresa_puesto_ultimo_depto,
        'puesto_anterior': exp.empresa_puesto_anterior,
        'puesto_anterior_tiempo': exp.empresa_puesto_anterior_tiempo,
        'depto_anterior': exp.empresa_puesto_anterior_depto,
        'exp_supervision': exp.experiencia_supervision,
        'num_supervision': exp.experiencia_supervision_num,
        'motivo': exp.separacion_motivo,
        'empresa_actual': exp.empresa_actual,
    }
    
    except Exception as e:
        print(e)
    

    return JsonResponse(data)

def del_experiencia(request):#borrar experiencia
    data = dict()
    id=request.GET.get('id')
    exp= Experiencia.objects.get(pk=id)
    candidato=exp.candidato
    exp.delete()
    data['form_is_valid'] = True
    experiencias = Experiencia.objects.filter(candidato=candidato)
    data['html_experiencias_lista'] = render_to_string('candidatos/experiencias_lista.html', {
        'experiencias': experiencias
    })
    return JsonResponse(data)

def edit_experiencia(request):#editar experiencia
    data = dict()
    #form = IdiomaSecdosForm(request.POST)
    if not request.POST._mutable:
        request.POST._mutable = True
    print(request.POST)
    request.POST['empresa_fecha_ingreso']=mod_fecha(request.POST.get('empresa_fecha_ingreso'))
    fec_sep=request.POST.get('empresa_fecha_separacion')
    
    if fec_sep not in [None,'']:
        request.POST['empresa_fecha_separacion']=mod_fecha(fec_sep)
    else:
        request.POST['empresa_fecha_separacion']=None
    
    id=request.POST.get('exp_id')
    exp= Experiencia.objects.get(pk=id)
    candidato=exp.candidato
    exp.empresa_nombre=request.POST.get('empresa_nombre')
    exp.empresa_direccion=request.POST.get('empresa_direccion')
    exp.empresa_tel=request.POST.get('empresa_tel')
    exp.empresa_giro=request.POST.get('empresa_giro')
    exp.empresa_nombre_jefe=request.POST.get('empresa_nombre_jefe')
    exp.empresa_jefe_puesto=request.POST.get('empresa_jefe_puesto')
    exp.empresa_fecha_ingreso=request.POST.get('empresa_fecha_ingreso')
    exp.empresa_salario_inicio=request.POST.get('empresa_salario_inicio')
    exp.empresa_fecha_separacion=request.POST.get('empresa_fecha_separacion')
    exp.empresa_salario_final=request.POST.get('empresa_salario_final')
    exp.empresa_puesto_ultimo=request.POST.get('empresa_puesto_ultimo')
    exp.empresa_puesto_ultimo_tiempo=request.POST.get('empresa_puesto_ultimo_tiempo')
    exp.empresa_puesto_ultimo_depto=request.POST.get('empresa_puesto_ultimo_depto')
    exp.empresa_puesto_anterior=request.POST.get('empresa_puesto_anterior')
    exp.empresa_puesto_anterior_tiempo=request.POST.get('empresa_puesto_anterior_tiempo')
    exp.empresa_puesto_anterior_depto=request.POST.get('empresa_puesto_anterior_depto')
    exp.experiencia_supervision=request.POST.get('experiencia_supervision')
    exp.experiencia_supervision_num=request.POST.get('experiencia_supervision_num')
    exp.separacion_motivo=request.POST.get('separacion_motivo')
    exp.empresa_actual=request.POST.get('empresa_actual')

    
    exp.save()
    data['form_is_valid'] = True
    experiencias = Experiencia.objects.filter(candidato=candidato)
    data['html_experiencias_lista'] = render_to_string('candidatos/experiencias_lista.html', {
        'experiencias': experiencias
    })
    response=data
    
    return JsonResponse(data)

def cv_seccinco(request):#agregar experiencia sec cinco
    data = dict()
    if not request.POST._mutable:
        request.POST._mutable = True
    print(request.POST)
    request.POST['empresa_fecha_ingreso']=mod_fecha(request.POST.get('empresa_fecha_ingreso'))
    request.POST['empresa_fecha_separacion']=mod_fecha(request.POST.get('empresa_fecha_separacion'))
    form = ExperienciaSeccincoForm(request.POST)
    cand_id = request.POST.get('candId5')
    if 'cand_reg' in request.session:
        cand_id=request.session['cand_reg']
    #cand_id =13
    response=""
    if form.is_valid():
        try:
            candidato= Candidato.objects.get(id=cand_id)
            experiencia = form.save(commit=False)
            experiencia.candidato=candidato
            experiencia.save()
            data['form_is_valid'] = True
            experiencias = Experiencia.objects.filter(candidato=candidato)
            data['html_experiencias_lista'] = render_to_string('candidatos/experiencias_lista.html', {
                'experiencias': experiencias
            })
            response=data
        except Exception as e:
            #print(e)
            data = {
                'result': 'errores'
            }
            response=data
    else:
        #print(form.errors)
        data = {
                'result': 'errores'
        }
        response=data
    return JsonResponse(response)

def lst_referencia(request):#buscar referencia
    try:
        id=request.GET.get('id')
        ref= Referencia.objects.get(pk=id)
    except Exception as e:
        print(e)
    try:
        data = {
        'status':"OK",
        'id': ref.id,
        'nombre': ref.referencia_nombre,
        'domicilio': ref.referencia_domicilio,
        'telefono': ref.referencia_tel,
        'ocupacion': ref.referencia_ocupacion,
        'annios': ref.referencia_annios_conocer,
    }
    
    except Exception as e:
        print(e)

    return JsonResponse(data)

def del_referencia(request):#borrar referencia
    data = dict()
    id=request.GET.get('id')
    ref= Referencia.objects.get(pk=id)
    candidato=ref.candidato
    ref.delete()
    data['form_is_valid'] = True
    referencias = Referencia.objects.filter(candidato=candidato)
    data['html_referencias_lista'] = render_to_string('candidatos/referencias_lista.html', {
        'referencias': referencias
    })
    return JsonResponse(data)

def edit_referencia(request):#editar referencia
    data = dict()
    #form = IdiomaSecdosForm(request.POST)
    
    id=request.POST.get('ref_id')
    ref= Referencia.objects.get(pk=id)
    candidato=ref.candidato
    ref.referencia_nombre=request.POST.get('referencia_nombre')
    ref.referencia_domicilio=request.POST.get('referencia_domicilio')
    ref.referencia_tel=request.POST.get('referencia_tel')
    ref.referencia_ocupacion=request.POST.get('referencia_ocupacion')
    ref.referencia_annios_conocer=request.POST.get('referencia_annios_conocer')
        
    ref.save()
    data['form_is_valid'] = True
    referencias = Referencia.objects.filter(candidato=candidato)
    data['html_referencias_lista'] = render_to_string('candidatos/referencias_lista.html', {
        'referencias': referencias
    })
    response=data
    
    return JsonResponse(data)


def cv_secseis(request):#agregar referencia sec seis
    data = dict()
    form = ReferenciaSecseisForm(request.POST)
    cand_id = request.POST.get('candId6')
    if 'cand_reg' in request.session:
        cand_id=request.session['cand_reg']
    #cand_id =13
    response=""
    if form.is_valid():
        try:
            candidato= Candidato.objects.get(id=cand_id)
            referencia = form.save(commit=False)
            referencia.candidato=candidato
            referencia.save()
            data['form_is_valid'] = True
            referencias = Referencia.objects.filter(candidato=candidato)
            data['html_referencias_lista'] = render_to_string('candidatos/referencias_lista.html', {
                'referencias': referencias
            })
            response=data
        except Exception as e:
            #print(e)
            data = {
                'result': 'errores'
            }
            response=data
    else:
        #print(form.errors)
        data = {
                'result': 'errores'
        }
        response=data
    return JsonResponse(response)



def lst_correo(request):#buscar correos para enviar email
    cand_id=request.GET.get('cand_id')
    user_id=request.GET.get('user_id')
    try:
        cand= Candidato.objects.get(id=cand_id)
        cand_email=cand.email_personal
        cand_name=cand.nombre+" "+cand.apellido_paterno+" "+cand.apellido_materno
        user= User.objects.get(pk=user_id)
        user_email=user.email
        user_name=user.first_name+" "+user.last_name

        data = {
            'status':"OK",
            'cand_email': cand_email,
            'user_email':user_email,
            'user_name': user_name,
            'cand_name': cand_name,
        }

    except Exception as e:
        print(e)
        data = {
            'status':"NONE",
            'cand_id':cand_id,
        }
    return JsonResponse(data)

def lst2_correo(request):#buscar correos para enviar email
    emp_id=request.GET.get('emp_id')
    user_id=request.GET.get('user_id')
    try:
        emp= User.objects.get(pk=emp_id)
        #emp_user=User.objects.get(pk=user_id)

        emp_email=emp.email
        emp_name=emp.first_name+" "+emp.last_name

        user= User.objects.get(pk=user_id)
        user_email=user.email
        user_name=user.first_name+" "+user.last_name

        data = {
            'status':"OK",
            'emp_email': emp_email,
            'user_email':user_email,
            'user_name': user_name,
            'emp_name': emp_name,
        }

    except Exception as e:
        print(e)
        data = {
            'status':"NONE",
            'emp_id':emp_id,
        }
    return JsonResponse(data)


    


def lst2_docs(request):#buscar Docs de empleados
    INE=False
    Acta=False
    CURP=False
    RFC=False
    Comp_dom=False
    Comp_grado=False
    Comp_cursos=False
    Comp_permiso=False
    IMSS=False
    Cartas=False
    Esdo_cuenta=False
    Esdo_info=False
    Lic_manejo=False
    Observaciones=False
    id=request.GET.get('id')
    status=' Etapa 1'
    try:
        print(id)
        emp= Empleado.objects.get(pk=id)
        st=emp.status
        if st==2:
            status=' Etapa 2'
        elif st==4:
            status=' Etapa 3'
        elif st==6:
            status=' Etapa 4'
        elif st==8:
            status=' Etapa 5'
        elif st==13:
            status=' Etapa 6'
        elif st==15:
            status=' Completo proceso'


        if not emp.docu_ident_front in [None,'']:
            INE=True
        if not emp.acta_nacimiento in [None,'']:
            Acta=True
        if not emp.imagen_curp in [None,'']:
            CURP=True
        if not emp.imagen_rfc in [None,'']:
            RFC=True
        if not emp.imagen_imss in [None,'']:
            IMSS=True
        if not emp.imagen_infonavit in [None,'']:
            Esdo_info=True
    except Exception as e:
        print(e)
        
    try:#####
        dom= Domicilio.objects.get(user=id)
        print(dom.comprobante_domicilio)
        if not dom.comprobante_domicilio in [None,'']:
            Comp_dom=True
    except Exception as e:
        print(e)
    try:#####
        est= Estudio.objects.get(user=id)
        if not est.cedula_profesional.imagen_cedula_profesional in [None,'']:
        #if not est.constacia_de_estudio in [None,'']:
            Comp_grado=True
    except Exception as e:
        print(e)
    try:####
        cap= Capacitaciones.objects.filter(user=id)[0]
        if not cap.certificado in [None,'']:
            Comp_cursos=True
    except Exception as e:
        print(e)
    try:####
        reco= Recomendaciones.objects.filter(user=id)[0]
        if not reco.carta_recomendacion in [None,'']:
            Cartas=True
    except Exception as e:
        print(e)
    try:####
        ban= Banco.objects.get(user=id)
        if not ban.contrato in [None,'']:
            Esdo_cuenta=True
    except Exception as e:
        print(e)
    try:####
        lic= LicenciasConducir.objects.get(user=id)
        if not lic.imagen_lic_anverso in [None,'']:
            Lic_manejo=True
    except Exception as e:
        print(e)
    #pendiente no existe file en empleados    
    #if not emp.imagen_rfc in [None,'']:
     #    Comp_permiso=True
    data = {
        'status':"OK",
        'et_status':status,
        'INE': INE,
        'Acta': Acta,
        'CURP': CURP,
        'RFC': RFC,
        'Comp_dom': Comp_dom,
        'Comp_grado': Comp_grado,
        'Comp_cursos': Comp_cursos,
        'Comp_permiso': Comp_permiso,
        'IMSS': IMSS,
        'Cartas': Cartas,
        'Esdo_cuenta': Esdo_cuenta,
        'Esdo_info': Esdo_info,
        'Lic_manejo': Lic_manejo,
        'Observaciones': Observaciones,
    }

    return JsonResponse(data)