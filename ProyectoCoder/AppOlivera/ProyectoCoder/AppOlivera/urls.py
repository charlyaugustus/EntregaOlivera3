from django.urls import path
from .views import *


urlpatterns = [
    path("listaServicios/", listaServicios, name="ListaServicios"),
    path("", inicio, name="Inicio"),
    path("lugar/", lugar, name="Lugar_Evento"),
    path("entregables/", fecha_entregar, name="Fecha de Entrega"),
    path("servicio-formulario/", servicioFormulario, name="ServicioFormulario"),
    path("busqueda-evento/", busquedaEvento, name="BusquedaEvento"),
    path("listaclientes/", ListaClientes, name="ListaClientes"),
    path("buscar/", buscar, name="Buscar"),
    path("listalugares/", ListaLugares, name="ListaLugares"),
    path("listatrabajos/", ListaTrabajos, name="ListaTrabajos"),
    path("busqueda-clientes/", BuscarClientes, name="BusquedaClientes"),
    path("busquedando-cli/", BuscarCli, name="BusquedandoClientes"),
    path("cliente-formulario/", clienteFormulario, name="ClienteFormulario"),
    path("lugar-formulario/", lugarFormulario, name="LugarFormulario"),
    path("trabajo-formulario/", trabajoFormulario, name="TrabajoFormulario"),

   
    
    
    
   
    
    
]
