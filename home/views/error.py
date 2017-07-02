from django.views.generic.base import TemplateView


class Page404(TemplateView):
    template_name = 'error/404.html'
