from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Producto
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#ver clase repaso
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate

#ver clase repaso
def login_request(request):
     #msg_login = ""
     if request.method == "POST":
          form = AuthenticationForm(request, data = request.POST)
          print(form)
          if form.is_valid():
               usuario = form.cleaned_data.get("username")
               contraseña = form.cleaned_data.get("password")

               user = authenticate(username=usuario , password=contraseña)
               
               if user is not None:
                    login (request , user)
                    return render (request, "AppSanta/index.html" , {"mensaje":f"Has iniciado sesión. Bienvenido {usuario}"})
               else:
                    form = AuthenticationForm()
                    return render (request, "AppSanta/login.html" , {"mensaje": f"Error, datos incorrectos", "form": form})
               
          #msg_login = "Usuario o contraseña incorrectos"
          else: 
               return render(request, "AppSanta/index.html", {"mensaje": "Error, formulario inválido"})
     
     form = AuthenticationForm()                                                               
     return render(request, "AppSanta/login.html", {"form": form})

#ver en que clase lo hicimos
def inicio (request):
     return render(request, "AppSanta/index.html")

@login_required
def about(request):
     return render(request, "AppSanta/about.html")



class ProductoListView (LoginRequiredMixin, ListView):
     model = Producto
     context_object_name = "producto"
     template_name ="/AppSanta/Vista_Clases/producto_list.html"
     
     def get(self,request,*args,**kwargs):
         return super().get(request,*args,**kwargs)




class ProductoDetailView(LoginRequiredMixin, DetailView):
     model= Producto
     template_name="/AppSanta/Vista_Clases/producto_detalle.html"
    
class ProductoCreateViews (LoginRequiredMixin, CreateView):
     model = Producto
     template_name = "/AppSanta/Vista_Clases/producto_form.html"
     success_url =reverse_lazy ("List")
     fields = ["nombre","cantidad"]

class ProductoUpdateView (LoginRequiredMixin, UpdateView):
     model= Producto
     template_name= "/AppSanta/Vista_Clases/producto_edit.html"
     #success_url =reverse_lazy ("List")
     success_url ="/AppSanta/clases/lista/"
     fields = ["nombre","cantidad"]

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
     model = Producto
     template_name = "/AppSanta/Vista_Clases/producto_confirm_delete.html"
     #success_url =reverse_lazy ("List")
     success_url ="/AppSanta/clases/lista/"
     fields = ["nombre","cantidad"]
