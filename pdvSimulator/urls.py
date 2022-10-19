from django.contrib import admin
from django.urls import path, include
from pdvSimulations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pdvSimulations.urls')),
]
