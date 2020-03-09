from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('home/', views.home, name='home'),
]
