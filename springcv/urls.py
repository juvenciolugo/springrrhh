"""springcv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from dashboard import views as dashboard_views
from empleados import views as empleados_views
from candidatos import views as candidatos_views
#from becarios import views as becarios_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from dashboard.views import mi_error_404
 
#handler404 = mi_error_404
 
# urls de app dashboard
extra_patterns1 = [
    url(r'^$', dashboard_views.home, name = 'home'),
    
    
    url(r'^login', dashboard_views.login_view, name = 'login'),
    url(r'^logout/$', dashboard_views.login_out, name = 'logout'),
    url(r'^portafolio/$', dashboard_views.portafolio, name = 'portafolio'),
    url(r'^porta-emp/$', dashboard_views.porta_emp, name = 'porta-emp'),
    
    url(r'^register/$', dashboard_views.register, name = 'register'),
    url(r'^sadmin/$', dashboard_views.sadmin, name = 'sadmin'),
    url(r'^cola-home/$', dashboard_views.cola_home, name = 'cola-home'),
    url(r'^rrhh/$', dashboard_views.rrhh, name = 'rrhh'),
    #url(r'^crear/$', dashboard_views.crear, name = 'crear'),
   
   #urls para administracion
    #url(r'^crear2/$', dashboard_views.crear2, name = 'crear2'),
    #url(r'^empAct/$', dashboard_views.empAct, name = 'empAct'),
    url(r'^empLst/$', dashboard_views.empLst, name = 'empLst'),
    #url(r'^empIna/$', dashboard_views.empIna, name = 'empIna'),
    #url(r'^admAct/$', dashboard_views.admAct, name = 'admAct'),
    #url(r'^admBec/$', dashboard_views.admBec, name = 'admBec'),
    #url(r'^editarEmp/(?P<id>[-A-Za-z0-9_]+)$', dashboard_views.editarEmp, name = 'editarEmp'),
    url(r'^update_per', dashboard_views.update_per, name = 'update_per'),
    url(r'^new_per', dashboard_views.new_per, name = 'new_per'),
    url(r'^dashAdm/(?P<id>[-A-Za-z0-9_]+)$', dashboard_views.dashAdm, name = 'dashAdm'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urls de app empleados
extra_patterns2 = [
    #url(r'^captura', empleados_views.captura, name = 'captura'),
    url(r'^perfil', empleados_views.perfil, name = 'perfil'),
    
    url(r'^confirma1', empleados_views.confirma_etapa_1, name = 'confirma1'),
    url(r'^rechaza1', empleados_views.rechaza_etapa_1, name = 'rechaza1'),
    #adm etapa1
    url(r'^admperfil/(?P<id>[-A-Za-z0-9_]+)$', empleados_views.admperfil, name = 'admperfil'),
    url(r'^update_bas', empleados_views.update_bas, name = 'update_bas'),
    url(r'^update_nac', empleados_views.update_nac, name = 'update_nac'),
    #adm etapa2
    url(r'^admetapa-2/(?P<id>[-A-Za-z0-9_]+)$', empleados_views.admetapa_2, name = 'admetapa-2'),
    url(r'^update_doc', empleados_views.update_doc, name = 'update_doc'),
    url(r'^update_vis', empleados_views.update_vis, name = 'update_vis'),
    url(r'^update_lic', empleados_views.update_lic, name = 'update_lic'),
    #adm etapa3
    url(r'^admetapa-3/(?P<id>[-A-Za-z0-9_]+)$', empleados_views.admetapa_3, name = 'admetapa-3'),
    url(r'^update_esdo', empleados_views.update_esdo, name = 'update_esdo'),
    url(r'^update_ext', empleados_views.update_ext, name = 'update_ext'),
    #adm etapa4
    url(r'^admetapa-4/(?P<id>[-A-Za-z0-9_]+)$', empleados_views.admetapa_4, name = 'admetapa-4'),
    url(r'^update_hijo', empleados_views.update_hijo, name = 'update_hijo'),
    url(r'^add_hijo', empleados_views.add_hijo, name = 'add_hijo'),
    
    #adm etapa5
    url(r'^admetapa-5/(?P<id>[-A-Za-z0-9_]+)$', empleados_views.admetapa_5, name = 'admetapa-5'),
    url(r'^update_sec1', empleados_views.update_sec1, name = 'update_sec1'),
    url(r'^update_sec2', empleados_views.update_sec2, name = 'update_sec2'),
    url(r'^add_sec2', empleados_views.add_sec2, name = 'add_sec2'),
    url(r'^update_sec3', empleados_views.update_sec3, name = 'update_sec3'),
    url(r'^add_sec3', empleados_views.add_sec3, name = 'add_sec3'),
    url(r'^borrar_idi/', empleados_views.borrar_idi, name = 'borrar-idi'),
    url(r'^borrar_capa/', empleados_views.borrar_capa, name = 'borrar-capa'),
    #adm etapa6
    url(r'^admetapa-6/(?P<id>[-A-Za-z0-9_]+)$', empleados_views.admetapa_6, name = 'admetapa-6'),
    url(r'^update_com', empleados_views.update_com, name = 'update_com'),
    url(r'^update_rec', empleados_views.update_rec, name = 'update_rec'),
    # ETAPA 2
    url(r'^etapa-2', empleados_views.etapa_2, name = 'etapa-2'),
    
    url(r'^rechaza2', empleados_views.rechaza_etapa_2, name = 'rechaza2'),
    url(r'^confirma2', empleados_views.confirma_etapa_2, name = 'confirma2'),
    # ETAPA 3
    url(r'^etapa-3', empleados_views.etapa_3, name = 'etapa-3'),
    url(r'^rechaza3', empleados_views.rechaza_etapa_3, name = 'rechaza3'),
    url(r'^confirma3', empleados_views.confirma_etapa_3, name = 'confirma3'),
    # ETAPA 4
    url(r'^etapa-4', empleados_views.etapa_4, name = 'etapa-4'),
    url(r'^rechaza4', empleados_views.rechaza_etapa_4, name = 'rechaza4'),
    url(r'^confirma4', empleados_views.confirma_etapa_4, name = 'confirma4'),
    # ETAPA 4
    url(r'^etapa-5', empleados_views.etapa_5, name = 'etapa-5'),
    url(r'^rechaza5_9', empleados_views.rechaza_etapa_5_status_9, name = 'rechaza-status-9'),
    url(r'^confirma5_9', empleados_views.confirma_etapa_5_status_9, name = 'confirma-status-9'),
    url(r'^borrar-curso/(?P<id>[-A-Za-z0-9_]+)$', empleados_views.borrar_curso, name = 'borrar-curso'),
    url(r'^borrar-idioma/(?P<id>[-A-Za-z0-9_]+)$', empleados_views.borrar_idioma, name = 'borrar-idioma'),
    url(r'^confirma5_10', empleados_views.confirma_etapa_5_status_10, name = 'confirma-status-10'),
    url(r'^confirma5_11', empleados_views.confirma_etapa_5_status_11, name = 'confirma-status-11'),
    url(r'^confirma5', empleados_views.confirma_etapa_5, name = 'confirma5'),
    url(r'^rechaza5', empleados_views.rechaza_etapa_5, name = 'rechaza5'),
    # ETAPA 6
    url(r'^etapa-6', empleados_views.etapa_6, name = 'etapa-6'),
    url(r'^rechaza6', empleados_views.rechaza_etapa_6, name = 'rechaza6'),
    url(r'^confirma6', empleados_views.confirma_etapa_6, name = 'confirma6'),
  
    url(r'^admconfirma1/(?P<id>[-A-Za-z0-9_]+)$', empleados_views.admconfirma_etapa_1, name = 'admconfirma1'),
    #url(r'^admconfirma1', empleados_views.admconfirma_etapa_1, name = 'admconfirma1'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#candidatos
extra_patterns3 = [
    url(r'^candidato/', candidatos_views.home_candidato, name = 'home-candidato'),
    url(r'^registro-cv/', candidatos_views.registro_cv, name = 'registro-cv'),
    url(r'^cv-secuno', candidatos_views.cv_secuno, name = 'cv-secuno'),
    url(r'^cv-secdos', candidatos_views.cv_secdos, name = 'cv-secdos'),
    url(r'^cv-sectres', candidatos_views.cv_sectres, name = 'cv-sectres'),
    url(r'^cv-seccuatro', candidatos_views.cv_seccuatro, name = 'cv-seccuatro'),
    url(r'^cv-seccinco', candidatos_views.cv_seccinco, name = 'cv-seccinco'),#agrega experiencia del candidato
    url(r'^cv-secseis', candidatos_views.cv_secseis, name = 'cv-secseis'),  #agrega referencia del candidato

    url(r'^lst-idioma', candidatos_views.lst_idioma, name = 'lst-idioma'),
    url(r'^add-idioma', candidatos_views.add_idioma, name = 'add-idioma'),
    url(r'^edit-idioma', candidatos_views.edit_idioma, name = 'edit-idioma'),
    url(r'^del-idioma', candidatos_views.del_idioma, name = 'del-idioma'),
    
    
    
    url(r'^lst-hijo', candidatos_views.lst_hijo, name = 'lst-hijo'),
    url(r'^add-hijocv', candidatos_views.add_hijocv, name = 'add-hijocv'),
    url(r'^edit-hijocv', candidatos_views.edit_hijo, name = 'edit-hijocv'),
    url(r'^del-hijo', candidatos_views.del_hijo, name = 'del-hijo'),
    
    
    
    url(r'^lst-hermano', candidatos_views.lst_hermano, name = 'lst-hermano'),
    url(r'^add-hermanocv', candidatos_views.add_hermanocv, name = 'add-hermanocv'),
    url(r'^edit-hermanocv', candidatos_views.edit_hermano, name = 'edit-hermanocv'),
    url(r'^del-hermano', candidatos_views.del_hermano, name = 'del-hermano'),
    
    
    
    
    url(r'^lst-estudio', candidatos_views.lst_estudio, name = 'lst-estudio'),
    url(r'^add-estudio', candidatos_views.add_estudio, name = 'add-estudio'),
    url(r'^edit-estudio', candidatos_views.edit_estudio, name = 'edit-estudio'),
    url(r'^del-estudio', candidatos_views.del_estudio, name = 'del-estudio'),
    

    url(r'^lst-otroestudio', candidatos_views.lst_otroestudio, name = 'lst-otroestudio'),
    url(r'^add-otroestudio', candidatos_views.add_otroestudio, name = 'add-otroestudio'),
    url(r'^edit-otroestudio', candidatos_views.edit_otroestudio, name = 'edit-otroestudio'),
    url(r'^del-otroestudio', candidatos_views.del_otroestudio, name = 'del-otroestudio'),
    
    url(r'^lst-experiencia', candidatos_views.lst_experiencia, name = 'lst-experiencia'),
    url(r'^edit-experiencia', candidatos_views.edit_experiencia, name = 'edit-experiencia'),
    url(r'^del-experiencia', candidatos_views.del_experiencia, name = 'del-experiencia'),
    
   
    url(r'^lst-referencia', candidatos_views.lst_referencia, name = 'lst-referencia'),
    url(r'^edit-referencia', candidatos_views.edit_referencia, name = 'edit-referencia'),
    url(r'^del-referencia', candidatos_views.del_referencia, name = 'del-referencia'),
    
    
    #url(r'^lst-docs', candidatos_views.lst_docs, name = 'lst-docs'),
    url(r'^lst-correo', candidatos_views.lst_correo, name = 'lst-correo'),
    url(r'^lst2-correo', candidatos_views.lst2_correo, name = 'lst2-correo'),
    url(r'^enviar-email', dashboard_views.enviar_email, name = 'enviar-email'),
    url(r'^enviar2-email', dashboard_views.enviar2_email, name = 'enviar2-email'),
    url(r'^lst2-docs', candidatos_views.lst2_docs, name = 'lst2-docs'),
    #url(r'^cand-docs', candidatos_views.cand_docs, name = 'cand-docs'),
    url(r'^del-session', candidatos_views.del_session, name = 'del-session')
    #url(r'^lst-idioma/(?P<id>[-A-Za-z0-9_]+)$', candidatos_views.lst_idioma, name = 'lst-idioma'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#RRHH
extra_patterns4 = [
    url(r'^candLst/$', dashboard_views.candLst, name = 'candLst'),
    url(r'^candrrhh/(?P<id>[-A-Za-z0-9_]+)$', dashboard_views.candrrhh, name = 'candrrhh'),
    
    url(r'^filtra-cand', dashboard_views.filtra_cand, name = 'filtra-cand'),
    url(r'^filtra2-cand', dashboard_views.filtra2_cand, name = 'filtra2-cand'),
    url(r'^filtra3-cand', dashboard_views.filtra3_cand, name = 'filtra3-cand'),
    url(r'^all-cand', dashboard_views.all_cand, name = 'all-cand'),
    url(r'^del-candidato', dashboard_views.del_candidato, name = 'del-candidato'),
    url(r'^pasar-emp/(?P<id>[-A-Za-z0-9_]+)$', dashboard_views.pasar_emp, name = 'pasar-emp'),
    url(r'^new_emp', dashboard_views.new_emp, name = 'new-emp'),
    url(r'^baja-emp', dashboard_views.baja_emp, name = 'baja-emp'),
    url(r'^reporte/(?P<id>[-A-Za-z0-9_]+)$', dashboard_views.ReportePersonalizadoExcel.as_view(), name = 'reporte'),
    #url(r'^lstreporte/(?P<id>[-A-Za-z0-9_]+)$', dashboard_views.ReporteLstPersonalizadoExcel.as_view(), name = 'reporte-lst'),
    #url(r'^Pruebalst/', dashboard_views.Pruebalst.as_view(), name = 'Pruebalst'),
    
    url(r'^lstreporte', dashboard_views.ReporteLstPersonalizadoExcel.as_view(), name = 'lst-reporte'),
    url(r'^candidato-pdf/(?P<id>[-A-Za-z0-9_]+)$', dashboard_views.ReportePersonalizadoPDF.as_view(), name = 'candidato_pdf'),
####COLABORADOR
    url(r'^colaborador/(?P<id>[-A-Za-z0-9_]+)$', dashboard_views.colaborador, name = 'colaborador'),
    url(r'^colarrhh/(?P<id>[-A-Za-z0-9_]+)$', dashboard_views.colarrhh, name = 'colarrhh'),
    url(r'^lstcol-idioma', dashboard_views.lstcol_idioma, name = 'lstcol-idioma'),
    url(r'^addcol-idioma', dashboard_views.addcol_idioma, name = 'addcol-idioma'),
    url(r'^editcol-idioma', dashboard_views.editcol_idioma, name = 'editcol-idioma'),
    url(r'^delcol-idioma', dashboard_views.delcol_idioma, name = 'delcol-idioma'),

    url(r'^lstcol-estudio', dashboard_views.lstcol_estudio, name = 'lstcol-estudio'),
    url(r'^addcol-estudio', dashboard_views.addcol_estudio, name = 'addcol-estudio'),
    url(r'^editcol-estudio', dashboard_views.editcol_estudio, name = 'editcol-estudio'),
    url(r'^delcol-estudio', dashboard_views.delcol_estudio, name = 'delcol-estudio'),
    
    url(r'^lstcol-otroestudio', dashboard_views.lstcol_otroestudio, name = 'lstcol-otroestudio'),
    url(r'^addcol-otroestudio', dashboard_views.addcol_otroestudio, name = 'addcol-otroestudio'),
    url(r'^editcol-otroestudio', dashboard_views.editcol_otroestudio, name = 'editcol-otroestudio'),
    url(r'^delcol-otroestudio', dashboard_views.delcol_otroestudio, name = 'delcol-otroestudio'),
    
    url(r'^lstcol-hijo', dashboard_views.lstcol_hijo, name = 'lstcol-hijo'),
    url(r'^addcol-hijo', dashboard_views.addcol_hijo, name = 'addcol-hijo'),
    url(r'^editcol-hijo', dashboard_views.editcol_hijo, name = 'editcol-hijo'),
    url(r'^delcol-hijo', dashboard_views.delcol_hijo, name = 'delcol-hijo'),

    url(r'^lstcol-hermano', dashboard_views.lstcol_hermano, name = 'lstcol-hermano'),
    url(r'^addcol-hermano', dashboard_views.addcol_hermano, name = 'addcol-hermano'),
    url(r'^editcol-hermano', dashboard_views.editcol_hermano, name = 'editcol-hermano'),
    url(r'^delcol-hermano', dashboard_views.delcol_hermano, name = 'delcol-hermano'),

    url(r'^lstcol-experiencia', dashboard_views.lstcol_experiencia, name = 'lstcol-experiencia'),
    url(r'^editcol-experiencia', dashboard_views.editcol_experiencia, name = 'editcol-experiencia'),
    url(r'^delcol-experiencia', dashboard_views.delcol_experiencia, name = 'delcol-experiencia'),

    
    url(r'^lstcol-referencia', dashboard_views.lstcol_referencia, name = 'lstcol-referencia'),
    url(r'^editcol-referencia', dashboard_views.editcol_referencia, name = 'editcol-referencia'),
    url(r'^delcol-referencia', dashboard_views.delcol_referencia, name = 'delcol-referencia'),
    
    url(r'^col-secuno', dashboard_views.col_secuno, name = 'col-secuno'),
    url(r'^col-secdos', dashboard_views.col_secdos, name = 'col-secdos'),
    url(r'^col-sectres', dashboard_views.col_sectres, name = 'col-sectres'),
    url(r'^col-seccuatro', dashboard_views.col_seccuatro, name = 'col-seccuatro'),
    url(r'^col-seccinco', dashboard_views.col_seccinco, name = 'col-seccinco'),#Agrega ñla experiencia
    url(r'^col-secseis', dashboard_views.col_secseis, name = 'col-secseis'),#Agrega la referencia
    url(r'^candDocs/(?P<id>[-A-Za-z0-9_]+)$', dashboard_views.candDocs, name = 'candDocs'),
    url(r'^update-docs', dashboard_views.update_docs, name = 'update-docs'),
    url(r'^update-pro-docs', dashboard_views.update_pro_docs, name = 'update-pro-docs'),
    url(r'^update-otro-docs', dashboard_views.update_otro_docs, name = 'update-otro-docs'),
    url(r'^buscar-cand', dashboard_views.buscar_cand, name = 'buscar-cand'),
    
    
    
    
    #path('categorias/print', categoria_print, name='categoria_print'),  
    #path('categorias/print/<int:pk>', categoria_print, name='categoria_print_one'), 

    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(extra_patterns1)),
    url(r'^', include(extra_patterns2)),
    url(r'^', include(extra_patterns3)),
    url(r'^', include(extra_patterns4)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


