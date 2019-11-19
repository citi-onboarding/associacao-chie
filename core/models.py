from django.db import models
from solo.models import SingletonModel

class QuemSomos (SingletonModel):
        
    description = models.TextField(verbose_name='Sobre nós', null=False, blank=False)
    image = models.ImageField(verbose_name='Imagem', null = False, blank=False, upload_to='aboutUs/')
    
    class Meta:
        verbose_name = 'Quem somos'
        
    def __str__(self):
        return "Quem Somos"
