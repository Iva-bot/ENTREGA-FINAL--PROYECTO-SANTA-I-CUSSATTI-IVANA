from AppSanta import views
from django.urls import path
from AppSanta import views_clases
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path ('inicio/', views.inicio,name= 'inicio'),
    path ('productos/', views.productos, name= 'productos'),
    path ('proveedores/', views.proveedores, name= 'proveedores'),
    path ('clientes/', views.clientes, name= 'clientes'),
    path ('envios/', views.envios, name= 'envios'),
    path ('cliente-form/' , views.cliente_form, name= 'ClienteForm'),
    path ('producto-form-2/' , views.producto_form_2, name= 'ProductoForm2'),
    path ('productoFormulario/' , views.productoFormulario, name= 'productoFormulario'),
    path ('busquedaProducto/', views.busquedaProducto, name="BusquedaProducto"),
    path('buscar/', views.buscar),
    path('leerProducto/', views.leerProducto, name= 'leerProducto'),
    path('eliminarProducto/<producto_nombre>', views.eliminarProducto, name= 'EliminaProducto'),
    path('login/' , views_clases.login_request,name="Login"),
    #path('logout/', LogoutView.as_view(template_name='AppSanta/padre.html'), name= 'Logout'),
]

urls_vista_clases= [
    path ('producto/lista/', views_clases.ProductoListView.as_view(),name= 'List'),
    path ('producto/detalle/<int:pk>/', views_clases.ProductoDetailView.as_view(), name= 'Detail'),
    path ('producto/nuevo/', views_clases.ProductoCreateViews.as_view(), name= 'New'),
    path ('producto/editar/<int:pk>', views_clases.ProductoUpdateView.as_view(), name= 'Edit'),
    path ('producto/eliminar/<int:pk>', views_clases.ProductoDeleteView.as_view(), name= 'Delete'),
]
urlpatterns += urls_vista_clases