from django.shortcuts import render
from django.views import generic
from .models import QuemSomos, Metas, MarcoHistorico
from django.core.mail import EmailMessage

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quemsomos"] = QuemSomos.objects.first()
        context["metas"] = Metas.objects.first()
        context["marcoshistoricos"] = MarcoHistorico.objects.all()
        context["informacoescontato"] = informacoescontato.objects.all()
        return context


def sendEmail(request):

    name = request.POST.get('name')
    cnpj = request.POST.get('cnpj')
    email = request.POST.get('email')
    occupation = request.POST.get('occupation')
    message = request.POST.get('message')

    subject = f'[Site - Contato] {name}'
    body = f' Nome: {name}\n CNPJ: {cnpj}\n Email: {email}\n Área de atuação: {occupation}\n Mensagem: {message}'

    mail = EmailMessage(subject, body, 'ascomicchie@gmail.com', ['ascomicchie@gmail.com'])
    mail.send()

