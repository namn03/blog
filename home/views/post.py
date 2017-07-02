from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

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
    PREVIEW_CHARS = 200

    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'
    paginate_by = POSTS_IN_PAGE
    ordering = '-id'
    category = ""
    search = ""

    def get(self, request, *args, **kwargs):
        if 'category' in kwargs:
            self.category = kwargs['category']
        if 'word' in request.GET:
            print request.GET['word']
            self.search = request.GET['word']
        return super(PostListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        if self.category and self.search:
            return self.model.objects.filter(title__contains=self.search, category__url=self.category)
        elif self.search:
            return self.model.objects.filter(title__contains=self.search)
        elif self.category:
            return self.model.objects.filter(category__url=self.category)
        else:
            return self.model.objects.all()

    def form_valid(self, form):
        self.search = form.cleaned_data['word']

        return super(PostListView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        # paginating
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

        # posts should contain just preview of content
        posts = context['posts']
        for post in posts:
            original = post.content
            if len(original) > self.PREVIEW_CHARS:
                post.content = original[:self.PREVIEW_CHARS]

        return context
