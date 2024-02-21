
from django.contrib import admin
from django.urls import path
from app.views import home ,detail_page,hero

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('hero/',hero,name='hero'),
    path('detail_page/<slug:slug>/',detail_page , name='detail_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
