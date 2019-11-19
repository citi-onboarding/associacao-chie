from django.contrib import admin
from .models import QuemSomos
from solo.admin import SingletonModelAdmin

# Register your models here.

admin.site.register(QuemSomos, SingletonModelAdmin)
