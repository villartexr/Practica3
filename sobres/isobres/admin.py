from django.contrib import admin
from isobres.models import Professor, Alumne, Aula, Titulacio, Curs

admin.site.register(Titulacio)
admin.site.register(Alumne)
admin.site.register(Aula)
admin.site.register(Professor)
admin.site.register(Curs)