from django.contrib import admin
from .models import QuemSomos, Metas
from solo.admin import SingletonModelAdmin

# Register your models here.

admin.site.register(QuemSomos, SingletonModelAdmin)
admin.site.register(Metas, SingletonModelAdmin)
