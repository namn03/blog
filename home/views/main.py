from django.views.generic.base import TemplateView


class MainView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        pass
