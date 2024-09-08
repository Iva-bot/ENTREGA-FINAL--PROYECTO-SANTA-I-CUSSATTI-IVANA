from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from .forms import UserRegisterForm,UsuarioEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView,LogoutView
from users.models import Imagen
from django.urls import reverse_lazy

# Create your views here.
def login_request(request):
     msg_login = ""
     if request.method == 'POST':
          form = AuthenticationForm(request, data=request.POST)
          #print(form)
          if form.is_valid():
               usuario = form.cleaned_data.get('username')
               contraseña = form.cleaned_data.get('password')

               user = authenticate(username= usuario , password= contraseña)
               
               if user is not None:
                    login (request , user)
                    return render (request, "AppSanta/padre.html" , {"mensaje":f"Has iniciado sesión. Bienvenido {usuario}"})
               else:
                    form = AuthenticationForm()
                    return render (request, "user/login.html" , {"mensaje": f"Error, datos incorrectos", "form": form})
               
          msg_login = "Usuario o contraseña incorrectos"
          #else: 
              #return render(request, "AppSanta/index.html", {"mensaje": "Error, formulario inválido"})
     
     form = AuthenticationForm()                                                               
     return render(request, "user/login.html", {"form": form, "msg_login": msg_login})

def register(request):
     msg_register = ""
     if request.method == 'POST':

          form = UserRegisterForm(request.POST)
          if form.is_valid():
             form.save()
             return render(request,"AppSanta/padre.html")
          
          msg_register = "Error en los datos ingresados"
     else:
          form = UserRegisterForm()
     return render(request,"user/register.html" , {"form": form, "msg_register": msg_register})

@login_required
def editar_usuario(request):
     usuario = request.user
     if request.method == 'POST':
          miFormulario = UsuarioEditForm(request.POST, request.FILES, instance=usuario)
          if miFormulario.is_valid():
               if miFormulario.cleaned_data.get('imagen'):
                     if Imagen.objects.filter(user=usuario).exists():
                         usuario.imagen.imagen =miFormulario.cleaned_data.get('imagen')
                         usuario.imagen.save()

                     else:
                         avatar =Imagen(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
                         avatar.save()
               miFormulario.save()

               return render(request, "AppSanta/index.html")

     else:
          miFormulario = UsuarioEditForm(instance=usuario)
     return render(request, "user/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})                        


#class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
      #template_name = "user/editar_pass.html"
      #success_url = reverse_lazy("EditarPerfil")



def logout(request):
    if request.method == 'POST':

        return LogoutView.as_view(next_page='login/')(request)
    else:
        return render(request, 'user/logout.html')




