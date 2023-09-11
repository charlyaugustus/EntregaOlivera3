from django.urls import path
from .views import *


urlpatterns = [
    path("listaServicios/", listaServicios, name="ListaServicios"),
    path("", inicio, name="Inicio"),
    path("lugar/", lugar, name="Lugar_Evento"),
    path("entregables/", fecha_entregar, name="Fecha de Entrega"),
    path("servicio-formulario/", servicioFormulario, name="ServicioFormulario"),
    path("busqueda-servicio/", busquedaEvento, name="BusquedaEvento"),
    path("listaclientes/", ListaClientes, name="ListaClientes"),
    path("buscar/", buscar, name="Buscar"),
    path("listalugares/", ListaLugares, name="ListaLugares")
    
    
   
    
    
]
