
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import datetime
from .models import *
from candidatos.models import Candidato
from .forms import *
from dashboard.views import *
from .metodos import *
#from empleados.metodos import set_Candvalues
from datetime import datetime
from django.forms import formset_factory
import os
from os.path import splitext, basename
# Create your views here.





@login_required(login_url = '/captura/')
def captura(request, template_name = "empleados/captura.html"):

    return render(request, template_name, locals(),)

# ========= INICIO ETAPA 1 ==========
@login_required(login_url = '/login/')
def perfil(request, template_name = "empleados/perfil.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        foto = 1
    except:
        foto = 0
    if request.method == 'POST':
        form = Formulario1(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido_paterno = form.cleaned_data['apellido_paterno']
            apellido_materno = form.cleaned_data['apellido_materno']
            fecha_nacimiento = datetime.strptime(request.POST['fecha_nacimiento'], '%d/%m/%Y').strftime('%Y-%m-%d')

            

            """ if("fecha_vencimiento_pasaporte" not in request.POST):
                fecha_vencimiento_pasaporte = datetime.strptime(request.POST['fecha_vencimiento_pasaporte'], '%d/%m/%Y').strftime('%Y-%m-%d')
            else: 
                fecha_vencimiento_pasaporte=None
            
            if ("image_pasaporte" not in request.FILES):
                img_pasaporte =False
            else:
                img_pasaporte = request.FILES['image_pasaporte'] """
            
            try:

            
                pasaporte=None
                fecha_vencimiento_pasaporte=None
                img_pasaporte=None
            

                pais_nacimiento = request.POST['pais_nacimiento']
                pais_nacimiento = Country.objects.get(pk=pais_nacimiento)
                edad = form.cleaned_data['edad']
                tel = form.cleaned_data['tel']
                cel = form.cleaned_data['cel']
                email_personal = form.cleaned_data['email_personal']
                #direccion = form.cleaned_data['direccion']
                tipo = form.cleaned_data['tipo']
                calle = form.cleaned_data['calle']
                num_ext = form.cleaned_data['num_ext']
                num_int = form.cleaned_data['num_int']
                calle_uno = form.cleaned_data['calle_uno']
                calle_dos = form.cleaned_data['calle_dos']
                piso = form.cleaned_data['piso']
                depto = form.cleaned_data['depto']
                cp = form.cleaned_data['cp']
                colonia = form.cleaned_data['cp']
                esdo = form.cleaned_data['esdo']
                pais_direc = form.cleaned_data['pais_direc']
                referencia = form.cleaned_data['referencia']
                foto = request.FILES['foto']
                acta_nacimiento = request.FILES['acta_nacimiento']
                nacionalidad = form.cleaned_data['nacionalidad']
                tipo_documento_identidad_valor = TipoDocumentoIdentidad.objects.get(pk=request.POST['tipo_documento_identidad'])
            except Exception as e:
                response="error"
                print(e)
                form.errors
            # Grabamos los datos nativos en tabla empleados
            nuevo_empleado = Empleado(user=usuario,
                nombre=nombre,
                apellido_paterno=apellido_paterno,
                apellido_materno=apellido_materno,
                fecha_nacimiento=fecha_nacimiento,
                pais_nacimiento=pais_nacimiento,
                edad=edad,
                foto=request.FILES['foto'],
                acta_nacimiento=request.FILES['acta_nacimiento'],
                docu_ident_front=request.FILES['docu_ident_front'], 
                docu_ident_back=request.FILES['docu_ident_back'],
                tipo_documento_identidad=tipo_documento_identidad_valor,
                pasaporte_valido=fecha_vencimiento_pasaporte, 
                pasaporte=pasaporte,
                imagen_pasaporte=img_pasaporte, 
                tel=tel, 
                cel=cel, 
                email_personal=email_personal, 
                #direccion=direccion,
                tipo=tipo,
                calle=calle,
                num_ext=num_ext,
                num_int=num_int,
                calle_uno=calle_uno,
                calle_dos=calle_dos,
                piso=piso,
                depto=depto,
                cp=cp,
                colonia=colonia,
                esdo=esdo,
                pais_direc=pais_direc,
                referencia=referencia)
            nuevo_empleado.save()
            
            # Grabamos las nacionalidades en la tabla nacionalidades referenciando pais y usuario
            for dato in nacionalidad:
                objeto_pais = Country.objects.get(pais=dato)
                if objeto_pais:
                    empleado = Empleado.objects.get(user = usuario.pk)
                    nacionalidad = Nacionalidad(user=empleado,pais=objeto_pais)
                    nacionalidad.save()
            form = set_values(usuario)
            nacionalidades = Nacionalidad.objects.filter(user=empleado)


            ##grabamos extranjero
            formSiNo = ExtranjeroSiNo(request.POST)
            if formSiNo.is_valid():
                extranjero = request.POST['SiNo']
                if extranjero == 'Si':
                    extranjero = True
                else:
                    extranjero = False
                if extranjero == True:
                    formPreguntas = PreguntasEtapa3(request.POST)
                    if formPreguntas.is_valid():
                        obj_preguntas = formPreguntas.save(commit=False)
                        obj_preguntas.extranjero = extranjero
                        obj_preguntas.user = empleado
                        obj_preguntas.save()
                        #preguntas_saved = Preguntas.objects.get(user = empleado)
            #return HttpResponseRedirect('/resumen/%s' % usuario.pk) #EJEMPLO PARA REDIRECT A PÁGINA CON DATOS
            #return HttpResponseRedirect('/perfil/')
        else:
            print (form.errors)
            form.errors
            try:
                empleado = Empleado.objects.get(user = usuario.pk)
                if empleado:
                    form = set_values(usuario)
                    nacionalidades = Nacionalidad.objects.filter(user=empleado)
            except:
                form = Formulario1()
                form.fields['foto'].widget.attrs['accept'] ='image/gif.image/jpeg.image/jpg.image/png'
    else:
        try:
            empleado = Empleado.objects.get(user = usuario.pk)
            
            if empleado:
                form = set_values(usuario)
                form.fields['foto'].widget.attrs['accept'] ='image/*'
                form.fields['acta_nacimiento'].widget.attrs['accept'] ='image/*'
                form.fields['docu_ident_front'].widget.attrs['accept'] ='image/*'
                form.fields['docu_ident_back'].widget.attrs['accept'] ='image/*'
                form.fields['imagen_pasaporte'].widget.attrs['accept'] ='image/*'
                #form.fields['cp'].widget.NumberInput()
                #forms.widgets.NumberInput()
                formPreguntas = PreguntasEtapa3()
                formSiNo = ExtranjeroSiNo()
                nacionalidades = Nacionalidad.objects.filter(user=empleado)

        except:
            ##Buscar datos de candidato y ponerlos en form
            #form = Formulario1()
            form=set_Candvalues(usuario)
            form.fields['nombre'].initial = usuario.first_name
            form.fields['foto'].widget.attrs['accept'] ='image/*'
            form.fields['acta_nacimiento'].widget.attrs['accept'] ='image/*'
            form.fields['docu_ident_front'].widget.attrs['accept'] ='image/*'
            form.fields['docu_ident_back'].widget.attrs['accept'] ='image/*'
            form.fields['imagen_pasaporte'].widget.attrs['accept'] ='image/*'
            
            formPreguntas = PreguntasEtapa3()
            formSiNo = ExtranjeroSiNo()
        #form.fields['tipo_documento_identidad'].initial = datetime.now().strftime("%m-%d-%y")
    return render(request, template_name, locals(),)

@login_required(login_url = '/login/')
def confirma_etapa_1(request, template_name = "dashboard/dashboard.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 2
        empleado.save()
        usuario.first_name= empleado.nombre
        usuario.last_name= empleado.apellido_paterno+" "+empleado.apellido_materno
        usuario.save()
    except:
        pass
    return portafolio(request)



 

@login_required(login_url = '/login/')
def rechaza_etapa_1(request, template_name = "empleados/perfil.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 1
        empleado.delete()
    except:
        pass
    return perfil(request)
# ========= FIN ETAPA 1 ==========


# ========= INICIO ETAPA 2 ========== 
@login_required(login_url = '/login/')
def etapa_2(request, template_name = "empleados/etapa_2.html"):
    usuario = request.user
    empleado = Empleado.objects.get(user = usuario.pk)
    if request.method == 'POST':
        form = Formulario_etapa_2(request.POST, request.FILES)
        if form.is_valid():
            try:
                # VISA 1
                pais_visa_1 = request.POST['visa_1']
                if pais_visa_1:
                    pais_visa_1 = Country.objects.get(pk=pais_visa_1)
                    if not request.POST['vigencia_visa_1'] in [None,'']:
                        fecha_vigencia_visa_1 = datetime.strptime(request.POST['vigencia_visa_1'], '%d/%m/%Y').strftime('%Y-%m-%d')
                    if not request.FILES['img_visa_1'] in [None,'']:
                        img_visa_1 = request.FILES['img_visa_1']
                # VISA 2
                pais_visa_2 = request.POST['visa_2']
                if pais_visa_2:
                    pais_visa_2 = Country.objects.get(pk=pais_visa_2)
                    if not request.POST['vigencia_visa_2'] in [None,'']:
                        fecha_vigencia_visa_2 = datetime.strptime(request.POST['vigencia_visa_2'], '%d/%m/%Y').strftime('%Y-%m-%d')
                    if not request.FILES['img_visa_2'] in [None,'']:
                        img_visa_2 = request.FILES['img_visa_2']
                # VISA 3
                pais_visa_3 = request.POST['visa_3']
                if pais_visa_3:
                    pais_visa_3 = Country.objects.get(pk=pais_visa_3)
                    if not request.POST['vigencia_visa_3'] in [None,'']:
                        fecha_vigencia_visa_3 = datetime.strptime(request.POST['vigencia_visa_3'], '%d/%m/%Y').strftime('%Y-%m-%d')
                    if not request.FILES['img_visa_3'] in [None,'']:
                        img_visa_3 = request.FILES['img_visa_3']
                # VISA 4
                pais_visa_4 = request.POST['visa_4']
                if pais_visa_4:
                    pais_visa_4 = Country.objects.get(pk=pais_visa_4)
                    if not request.POST['vigencia_visa_4'] in [None,'']:
                        fecha_vigencia_visa_4 = datetime.strptime(request.POST['vigencia_visa_4'], '%d/%m/%Y').strftime('%Y-%m-%d')
                    if not request.FILES['img_visa_4'] in [None,'']:
                        img_visa_4 = request.FILES['img_visa_4']
                # VISA 5
                pais_visa_5 = request.POST['visa_5']
                if pais_visa_5:
                    pais_visa_5 = Country.objects.get(pk=pais_visa_5)
                    if not request.POST['vigencia_visa_5'] in [None,'']:
                        fecha_vigencia_visa_5 = datetime.strptime(request.POST['vigencia_visa_5'], '%d/%m/%Y').strftime('%Y-%m-%d')
                    if not request.FILES['img_visa_5'] in [None,'']:
                        img_visa_5 = request.FILES['img_visa_5']
                # LICENCIA
                print("paso las visas")
                licencia = request.POST['licencia_conducir']
                if licencia:
                    fecha_vigencia_licencia=''
                    img_lic_anverso=''
                    img_lic_reverso=''
                    estado_emision = form.cleaned_data['estado_emision_licencia']
                    if not request.POST['vigencia_licencia_conducir'] in [None,'']:
                        fecha_vigencia_licencia = datetime.strptime(request.POST['vigencia_licencia_conducir'], '%d/%m/%Y').strftime('%Y-%m-%d')
                    if not request.FILES['img_lic_anverso'] in [None,'']:
                        img_lic_anverso = request.FILES['img_lic_anverso']
                    if not request.FILES['img_lic_reverso'] in [None,'']:
                        img_lic_reverso = request.FILES['img_lic_reverso']
                print("paso las licencias")

                curp = form.cleaned_data['curp']
                imagen_curp = request.FILES['imagen_curp']
                rfc = form.cleaned_data['rfc']
                imagen_rfc = request.FILES['imagen_rfc']
                sat = form.cleaned_data['sat']
                imagen_sat = request.FILES['imagen_sat']
                infonavit = form.cleaned_data['infonavit']
                imagen_infonavit = request.FILES['imagen_infonavit']
                imss = form.cleaned_data['imss']
                imagen_imss = request.FILES['imagen_imss']
                print("paso las curp sat imss")
            
            except Exception as e:
                response="error"
                print(e)
                form.errors
            #except:
            #    mensaje_error = "Faltan Datos"
            #    print(mensaje_error)
            #    form.errors

            # GUARDADO DE DATOS
            try:
                if pais_visa_1:
                    nueva_visa = visas(user=empleado, pais=pais_visa_1, fecha_vigencia=fecha_vigencia_visa_1, imagen_visa=img_visa_1)
                    previo = visas.objects.filter(user=empleado,pais=pais_visa_1,fecha_vigencia=fecha_vigencia_visa_1)
                    if not previo.exists():
                        nueva_visa.save()
                if pais_visa_2:
                    nueva_visa = visas(user=empleado, pais=pais_visa_2, fecha_vigencia=fecha_vigencia_visa_2, imagen_visa=img_visa_2)
                    previo = visas.objects.filter(user=empleado,pais=pais_visa_2,fecha_vigencia=fecha_vigencia_visa_2)
                    if not previo.exists():
                        nueva_visa.save()
                if pais_visa_3:
                    nueva_visa = visas(user=empleado, pais=pais_visa_3, fecha_vigencia=fecha_vigencia_visa_3, imagen_visa=img_visa_3)
                    previo = visas.objects.filter(user=empleado,pais=pais_visa_3,fecha_vigencia=fecha_vigencia_visa_3)
                    if not previo.exists():
                        nueva_visa.save()
                if pais_visa_4:
                    nueva_visa = visas(user=empleado, pais=pais_visa_4, fecha_vigencia=fecha_vigencia_visa_4, imagen_visa=img_visa_4)
                    previo = visas.objects.filter(user=empleado,pais=pais_visa_4,fecha_vigencia=fecha_vigencia_visa_4)
                    if not previo.exists():
                        nueva_visa.save()
                if pais_visa_5:
                    nueva_visa = visas(user=empleado, pais=pais_visa_5, fecha_vigencia=fecha_vigencia_visa_5, imagen_visa=img_visa_5)
                    previo = visas.objects.filter(user=empleado,pais=pais_visa_5,fecha_vigencia=fecha_vigencia_visa_5)
                    if not previo.exists():
                        nueva_visa.save()
                if licencia:
                    nueva_licencia = LicenciasConducir(user=empleado,
                        permanente=request.POST['permanente'], 
                        fecha_vigencia=fecha_vigencia_licencia, 
                        estado_emision=estado_emision, 
                        imagen_lic_anverso=img_lic_anverso, 
                        imagen_lic_reverso=img_lic_reverso, 
                        licencia=licencia)
                    nueva_licencia.save()
                empleado = Empleado.objects.get(user = usuario.pk)
                empleado.curp = curp
                empleado.imagen_curp = imagen_curp
                empleado.rfc = rfc
                empleado.imagen_rfc = imagen_rfc
                empleado.sat = sat
                empleado.imagen_sat = imagen_sat
                empleado.infonavit = infonavit
                empleado.imagen_infonavit = imagen_infonavit
                empleado.imss = imss
                empleado.imagen_imss = imagen_imss
                empleado.status = 3
                empleado.save()
                if visas.objects.filter(user=empleado).exists():
                    todas_visas = visas.objects.filter(user=empleado)
                if LicenciasConducir.objects.filter(user=empleado).exists():
                    licencia_data = LicenciasConducir.objects.filter(user=empleado)
                form = set_values_2(usuario)
            except Exception as e:
                response="error"
                print(e)
                form.errors

        else:
            form.errors
            try:
                empleado = Empleado.objects.get(user = usuario.pk)
                if empleado.status == 3:
                    if visas.objects.filter(user=empleado).exists():
                        todas_visas = visas.objects.filter(user=empleado)
                    if LicenciasConducir.objects.filter(user=empleado).exists():
                        licencia_data = LicenciasConducir.objects.filter(user=empleado)
                    form = set_values_2(usuario)
            except:
                form = Formulario_etapa_2()
            form.fields['img_visa_1'].widget.attrs['accept'] ='image/*'
            form.fields['img_visa_2'].widget.attrs['accept'] ='image/*'
            form.fields['img_visa_3'].widget.attrs['accept'] ='image/*'
            form.fields['img_visa_4'].widget.attrs['accept'] ='image/*'
            form.fields['img_visa_5'].widget.attrs['accept'] ='image/*'
            form.fields['img_lic_anverso'].widget.attrs['accept'] ='image/*'
            form.fields['img_lic_reverso'].widget.attrs['accept'] ='image/*'
            form.fields['imagen_curp'].widget.attrs['accept'] ='image/*'
            form.fields['imagen_rfc'].widget.attrs['accept'] ='image/*'
            form.fields['imagen_sat'].widget.attrs['accept'] ='image/*'
            form.fields['imagen_infonavit'].widget.attrs['accept'] ='image/*'
            form.fields['imagen_imss'].widget.attrs['accept'] ='image/*'
    else:
        try:
            empleado = Empleado.objects.get(user = usuario.pk)
            if empleado.status == 3:
                if visas.objects.filter(user=empleado).exists():
                    todas_visas = visas.objects.filter(user=empleado)
                if LicenciasConducir.objects.filter(user=empleado).exists():
                    licencia_data = LicenciasConducir.objects.filter(user=empleado)
                form = set_values_2(usuario)
            else:
                #Buscar datos en modelo Candidatos
                form=set_Candvalues_etapa2(usuario)
                #form = Formulario_etapa_2()
            #si trae numero de licencia
            if (form.fields['licencia_conducir']):
                trae_lic=True
                form.fields['licencia_conducir'].widget.attrs['required'] ='true'
                form.fields['vigencia_licencia_conducir'].widget.attrs['required'] ='true'
                form.fields['img_lic_anverso'].widget.attrs['required'] ='true'
                form.fields['img_lic_reverso'].widget.attrs['required'] ='true'

            else:
                trae_lic=False
                
            form.fields['img_visa_1'].widget.attrs['accept'] ='image/*'
            form.fields['img_visa_2'].widget.attrs['accept'] ='image/*'
            form.fields['img_visa_3'].widget.attrs['accept'] ='image/*'
            form.fields['img_visa_4'].widget.attrs['accept'] ='image/*'
            form.fields['img_visa_5'].widget.attrs['accept'] ='image/*'
            form.fields['img_lic_anverso'].widget.attrs['accept'] ='image/*'
            form.fields['img_lic_reverso'].widget.attrs['accept'] ='image/*'
            form.fields['imagen_curp'].widget.attrs['accept'] ='image/*'
            form.fields['imagen_rfc'].widget.attrs['accept'] ='image/*'
            form.fields['imagen_sat'].widget.attrs['accept'] ='image/*'
            form.fields['imagen_infonavit'].widget.attrs['accept'] ='image/*'
            form.fields['imagen_imss'].widget.attrs['accept'] ='image/*'
        except:
            pass
    return render(request, template_name, locals(),)

@login_required(login_url = '/login/')
def rechaza_etapa_2(request, template_name = "empleados/etapa_2.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 2
        empleado.imagen_curp.delete(save=True)
        empleado.imagen_rfc.delete(save=True)
        empleado.imagen_sat.delete(save=True)
        empleado.imagen_infonavit.delete(save=True)
        empleado.imagen_imss.delete(save=True)
        if visas.objects.filter(user=empleado).exists():
            todas_visas = visas.objects.filter(user=empleado)
            todas_visas.delete()
        if LicenciasConducir.objects.filter(user=empleado).exists():
            licencia_data = LicenciasConducir.objects.filter(user=empleado)
            licencia_data.delete()
    except:
        pass
    return etapa_2(request)

@login_required(login_url = '/login/')
def confirma_etapa_2(request, template_name = "dashboard/dashboard.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 4
        empleado.save()
    except:
        pass
    return portafolio(request)
# ========= FIN ETAPA 2 ==========

# ========= INICIO ETAPA 3 ==========
@login_required(login_url = '/login/')
def etapa_3(request, template_name = "empleados/etapa_3.html"):
    usuario = request.user
    empleado = Empleado.objects.get(user = request.user)
    if request.method == 'POST':
        formEstadoCivil = EstadoCivil(request.POST)
        if formEstadoCivil.is_valid():
            estadocivil = formEstadoCivil.cleaned_data['estado_civil']
            empleado.estado_civil = estadocivil
            #empleado.save()
        else:
            formEstadoCivil.errors
            print(formEstadoCivil.errors)

        if estadocivil != 'Soltero(a)' and estadocivil != 'Viudo(a)':
            formConyugue = FormConyugue(request.POST, request.FILES)
            if formConyugue.is_valid():
                conyugue = formConyugue.save(commit=False)
                conyugue.user = empleado
                conyugue.save()
                conyugue_saved = Conyugue.objects.get(user = empleado)
                try:
                    if conyugue_saved.nombre == '':
                        conyugue_saved.delete()
                except:
                    pass
            else:
                formConyugue.errors
                print(formConyugue.errors)
        
        formConyugue = FormConyugue()
        formEstadoCivil = EstadoCivil()
        formPreguntas = PreguntasEtapa3()
        formSiNo = ExtranjeroSiNo()
        empleado.status = 5
        empleado.save()
    else:
        #Buscar datos en modelo Candidatos
        formConyugue=set_Candvalues_etapa3(usuario)
        #formConyugue = FormConyugue()
        formEstadoCivil=set_Candvalues_etapa3_civil(usuario)
        #formEstadoCivil = EstadoCivil()
        formConyugue.fields['acta'].widget.attrs['accept'] ='image/*'
        formConyugue.fields['acta_nacimiento'].widget.attrs['accept'] ='image/*'
        if (formEstadoCivil.fields['estado_civil']=='Soltero(a)') or (formEstadoCivil.fields['estado_civil']=='Viudo(a)'):
            es_soltero=True
        else:
            es_soltero=False
            if (formEstadoCivil.fields['estado_civil']=='Casado(a)'):
                es_casado=True
            else:
                es_casado=False
            

    return render(request, template_name, locals(),)

@login_required(login_url = '/login/')
def rechaza_etapa_3(request, template_name = "empleados/etapa_3.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 4
        empleado.save()
        if Conyugue.objects.filter(user = empleado).exists():
            conyugue_saved = Conyugue.objects.filter(user = empleado)
            conyugue_saved.delete()
    except:
        pass
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 4
        empleado.save()
        if Preguntas.objects.filter(user = empleado).exists():
            preguntas_saved = Preguntas.objects.filter(user = empleado).filter(user = empleado)
            preguntas_saved.delete()
    except:
        pass
    return etapa_3(request)

@login_required(login_url = '/login/')
def confirma_etapa_3(request, template_name = "dashboard/dashboard.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 6
        empleado.save()
    except:
        pass
    return portafolio(request)
# ========= FIN ETAPA 3 ==========

# ========= INICIO ETAPA 4 ==========
@login_required(login_url = '/login/')
def etapa_4(request, template_name = "empleados/etapa_4.html"):
    usuario = request.user
    tiene_hijo = False
    empleado = Empleado.objects.get(user = usuario.pk)
    if request.method == 'POST':
        try:
            formCantidadHijos = numero_hijos(request.POST)
            HijoFormSet = formset_factory(FormHijos, extra = empleado.numero_hijos)
            formsetHijos = HijoFormSet(request.POST)
            if formCantidadHijos.is_valid():
                print("entro formcantidad")
                empleado.numero_hijos = formCantidadHijos.cleaned_data['cantidad']
                print(empleado.numero_hijos)
                empleado.status = 7
                empleado.save()
            if formsetHijos.is_valid():
                print("entro formhijos")
                for form in formsetHijos:
                    nuevo_hijo = Hijo(
                        user_id=empleado.pk,
                        nombre=form['nombre'].value(),
                        apellido_paterno=form['apellido_paterno'].value(),
                        apellido_materno=form['apellido_materno'].value(),
                        edad=form['edad'].value(),
                        fecha_nacimiento=form['fecha_nacimiento'].value())
                    nuevo_hijo.save()

            if empleado.numero_hijos > 0:
                print("entro num hijos")
                tiene_hijo = True
            else:
                tiene_hijo = False
                formCantidadHijos = numero_hijos()
        except Exception as e:
            
            print(e)
        return HttpResponseRedirect('/etapa-4/')
    else:
        if empleado.numero_hijos > 0:
            tiene_hijos = True
            if Hijo.objects.filter(user=empleado).exists():
                hijos_registrados = Hijo.objects.filter(user=empleado)
            HijoFormSet = formset_factory(FormHijos, extra = empleado.numero_hijos)
            formset = HijoFormSet()
        #buscar numero de hijos en Candidato
        formCantidadHijos = numero_hijos()
    return render(request, template_name, locals(),)

@login_required(login_url = '/login/')
def rechaza_etapa_4(request, template_name = "empleados/etapa_4.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 6
        empleado.numero_hijos = 0
        empleado.save()
        if Hijo.objects.filter(user=empleado).exists():
            hijos_registrados = Hijo.objects.filter(user=empleado)
            hijos_registrados.delete()
    except:
        pass
    return etapa_4(request)


@login_required(login_url = '/login/')
def confirma_etapa_4(request, template_name = "dashboard/dashboard.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 8
        empleado.save()
    except:
        pass
    return portafolio(request)
# ========= FIN ETAPA 4 ==========

# ========= INICIO ETAPA 5 ==========
@login_required(login_url = '/login/')
def etapa_5(request, template_name = "empleados/etapa_5.html"):
    usuario = request.user
    empleado = Empleado.objects.get(user=usuario.pk)
    if request.method == 'POST':
        try:
            Formulario_estudios = EstudiosForm(request.POST, request.FILES)
            Formulario_cursos = CapacitacionForm(request.POST, request.FILES)
            Formulario_idiomas = IdiomasForm(request.POST)
            if Formulario_estudios.is_valid():
                Estudios = Formulario_estudios.save(commit=False)
                Estudios.user = empleado
                empleado.status = 9  # Estudios y niveles cargados
                empleado.save()
                Estudios.save()
                # PARA 9
                estudios = Estudio.objects.get(user = usuario.pk)
            if Formulario_cursos.is_valid():
                cursos = Formulario_cursos.save(commit=False)
                cursos.user = empleado
                cursos.save()
                cursos = Capacitaciones.objects.filter(user=empleado)
            if Formulario_idiomas.is_valid():
                idiomas = Formulario_idiomas.save(commit=False)
                idiomas.user = empleado
                idiomas.save()
                idiomas = Idioma.objects.filter(user=empleado)
            if Estudio.objects.filter(user = usuario.pk).exists():
                estudios = Estudio.objects.get(user=usuario.pk)
                if (estudios.constacia_de_estudio):
                    extension = estudios.constacia_de_estudio.url
                    filename, extension_constancia = os.path.splitext(extension)
                if estudios.cedula_profesional.imagen_cedula_profesional:
                    extension = estudios.cedula_profesional.imagen_cedula_profesional.url
                    filename, extension_cedula = os.path.splitext(extension)
            if Capacitaciones.objects.filter(user=empleado).exists():
                cursos = Capacitaciones.objects.filter(user=empleado)
            if Idioma.objects.filter(user=empleado).exists():
                idiomas = Idioma.objects.filter(user=empleado)
            Formulario = EstudiosForm()
            
            
            Cursos = CapacitacionForm()
            Cursos.fields['certificado'].widget.attrs['accept'] ='image/*'
            Idiomas = IdiomasForm()
        except:
            print("Error al guardar datos")
    else:
        if Estudio.objects.filter(user = usuario.pk).exists():
            estudios = Estudio.objects.get(user=usuario.pk)
            if (estudios.constacia_de_estudio):
                extension = estudios.constacia_de_estudio.url
                filename, extension_constancia = os.path.splitext(extension)
            if estudios.cedula_profesional.imagen_cedula_profesional:
                extension = estudios.cedula_profesional.imagen_cedula_profesional.url
                filename, extension_cedula = os.path.splitext(extension)
        if Capacitaciones.objects.filter(user=empleado).exists():
            cursos = Capacitaciones.objects.filter(user=empleado)
        if Idioma.objects.filter(user=empleado).exists():
            idiomas = Idioma.objects.filter(user=empleado)
        Formulario = EstudiosForm()
        
        Formulario.fields['cedula_profesional_imagen_cedula_profesional'].widget.attrs['accept'] ='image/*'
        Formulario.fields['constacia_de_estudio'].widget.attrs['accept'] ='image/*'
        #Formulario.fields['cedula_profesional_cedula'].widget.attrs['data-mask'] ="9999999"
        #Formulario.fields['cedula_profesional_cedula'].widget.attrs['maxlength'] ='8'

        Cursos = CapacitacionForm()
        Cursos.fields['certificado'].widget.attrs['accept'] ='image/*'
        Idiomas = IdiomasForm()
    return render(request, template_name, locals(),)

@login_required(login_url = '/login/')
def rechaza_etapa_5_status_9(request, template_name = "empleados/etapa_4.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 8
        empleado.save()
        if Estudio.objects.filter(user=empleado).exists():
            estudios_registrados = Estudio.objects.filter(user=empleado)
            estudios_registrados.delete()
    except:
        pass
    return etapa_5(request)

@login_required(login_url = '/login/')
def confirma_etapa_5_status_9(request, template_name = "empleados/etapa_4.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 10
        empleado.save()
    except:
        pass
    return etapa_5(request)

@login_required(login_url = '/login/')
def borrar_curso(request, id, template_name = "empleados/etapa_4.html"):
    usuario = request.user
    try:
        curso = Capacitaciones.objects.filter(pk = id)
        curso.delete()
        curso.save()
    except:
        pass
    return etapa_5(request)

@login_required(login_url = '/login/')
def borrar_idioma(request, id, template_name = "empleados/etapa_4.html"):
    usuario = request.user
    try:
        idioma = Idioma.objects.filter(pk = id)
        idioma.delete()
        idioma.save()
    except:
        pass
    return etapa_5(request)

       

@login_required(login_url = '/login/')
def confirma_etapa_5_status_10(request, template_name = "empleados/etapa_4.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 11
        empleado.save()
    except:
        pass
    return etapa_5(request)

@login_required(login_url = '/login/')
def confirma_etapa_5_status_11(request, template_name = "empleados/etapa_4.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 12
        empleado.save()
    except:
        pass
    return etapa_5(request)

@login_required(login_url = '/login/')
def confirma_etapa_5(request, template_name = "dashboard/dashboard.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 13
        empleado.save()
    except:
        pass
    return portafolio(request)

@login_required(login_url = '/login/')
def rechaza_etapa_5(request, template_name = "empleados/etapa_4.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 8
        empleado.save()
        if Estudio.objects.filter(user=empleado).exists():
            estudios_registrados = Estudio.objects.filter(user=empleado)
            estudios_registrados.delete()
        if Capacitaciones.objects.filter(user=empleado).exists():
            cursos = Capacitaciones.objects.filter(user=empleado)
            cursos.delete()
        if Idioma.objects.filter(user=empleado).exists():
            idiomas = Idioma.objects.filter(user=empleado)
            idiomas.delete()
    except:
        pass
    return etapa_5(request)
# ========= FIN ETAPA 5 ==========

# ========= INICIO ETAPA 6 ==========
@login_required(login_url = '/login/')
def etapa_6(request, template_name = "empleados/etapa_6.html"):
    usuario = request.user
    empleado = Empleado.objects.get(user=usuario.pk)
    if request.method == 'POST':
        domicilios_post = DomicilioForm(request.POST, request.FILES)
        recomendaciones = formset_factory(RecomendacionesForm, extra = 2)
        recomendaciones_post = recomendaciones(request.POST, request.FILES)
        bancos_post = BancoForm(request.POST, request.FILES)
        try:
            if domicilios_post.is_valid():
                Domicilios = domicilios_post.save(commit=False)
                Domicilios.user = empleado
                Domicilios.save()
            if recomendaciones_post.is_valid():
                for form in recomendaciones_post:
                    if form.has_changed():
                        form = form.save(commit=False)
                        form.user = empleado
                        form.save()
            if bancos_post.is_valid():
                Bancos = bancos_post.save(commit=False)
                Bancos.user = empleado
                Bancos.save()
            empleado.status = 14
            empleado.save()
        except:
            print("ERROR AL GURADAR DATOS")
        domicilio_datos = Domicilio.objects.get(user=empleado)
        if Recomendaciones.objects.filter(user=empleado).exists():
            recomendaciones_datos = Recomendaciones.objects.filter(user=empleado)
        banco_datos = Banco.objects.get(user=empleado)
        domicilios = DomicilioForm()
        recomendaciones = formset_factory(RecomendacionesForm, extra = 2)
        recomendaciones_formset = recomendaciones()
        bancos = BancoForm()
    else:
        if Domicilio.objects.filter(user=empleado).exists():
            domicilio_datos = Domicilio.objects.get(user=empleado)
        if Recomendaciones.objects.filter(user=empleado).exists():
            recomendaciones_datos = Recomendaciones.objects.filter(user=empleado)
        if Banco.objects.filter(user=empleado).exists():
            banco_datos = Banco.objects.get(user=empleado)
        domicilios = DomicilioForm()
        domicilios.fields['comprobante_domicilio'].widget.attrs['accept'] ='image/*'
        
        recomendaciones = formset_factory(RecomendacionesForm, extra = 2)
        recomendaciones_formset = recomendaciones()
        
        bancos = BancoForm()
        bancos.fields['contrato'].widget.attrs['accept'] ='image/*'
        
        domicilios.fields['tlf_residencial'].widget.attrs['data-mask'] ="(99) 9999-9999)"
    return render(request, template_name, locals(),)

@login_required(login_url = '/login/')
def rechaza_etapa_6(request, template_name = "empleados/etapa_6.html"):
    usuario = request.user
    empleado = Empleado.objects.get(user=usuario.pk)
    try:
        domicilio_datos = Domicilio.objects.get(user=empleado)
        if Recomendaciones.objects.filter(user=empleado).exists():
            recomendaciones_datos = Recomendaciones.objects.filter(user=empleado)
        banco_datos = Banco.objects.get(user=empleado)
        domicilio_datos.delete()
        recomendaciones_datos.delete()
        banco_datos.delete()
        empleado.status = 13
        empleado.save()
    except:
        pass
    return etapa_6(request)

@login_required(login_url = '/login/')
def confirma_etapa_6(request, template_name = "dashboard/dashboard.html"):
    usuario = request.user
    try:
        empleado = Empleado.objects.get(user = usuario.pk)
        empleado.status = 15
        empleado.save()
    except:
        pass
    return portafolio(request) 
    







###############################
@login_required(login_url = '/login/')
def admconfirma_etapa_1(request, id, template_name = "dashboard/dashboardAdm.html"):
    try:
        empleado = Empleado.objects.get(user_id = id)
        usuario = User.objects.get(id = empleado.pk)
        empleado.save()
    except:
        pass
    return render(request, 'dashboard/dashboardAdm.html', { 'id': 1,'usuario':usuario,'empleado':empleado},)

@login_required(login_url = '/login/')
def admperfil(request,id, template_name = "empleados/perfiladm.html"):
    #print("Regreso "+id)
    try:
        empleado = Empleado.objects.get(user_id = id) 
        foto = 1
    except:
        foto = 0  
    if request.method == 'POST':
             print("POST")
    else:
        try:
            empleado = Empleado.objects.get(user_id=id)
            usuario= User.objects.get(id = empleado.pk)
            nacionalidades = Nacionalidad.objects.filter(user=empleado)
            form = set_values(usuario)
            form.fields['nombre'].widget.attrs['readonly'] =True
            #form.fields['nombre'].widget.attrs["required"] ="required"
            form.fields['apellido_paterno'].widget.attrs['readonly'] =True
            form.fields['apellido_materno'].widget.attrs['readonly'] =True
            form.fields['edad'].widget.attrs['readonly'] =True
            form.fields['pais_nacimiento'].widget.attrs['readonly'] =True
            form.fields['fecha_nacimiento'].widget.attrs['readonly'] =True
            form.fields['tipo'].widget.attrs['readonly'] =True
            form.fields['calle'].widget.attrs['readonly'] =True
            form.fields['num_ext'].widget.attrs['readonly'] =True
            form.fields['num_int'].widget.attrs['readonly'] =True
            form.fields['piso'].widget.attrs['readonly'] =True
            form.fields['depto'].widget.attrs['readonly'] =True
            form.fields['calle_uno'].widget.attrs['readonly'] =True
            form.fields['calle_dos'].widget.attrs['readonly'] =True
            form.fields['tel'].widget.attrs['readonly'] =True
            form.fields['cel'].widget.attrs['readonly'] =True
            form.fields['email_personal'].widget.attrs['readonly'] =True
            form.fields['cp'].widget.attrs['readonly'] =True
            form.fields['colonia'].widget.attrs['readonly'] =True
            form.fields['esdo'].widget.attrs['readonly'] =True
            form.fields['pais_direc'].widget.attrs['readonly'] =True
            form.fields['referencia'].widget.attrs['readonly'] =True
            form.fields['colonia'].widget.attrs['readonly'] =True

            form.fields['tipo_documento_identidad'].widget.attrs['readonly'] =True
            form.fields['pasaporte'].widget.attrs['readonly'] =True
            form.fields['fecha_vencimiento_pasaporte'].widget.attrs['readonly'] =True
            
            form.fields['foto'].widget.attrs['accept'] ='image/*'
            form.fields['acta_nacimiento'].widget.attrs['accept'] ='image/*'
            form.fields['docu_ident_front'].widget.attrs['accept'] ='image/*'
            form.fields['docu_ident_back'].widget.attrs['accept'] ='image/*'
            #form.fields['imagen_pasaporte'].widget.attrs['accept'] ='image/*'

            #form.nombre.widget
        except:
            print("No existe")
          
    return render(request, template_name, locals(),)

@login_required(login_url = '/login/')
def admetapa_2(request,id, template_name = "empleados/admetapa_2.html"):
    
    try:
        empleado = Empleado.objects.get(user_id = id) 
        foto = 1
    except:
        foto = 0  
    if request.method == 'POST':
        print("POST")
    else:
        try:
            empleado = Empleado.objects.get(user_id=id)
            #pais = Country.objects.get()
            formVisas = VisasForm()
            usuario= User.objects.get(id = empleado.pk)
            if visas.objects.filter(user=empleado).exists():
                todas_visas = visas.objects.filter(user=empleado)
            if LicenciasConducir.objects.filter(user=empleado).exists():
                lic = LicenciasConducir.objects.get(user = usuario.pk)
                #licencia_data = LicenciasConducir.objects.filter(user=empleado)
                #print(lic)
            form = set_values_2(usuario)
            form.fields['curp'].widget.attrs['readonly'] =True
            form.fields['rfc'].widget.attrs['readonly'] =True
            form.fields['sat'].widget.attrs['readonly'] =True
            form.fields['imss'].widget.attrs['readonly'] =True
            form.fields['infonavit'].widget.attrs['readonly'] =True
            form.fields['licencia_conducir'].widget.attrs['readonly'] =True
            form.fields['estado_emision_licencia'].widget.attrs['readonly'] =True
            form.fields['vigencia_licencia_conducir'].widget.attrs['readonly'] =True
            form.fields['permanente'].widget.attrs['readonly'] =True
            formVisas.fields['pais'].widget.attrs['style']='display:none'
            
            form.fields['imagen_curp'].widget.attrs['accept'] ='image/*'
            form.fields['imagen_rfc'].widget.attrs['accept'] ='image/*'
            form.fields['imagen_sat'].widget.attrs['accept'] ='image/*'
            form.fields['imagen_imss'].widget.attrs['accept'] ='image/*'
            form.fields['imagen_infonavit'].widget.attrs['accept'] ='image/*'
            form.fields['img_lic_anverso'].widget.attrs['accept'] ='image/*'
            form.fields['img_lic_reverso'].widget.attrs['accept'] ='image/*'
            formVisas.fields['imagen_visa'].widget.attrs['accept'] ='image/*'
            
            #formlic= FormLic()
        except Exception as e:
            print(e) 
        #except:
        #    print("No existe")
    return render(request, template_name, locals(),)

@login_required(login_url = '/login/')
def admetapa_3(request,id, template_name = "empleados/admetapa_3.html"):
    
    try:
        empleado = Empleado.objects.get(user_id = id) 
        foto = 1
    except:
        foto = 0  
    if request.method == 'POST':
        print("POST")
    else:
        try:
            #formConyugue = FormConyugue()
            usuario= User.objects.get(id = empleado.pk)
            formConyugue=set_values_conyugue(empleado)
            formConyugue.fields['nombre'].widget.attrs['readonly'] =True
            formConyugue.fields['apellido_paterno'].widget.attrs['readonly'] =True
            formConyugue.fields['apellido_materno'].widget.attrs['readonly'] =True
            formConyugue.fields['fecha_nacimiento'].widget.attrs['readonly'] =True
            formConyugue.fields['profesion'].widget.attrs['readonly'] =True
            formConyugue.fields['lugar_de_trabajo'].widget.attrs['readonly'] =True
            formConyugue.fields['tlf'].widget.attrs['readonly'] =True
            formConyugue.fields['email'].widget.attrs['readonly'] =True
            formConyugue.fields['email_trabajo'].widget.attrs['readonly'] =True
            formConyugue.fields['acta'].widget.attrs['accept'] ='image/*'
            formConyugue.fields['acta_nacimiento'].widget.attrs['accept'] ='image/*'
            
            formPreguntas = set_values_preguntas(empleado)
            formPreguntas.fields['extranjero'].widget.attrs['readonly'] =True
            formPreguntas.fields['fecha_llegada'].widget.attrs['readonly'] =True
            formPreguntas.fields['permiso_trabajo'].widget.attrs['readonly'] =True
            formPreguntas.fields['solicitud_permiso_trabajo'].widget.attrs['readonly'] =True
            
            formEstadoCivil = EstadoCivil()
            
            #formPreguntas = PreguntasEtapa3()
            
            formSiNo = ExtranjeroSiNo()
            #formSiNo
            conyugue_saved = Conyugue.objects.get(user = empleado)
            preguntas_saved = Preguntas.objects.get(user = empleado)
        except Exception as e:
            print(e)
        #except:
            #print("No existe")
    return render(request, template_name, locals(),)


@login_required(login_url = '/login/')
def admetapa_4(request,id, template_name = "empleados/admetapa_4.html"):
    try:
        empleado = Empleado.objects.get(user_id = id) 
        foto = 1
    except:
        foto = 0  
    if request.method == 'POST':
        print("POST")
    else:
        try:
             usuario= User.objects.get(id = empleado.pk)
             if empleado.numero_hijos > 0:
                 tiene_hijos = True
                 if Hijo.objects.filter(user=empleado).exists():
                     hijos_registrados = Hijo.objects.filter(user=empleado)
                 #HijoFormSet = formset_factory(FormHijos, extra = empleado.numero_hijos)
                 formset = FormHijos()
                 formhijo =FormHijos()
             formCantidadHijos = numero_hijos()
        except:
            print("No existe")
    return render(request, template_name, locals(),)

@login_required(login_url = '/login/')
def admetapa_5(request,id, template_name = "empleados/admetapa_5.html"):
    try:
        empleado = Empleado.objects.get(user_id = id) 
        foto = 1
    except:
        foto = 0  
    if request.method == 'POST':
        print("POST")
    else:
        try:
            usuario= User.objects.get(id = id)
            if Estudio.objects.filter(user = usuario.pk).exists():
                  estudios = Estudio.objects.get(user=usuario.pk)
                  if (estudios.constacia_de_estudio):
                      extension = estudios.constacia_de_estudio.url
                      filename, extension_constancia = os.path.splitext(extension)
                  if estudios.cedula_profesional.imagen_cedula_profesional:
                      extension = estudios.cedula_profesional.imagen_cedula_profesional.url
                      filename, extension_cedula = os.path.splitext(extension)
            if Capacitaciones.objects.filter(user=empleado).exists():
                cursos = Capacitaciones.objects.filter(user=empleado)
            if Idioma.objects.filter(user=empleado).exists():
                idiomas = Idioma.objects.filter(user=empleado)
            Formulario = set_values_estudios(empleado)
            Formulario.fields['nivel_estudios'].widget.attrs['readonly'] =True
            Formulario.fields['universidad'].widget.attrs['readonly'] =True
            Formulario.fields['titulo'].widget.attrs['readonly'] =True
            Formulario.fields['carrera'].widget.attrs['readonly'] =True
            Formulario.fields['cedula_profesional_cedula'].widget.attrs['readonly'] =True
            
            Cursos = CapacitacionForm()
            Cursos.fields['certificado'].widget.attrs['required'] =False
            Cursos2 = CapacitacionForm()
            Cursos2.fields['certificado'].widget.attrs['required'] =False
            Cursos.fields['tipo_curso'].widget.attrs['style']='display:none'
            #Cursos.fields['tipo_curso'].widget.attrs['readonly'] =True
            Idiomas = IdiomasForm()
            Idiomas2 = IdiomasForm()
            Idiomas.fields['nivel_escrito'].widget.attrs['style']='display:none'
            Idiomas.fields['nivel_hablado'].widget.attrs['style']='display:none'
        except Exception as e:
            print(e) 
        #except:
        #    print("No existe")
    return render(request, template_name, locals(),)

@login_required(login_url = '/login/')
def admetapa_6(request,id, template_name = "empleados/admetapa_6.html"):
    try:
        empleado = Empleado.objects.get(user_id = id) 
        foto = 1
    except:
        foto = 0  
    if request.method == 'POST':
        print("POST")
    else:
        try:
           usuario= User.objects.get(id = empleado.pk)
           if Domicilio.objects.filter(user=empleado).exists():
               domicilio_datos = Domicilio.objects.get(user=empleado)
           if Recomendaciones.objects.filter(user=empleado).exists():
               recomendaciones_datos = Recomendaciones.objects.filter(user=empleado)
           if Banco.objects.filter(user=empleado).exists():
               banco_datos = Banco.objects.get(user=empleado)
           #domicilios = DomicilioForm()
           domicilios = set_values_comprobante(empleado)
           domicilios.fields['tipo_comprobante'].widget.attrs['readonly'] =True
           
           domicilios.fields['tlf_residencial'].widget.attrs['data-mask'] ="(99)9999-9999"
           #domicilios.fields['tlf_residencial'].widget.attrs['readonly'] =True
           bancos = set_values_banco(empleado)
           bancos.fields['banco'].widget.attrs['readonly'] =True
           bancos.fields['clabe'].widget.attrs['readonly'] =True
           #recomendaciones = formset_factory(RecomendacionesForm, extra = 2)
           recomendaciones_formset = RecomendacionesForm()
           
        except:
            print("No existe")
    return render(request, template_name, locals(),)


# Inicia funciones de actualizar

def update_bas(request):
    
    emp_id = request.POST.get('userId')
    nombre = request.POST["nombre"]
    paterno = request.POST["apellido_paterno"]
    materno = request.POST["apellido_materno"]
    fecha_nacimiento=''
    if (not request.POST['fecha_nacimiento'] in [None,'']):
        fecha_nacimiento = datetime.strptime(request.POST['fecha_nacimiento'], '%d/%m/%Y').strftime('%Y-%m-%d')
    pais_nacimiento = request.POST['pais_nacimiento']
    pais_nacimiento = Country.objects.get(pk=pais_nacimiento)
    edad = request.POST["edad"]
    tel = request.POST["tel"]
    cel = request.POST["cel"]
    email_personal = request.POST["email_personal"]
    #direccion = request.POST["direccion"]
    tipo = request.POST["tipo"]
    calle = request.POST["calle"]
    num_ext = request.POST["num_ext"]
    num_int = request.POST["num_int"]
    calle_uno = request.POST["calle_uno"]
    calle_dos = request.POST["calle_dos"]
    piso = request.POST["piso"]
    depto = request.POST["depto"]
    cp = request.POST["cp"]
    colonia = request.POST["colonia"]
    esdo = request.POST["esdo"]
    pais_direc = request.POST["pais_direc"]
    pais_direc = Country.objects.get(pk=pais_direc)
    referencia = request.POST["referencia"]

    if "foto" not in request.FILES:
        foto=False
    else:
        foto = request.FILES['foto']
    #print("foto")
    if "acta_nacimiento" not in request.FILES:
        acta_nacimiento=False
    else:
        acta_nacimiento = request.FILES['acta_nacimiento']
    #print(request.POST)
    
    # Actualizamos seccion uno etapa uno
            
    response=""
    try:
        empleado= Empleado.objects.get(user_id=emp_id)
        empleado.nombre = nombre
        empleado.apellido_paterno = paterno
        empleado.apellido_materno = materno
        empleado.fecha_nacimiento = fecha_nacimiento
        #empleado.pasaporte_valido = fecha_vencimiento_pasaporte
        empleado.pais_nacimiento = pais_nacimiento
        empleado.edad = edad
        empleado.tel = tel
        empleado.cel = cel
        empleado.email_personal = email_personal
        #empleado.direccion = direccion
        empleado.tipo = tipo
        empleado.calle = calle
        empleado.num_ext = num_ext
        empleado.num_int = num_int
        empleado.calle_uno = calle_uno
        empleado.calle_dos = calle_dos
        empleado.piso = piso
        empleado.depto = depto
        empleado.cp = cp
        empleado.colonia = colonia
        empleado.esdo = esdo
        empleado.pais_direc = pais_direc
        empleado.referencia=referencia
        if (foto):
            empleado.foto=foto
        if (acta_nacimiento):
            empleado.acta_nacimiento = acta_nacimiento
        empleado.save()
        response="OK"
    #except:
    #   response="error"
    except Exception as e:
        print(e)
    return HttpResponse(response)


def update_nac(request):
    response=""
    try:
        #form = Formulario1(request.POST, request.FILES)
        emp_id = request.POST.get('userId')
        pasaporte=0
        if (not request.POST['pasaporte'] in [None,'']):
            pasaporte = request.POST["pasaporte"]
        vencimiento=None
        if (not request.POST['fecha_vencimiento_pasaporte'] in [None,'']):
            vencimiento = datetime.strptime(request.POST['fecha_vencimiento_pasaporte'], '%d/%m/%Y').strftime('%Y-%m-%d')
        #vencimiento = datetime.strptime(request.POST['fecha_vencimiento_pasaporte'], '%d/%m/%Y').strftime('%Y-%m-%d')
        
        if "nacionalidad" not in request.POST:
            nacionalidad=False
        else:
            
            #nacionalidad = form.cleaned_data["nacionalidad"]
            nacionalidad = request.POST['nacionalidad']
            #nacionalidad = request.POST.getlist("nacionalidad")
            
        tipo_documento_identidad_valor = TipoDocumentoIdentidad.objects.get(pk=request.POST['tipo_documento_identidad'])
        if "docu_ident_front" not in request.FILES:
            docu_ident_front=False
        else:
            docu_ident_front = request.FILES['docu_ident_front']
        if "docu_ident_back" not in request.FILES:
            docu_ident_back=False
        else:
            docu_ident_back = request.FILES['docu_ident_back']
        if "imagen_pasaporte" not in request.FILES:
            imagen_pasaporte=False
        else:
            imagen_pasaporte = request.FILES['imagen_pasaporte']
        
        empleado= Empleado.objects.get(user_id=emp_id)
        
        empleado.pasaporte = pasaporte
        
        
        empleado.pasaporte_valido = vencimiento
        
        empleado.tipo_documento_identidad = tipo_documento_identidad_valor
        if (docu_ident_front):
            empleado.docu_ident_front=docu_ident_front
        if (docu_ident_back):
            empleado.docu_ident_back=docu_ident_back
        if (imagen_pasaporte):
            empleado.imagen_pasaporte=imagen_pasaporte

        empleado.save()
        if (nacionalidad):
            naciones = Nacionalidad.objects.filter(user_id = emp_id)
            naciones.delete()
            empleado = Empleado.objects.get(user_id=emp_id)
            for dato in nacionalidad:
                objeto_pais = Country.objects.get(id=dato)
                if objeto_pais:
                    nacionalidad = Nacionalidad(user=empleado,pais=objeto_pais)
                    nacionalidad.save()
        response="OK"
    except Exception as e:
        print(e)
        response="error"
        #except:
        #    response="error"
    return HttpResponse(response)


def update_doc(request):
    emp_id = request.POST.get('userId')
    curp = request.POST["curp"]
    rfc = request.POST["rfc"]
    sat = request.POST["sat"]
    imss = request.POST["imss"]
    infonavit = request.POST["infonavit"]
    #licencia = request.POST['licencia_conducir']
    if "imagen_curp" not in request.FILES:
        imagen_curp=False
    else:
        imagen_curp = request.FILES['imagen_curp']
    if "imagen_rfc" not in request.FILES:
        imagen_rfc=False
    else:
        imagen_rfc = request.FILES['imagen_rfc']
    if "imagen_sat" not in request.FILES:
        imagen_sat=False
    else:
        imagen_sat = request.FILES['imagen_sat']
    if "imagen_imss" not in request.FILES:
        imagen_imss=False
    else:
        imagen_imss = request.FILES['imagen_imss']
    if "imagen_infonavit" not in request.FILES:
        imagen_infonavit=False
    else:
        imagen_infonavit = request.FILES['imagen_infonavit']
    response=""
  
    if emp_id is not None:
        try:
            empleado= Empleado.objects.get(user_id=emp_id)
            empleado.curp = curp
            empleado.rfc = rfc
            empleado.sat = sat
            empleado.imss = imss
            empleado.infonavit = infonavit
            if (imagen_curp):
                empleado.imagen_curp=imagen_curp
            if (imagen_rfc):
                empleado.imagen_rfc=imagen_rfc
            if (imagen_sat):
                empleado.imagen_sat=imagen_sat
            if (imagen_imss):
                empleado.imagen_imss=imagen_imss
            if (imagen_infonavit):
                empleado.imagen_infonavit=imagen_infonavit  
            empleado.save()
            ####
            print("grabo empleado") 
            
            response="OK"
        except Exception as e:
            print(e)  
        #except:
     #     response="error"
           
    return HttpResponse(response)

def update_vis(request):
    
    visaId = request.POST.get('visaId')
    pais = request.POST['pais']
    pais = Country.objects.get(pk=pais)
    
    fecha = datetime.strptime(request.POST['fecha_vigencia'], '%d/%m/%Y').strftime('%Y-%m-%d')
    #request.POST.get('fecha_vigencia').strftime('%Y-%m-%d')
    
    if ("id_imagen_vigencia" not in request.FILES):
        imagen_vigencia =False
    else:
        imagen_vigencia = request.POST.FILES['id_imagen_vigencia']
    
    response=""
   
    #if emp_id is not None:
    try:
        #empleado= Empleado.objects.get(user_id=emp_id)
        visa= visas.objects.get(id=visaId)
        visa.pais=pais
        visa.fecha_vigencia=fecha
        if(imagen_vigencia):
            visa.imagen_visa=imagen_vigencia
         
        visa.save()
        response="OK"
    except Exception as e:
            print(e) 
            response="error"       
    #except:
    #    response="error"
           
    return HttpResponse(response)

def update_esdo(request):
    emp_id = request.POST.get('userId')
   
    response=""
 
    if emp_id is not None:
        try:
            empleado= Empleado.objects.get(user_id=emp_id)
         
            empleado.save()
            response="OK"
         
        except:
            response="error"
           
    return HttpResponse(response)

def update_ext(request):
    emp_id = request.POST.get('userId')
    
   
    response=""
   
    if emp_id is not None:
        try:
            empleado= Empleado.objects.get(user_id=emp_id)
           
            empleado.save()
            response="OK"
           
        except:
            response="error"
           
    return HttpResponse(response)

def update_hijo(request):
    print(request.POST)
    
    #emp_id = request.POST.get('userId')
    hijoId = request.POST.get('Id')
    nombre = request.POST.get('nombre')
    paterno = request.POST.get('apellido_paterno')
    materno = request.POST.get('apellido_materno')
    fecha = datetime.strptime(request.POST['fecha_nacimiento'], '%d/%m/%Y').strftime('%Y-%m-%d')
    #fecha = request.POST.get('fecha_nacimiento')
    edad = request.POST.get('edad')
    #annio = request.POST.get('fecha_nacimiento_year')
    #mes = request.POST.get('fecha_nacimiento_month')
    #dia = request.POST.get('fecha_nacimiento_day')
    #fecha=annio+'-'+mes+'-'+dia
    response=""
    try:
        hijo= Hijo.objects.get(id=hijoId)
        hijo.nombre=nombre
        hijo.apellido_paterno=paterno
        hijo.apellido_materno=materno
        hijo.fecha_nacimiento=fecha
        hijo.edad=edad
        hijo.save()
        response="OK"
    except Exception as e:
        print(e)    
        response="error"
        #except:
        #    response="error"
           
    return HttpResponse(response)

def add_hijo(request):
    emp_id = request.POST.get('userId')
    nombre = request.POST.get('nombre')
    paterno = request.POST.get('apellido_paterno')
    materno = request.POST.get('apellido_materno')
    annio = request.POST.get('fecha_nacimiento_year')
    mes = request.POST.get('fecha_nacimiento_month')
    dia = request.POST.get('fecha_nacimiento_day')
    fecha=annio+'-'+mes+'-'+dia
    edad = request.POST.get('edad')
   
    response=""
  
    if emp_id is not None:
        try:
            empleado= Empleado.objects.get(user_id=emp_id)
            empleado.numero_hijos=empleado.numero_hijos+1
            empleado.save()
            nuevo_hijo = Hijo(
                user_id=empleado.pk,
                nombre=nombre,
                apellido_paterno=paterno,
                apellido_materno=materno,
                edad=edad,
                fecha_nacimiento=fecha)
            nuevo_hijo.save()
            response="OK"
        except Exception as e:
            print(e)    
        #except:
        #    response="error"
           
    return HttpResponse(response)

def update_sec1(request):
    print(request.POST)
    print(request.FILES)
    emp_id = request.POST.get('userId')
    n_estudios = request.POST.get('nivel_estudios')
    print(n_estudios)
    uni = request.POST.get('universidad')
    tit = request.POST.get('titulo')
    carr = request.POST.get('carrera')
    ced = request.POST.get('cedula_profesional_cedula')
    if ("cedula_profesional_imagen_cedula_profesional" not in request.FILES):
        imagen_cedula =False
    else:
        imagen_cedula = request.FILES['cedula_profesional_imagen_cedula_profesional']
    if ("constancia_de_estudio" not in request.FILES):
        imagen_constancia =False
    else:
        imagen_constancia = request.FILES['constancia_de_estudio']
    
   
    response="error"
   
    if emp_id is not None:
        try:
            #empleado= Empleado.objects.get(user_id=emp_id)
            estudio= Estudio.objects.get(user_id=emp_id)
            estudio.nivel_estudio=n_estudios
            estudio.universidad=uni
            estudio.titulo=tit
            estudio.carrera=carr
            estudio.cedula_profesional_cedula=ced
            if(imagen_cedula):
                estudio.cedula_profesional_imagen_cedula_profesional=imagen_cedula
            if(imagen_constancia):
                estudio.constancia_de_estudio=imagen_constancia
            #estudio.save()
            response="OK"
        except Exception as e:
            print(e)
            response="error"   
        #except:
            #response="error"
           
    return HttpResponse(response)

def update_sec2(request):#actualiza curso, taller o diplomado
    #emp_id = request.POST.get('userId')
    cursoId = request.POST.get('Id')
    tipo = request.POST.get('tipo_curso')
    nombre = request.POST.get('nombre_curso')
    if ("certificado" not in request.FILES):
        certificado =False
    else:
        certificado = request.FILES['certificado']
    response=""
    #if emp_id is not None:
    try:
        curso= Capacitaciones.objects.get(id=cursoId)
        curso.tipo_curso=tipo
        curso.nombre_curso=nombre
        if (certificado):
            curso.certificado=certificado
        curso.save()
        response="OK2"
    except Exception as e:
        print(e)
        response="error"    
    #except:
    #    response="error"
           
    return HttpResponse(response)

def add_sec2(request):#agregar curso, taller o diplomado
    
    emp_id = request.POST.get('userId')
    #tipo = request.POST.get('tipo_curso')
    #nombre = request.POST.get('nombre_curso')
    
    response=""
   
    if emp_id is not None:
        
        try:
            #form=FileUploadForm(data=request.POST, files=request.FILES)
            
            empleado= Empleado.objects.get(user_id=emp_id)
            Formulario_cursos = CapacitacionForm(request.POST, request.FILES)
            
            
            if Formulario_cursos.is_valid():
                cursos = Formulario_cursos.save(commit=False)
                cursos.user = empleado
                cursos.save()

            response="OK"
        except Exception as e:
            print(e)    
        #except:
        #    response="error"
           
    return HttpResponse(response)

def update_sec3(request):# actualizar idioma
    
    #emp_id = request.POST.get('userId')
    idi_id = request.POST.get('Id')
    idioma_user = request.POST.get('idioma')
    nivel_escrito = request.POST.get('nivel_escrito')
    nivel_hablado = request.POST.get('nivel_hablado')
   
    response=""
   
    #if emp_id is not None:
    try:

        idioma= Idioma.objects.get(id=idi_id)
        idioma.idioma=idioma_user
        idioma.nivel_escrito=nivel_escrito
        idioma.nivel_hablado=nivel_hablado
        idioma.save()
           
            
        response="OK3"
           
    except Exception as e:
        print(e)
        response="error"
        #except:
        #    response="error"
           
    return HttpResponse(response)

def add_sec3(request):#agregar idioma
    emp_id = request.POST.get('userId')
    
    Formulario_idiomas = IdiomasForm(request.POST)
    response=""
   
    if emp_id is not None:
        try:
            empleado= Empleado.objects.get(user_id=emp_id)
            if Formulario_idiomas.is_valid():
                idiomas = Formulario_idiomas.save(commit=False)
                idiomas.user = empleado
                idiomas.save()
           
            empleado.save()
            response="OK"
           
        except:
            response="error"
          
    return HttpResponse(response)

def update_com(request):
    emp_id = request.POST.get('userId')
    #domicilios_post = DomicilioForm(request.POST, request.FILES)
    
    tipo_comprobante = request.POST.get('tipo_comprobante')
    tlf_residencial = request.POST.get('tlf_residencial')
    
    if ("comprobante_domicilio" not in request.FILES):
        comprobante_domicilio =False
    else:
        comprobante_domicilio = request.FILES['comprobante_domicilio']

    #bancos_post = BancoForm(request.POST, request.FILES)
    banco = request.POST.get('banco')
    clabe = request.POST.get('clabe')
    if ("contrato" not in request.FILES):
        contrato =False
    else:
        contrato = request.FILES['contrato']
    
    response=""
   
    if emp_id is not None:
        try:
            dom= Domicilio.objects.get(user=emp_id)
            dom.tipo_comprobante=tipo_comprobante
            dom.tlf_residencial=tlf_residencial
            if(comprobante_domicilio):
                dom.comprobante_domicilio=comprobante_domicilio
            dom.save()
            ban= Banco.objects.get(user=emp_id)
            ban.banco=banco
            ban.clabe=clabe
            if(contrato):
                ban.contrato=contrato
            ban.save()
            response="OK"
        except Exception as e:
            print(e)
            response="error"
        #except:
         #   response="error"
           
    return HttpResponse(response)

def update_rec(request):
    
    response=""
    try:
        id=request.POST.get("Id")
        if ("carta_recomendacion" not in request.FILES):
            carta_recomendacion =False
        else:
            carta_recomendacion = request.FILES['carta_recomendacion']
        carta= Recomendaciones.objects.get(id=id)
        if(carta_recomendacion):
            carta.carta_recomendacion=carta_recomendacion
        carta.save()
        response="OK"
    except Exception as e:
        print(e)   
        response="error"
        #except:
        #   response="error"
           
    return HttpResponse(response)

def update_lic(request):
    emp_id = request.POST.get('userId')
    licId = request.POST.get('licId')
    fecha = request.POST.get('fecha_vigencia')
    permanente = request.POST.get('permanente')
    esdo = request.POST.get('estado_emision')
    lic = request.POST.get('licencia')
        

    response=""
   
    if emp_id is not None:
        try:
            lic= LicenciasConducir.objects.get(id=hijoId)
            lic.fecha_vigencia=fecha
            lic.permanente=permanente
            lic.estado_emision=esdo
            lic.licencia=lic
            lic.save()
            response="OK"
        except Exception as e:
            response="error"
            print(e)    
        #except:
        #    response="error"
           
    return HttpResponse(response)

#@login_required(login_url = '/login/')
def borrar_idi(request):
    try:
        print("va a borrar")
        data = dict()
        id=request.GET.get('id')
        idioma=Idioma.objects.get(id = id)
        idioma.delete()
        data['form_is_valid'] = True
    except Exception as e:
        print(e) 
        data['form_is_valid'] = False
        #except:
        #    pass
    return JsonResponse(data) 

def borrar_capa(request):
    try:
        data = dict()
        id=request.GET.get('id')
        capa=Capacitaciones.objects.get(id = id)
        capa.delete()
        data['form_is_valid'] = True
    except Exception as e:
        print(e) 
        data['form_is_valid'] = False
        #except:
        #    pass
    return JsonResponse(data) 