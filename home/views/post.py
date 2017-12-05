from django.http import Http404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

from home.models import Category
from ..forms import *


class NewPostView(PermissionRequiredMixin, CreateView):

    form_class = PostForm
    model = Post
    template_name = 'edit_post.html'
    success_url = '.'

    permission_required = 'home.add_post'


class PostView(DetailView):

    template_name = 'post.html'
    model = Post


class EditPostView(PermissionRequiredMixin, UpdateView):

    form_class = PostForm
    model = Post
    template_name = 'edit_post.html'
    success_url = '.'

    permission_required = 'home.add_post'

    def get_object(self, queryset=None):
        return Post.objects.get(pk=self.kwargs['pk'])


class PostListView(ListView):

    POSTS_IN_PAGE = 10
    PAGES_IN_LINE = 5

    template_name = 'list.html'
    context_object_name = 'posts'
    paginate_by = POSTS_IN_PAGE
    ordering = '-date'

    category = None

    def get(self, request, *args, **kwargs):
        self.queryset = Post.objects.all()

        if 'category' in kwargs:
            category = Category.objects.filter(url=kwargs['category'])

            if category:
                self.category = category[0]
                self.queryset = self.queryset.filter(category__url=kwargs['category'])
            else:
                raise Http404

        if 'word' in request.GET:
            self.queryset = self.queryset.filter(title__contains=request.GET['word'])

        return super(PostListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        context['category'] = self.category

        # custom paginating
        page = context['page_obj']
        paginator = context['paginator']

        start_page = page.number - (page.number % 5 - 1)
        if start_page + self.PAGES_IN_LINE < paginator.num_pages:
            current_range = range(start_page, start_page + self.PAGES_IN_LINE)
            next_page = start_page + self.PAGES_IN_LINE
        else:
            current_range = range(start_page, paginator.num_pages + 1)
            next_page = page.number

        if start_page == 1:
            prev_page = page.number
        else:
            prev_page = start_page - 1

        context['prev'] = prev_page
        context['next'] = next_page
        context['range'] = current_range

        return context
