from django.contrib import admin
from .models import QuemSomos, Metas, MarcoHistorico, InformacoesContato
from solo.admin import SingletonModelAdmin

# Register your models here.

admin.site.register(QuemSomos, SingletonModelAdmin)
admin.site.register(Metas, SingletonModelAdmin)
admin.site.register(MarcoHistorico)
admin.site.register(InformacoesContato, SingletonModelAdmin)