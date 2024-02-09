from django.contrib import admin
from django.urls import path
from appx.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('page/',page, name='page'),
    path('post/',post, name='post'),
    path('post/<slug:slug>',post, name='post')
]
