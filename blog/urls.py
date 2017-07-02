"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

# for media url 
from settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

from home.views import *

urlpatterns = [
    url(r'^$', MainView.as_view(), name='home'),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^post/(?P<pk>(\d+))/edit', EditPostView.as_view(), name='edit_post'),
    url(r'^post/(?P<pk>(\d+))', PostView.as_view(), name='post'),
    url(r'^post/new', NewPostView.as_view(), name='new_post'),
    url(r'^post/(?P<category>(\w+))', PostListView.as_view(), name='category'),
    url(r'^post', PostListView.as_view(), name='all_post'),
    url(r'^login/', login, kwargs={'template_name': 'login.html'}, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^admin/', admin.site.urls, name='admin'),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)


from django.conf.urls import handler404

handler404 = Page404.as_view()
