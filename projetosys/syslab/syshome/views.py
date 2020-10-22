from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'home/home.html'


class PricingView(TemplateView):
    template_name = 'home/pricing.html'
