from django.contrib import admin
from .models import *

admin.site.register(Candidato)
admin.site.register(Idioma_candidato)
admin.site.register(Hermano_candidato)
admin.site.register(Hijo_candidato)
admin.site.register(Experiencia)
admin.site.register(Referencia)
admin.site.register(Cand_docs)
admin.site.register(Estudios_otros)
admin.site.register(Estudios_pro)
admin.site.register(TipoDocumentoIdentidad)

