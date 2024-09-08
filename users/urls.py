from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView
from . import views



urlpatterns = [
    path ('login/', views.login_request, name="Login"),
    path('register/' , views.register, name="Register"),
    path('logout/', views.logout, name="logout"),
    path('edit/', views.editar_usuario, name="EditarPerfil")
]




