from django.shortcuts import render
from django.views import generic
from .models import QuemSomos, Metas, MarcoHistorico

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