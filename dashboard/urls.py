from django.contrib import admin
from django.urls import path, re_path, include

from . import views
from django.conf.urls import url
from pdt import urls
from .views import importar

urlpatterns = [
    #path('admin/', admin.site.urls),
    path(r'',views.dashboard_home, name='dashboard_home'),
    path(r'estudiante',views.dashboard_estudiante, name='estudiante'),
]
