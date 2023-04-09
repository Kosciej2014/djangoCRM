import CRM
from django.contrib import admin
from django.urls import path, include
from CRM import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(CRM.urls)),

]
