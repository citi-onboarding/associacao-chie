from django.db import models
from solo.models import SingletonModel

class QuemSomos (SingletonModel):
        
    description = models.TextField(verbose_name='Sobre nós', null=False, blank=False)
    image = models.ImageField(verbose_name='Imagem', null = False, blank=False, upload_to='aboutUs/')
    
    class Meta:
        verbose_name = 'Quem somos'
        
    def __str__(self):
        return "Quem Somos"

class Metas (SingletonModel):

    title_education = models.CharField(verbose_name="Educação - Meta", blank=True, null = True, max_length=100)
    donation_link_education = models.CharField(verbose_name="Link para vaquinha - Educação", blank=True, null=True, max_length=300)

    title_health = models.CharField(verbose_name="Saúde - Meta", blank=True, null=True, max_length=100)
    donation_link_health = models.CharField(verbose_name="Link para vaquinha - Saúde", blank=True, null=True, max_length=300)

    title_entrepreneur = models.CharField(verbose_name="População Empreendedora - Meta", blank=True, null=True, max_length=100)
    donation_link_entrepreneur = models.CharField(verbose_name="Link para vaquinha - População Empreendedora", blank=True, null=True, max_length=300)

    title_welfare = models.CharField(verbose_name="Bem-estar Social - Meta", blank=True, null=True, max_length=100)
    donation_link_welfare = models.CharField(verbose_name="Link para vaquinha - Bem-estar social", blank=True, null=True, max_length=300)

    class Meta:
        verbose_name = 'Metas'

    def __str__(self):
        return "Metas"

class MarcoHistorico(models.Model):
    date = models.DateTimeField(verbose_name='Data')
    description = models.TextField(verbose_name='Descrição')
    image = models.ImageField(verbose_name='Imagem', upload_to='timeline/')

    class Meta:
        verbose_name = 'Marco Histórico'
        verbose_name_plural = 'Marcos Históricos'

    def __str__(self):
        return self.date

class InformacoesContato(models.Model):
    logo = models.ImageField(verbose_name='Logo', upload_to='info/')
    address = models.CharField(verbose_name='Endereço')
    email = models.EmailField(verbose_name='E-mail')
    linkFace = models.URLField(verbose_name='Facebook')
    linkInsta = models.URLField(verbose_name='Instagram')

    class Meta:
        verbose_name = 'Informação de Contato'
        verbose_name_plural = 'Informações de Contato'

    def __str__(self):
        return "Informações de Contato"