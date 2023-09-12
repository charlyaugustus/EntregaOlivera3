from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def tipo_ser(req, nombre, evento, email):
    nombre = Tipo_Servicio(nombre = nombre, evento = evento, email = email)
    nombre.save()
    
    return HttpResponse(f"""
    
    <p>Tipo de Servicio: {nombre.nombre} - Evento: {nombre.evento}  - Email: {nombre.email} creado con éxito!</p>
    
    """)
    
def listaServicios(req):
    
    servicios = Tipo_Servicio.objects.all()
    return render(req, "ListaServicios.html", {"servicios":servicios})


def inicio(req):
    return render(req, "inicio.html")
    

def tipo(req):
    return render(req, "servicio.html")


def clientes(req):
    return render(req, "clientes.html")

def lugar(req):
    return render(req, "lugar.html")

def fecha_entregar(req):
    return render(req, "fecha_entregar.html")

def servicioFormulario(req):
    
    print('method', req.method)
    print('POST',  req.POST)
    
    if req.method == 'POST':
        
        miFormulario = ServicioFormulario(req.POST)
    
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            nombre = Tipo_Servicio(nombre = data["nombre"], evento = data["evento"], email = data["email"], tipo_servicio = data["tipo_servicio"])
            nombre.save()
            
            return render(req, "inicio.html")
        
    else:
        miFormulario = ServicioFormulario()
        return render(req, "servicioFormulario.html",{"miFormulario": miFormulario})

def busquedaEvento(req):
    return render(req, "busquedaEvento.html")

def buscar(req: HttpRequest):
    
    if req.GET["evento"]:
        evento = req.GET["evento"]
        nombre = Tipo_Servicio.objects.filter(evento__icontains = evento)
        return render(req, "resultadoBusqueda.html", {"nombres": nombre})
    else:
        return HttpResponse(f"Debe agregar un evento")
    
def ListaClientes(req):
        
    clientes = Cliente.objects.all()
    return render(req, "ListaClientes.html", {"clientes": clientes})

def ListaLugares(req):
        
    lugares = Lugar_Evento.objects.all()
    return render(req, "ListaLugares.html", {"lugares": lugares})

def ListaTrabajos(req):
        
    trabajos = Trabajos_entregar.objects.all()
    return render(req, "ListaTrabajos.html", {"trabajos": trabajos})


def BuscarClientes(req):
    
    return render(req, "BusquedaClientes.html")

def BuscarCli(req: HttpRequest):
    
    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        nombre = Cliente.objects.get(nombre=nombre)
        return render(req, "ResultadoBusquedaClientes.html",{"nombre": nombre})
    else:
        return HttpResponse(f"No hay clientes con ese nombre")

    
def clienteFormulario(req):
    print('method', req.method)
    print('POST',  req.POST)
    
    if req.method == 'POST':
        
        clienteFormulario = ClienteFormulario(req.POST)
    
        if clienteFormulario.is_valid():
            
            data = clienteFormulario.cleaned_data
            nombre = Cliente(nombre = data["nombre"], apellido = data["apellido"], email = data["email"])
            nombre.save()
            
            return render(req, "inicio.html")
        
    else:
        clienteFormulario = ClienteFormulario()
        return render(req, "ClienteFormulario.html",{"clienteFormulario": clienteFormulario})


def lugarFormulario(req):
    print('method', req.method)
    print('POST',  req.POST)
    
    if req.method == 'POST':
        
        lugarFormulario = LugarFormulario(req.POST)
    
        if lugarFormulario.is_valid():
            
            data = lugarFormulario.cleaned_data
            nombre = Lugar_Evento(nombre = data["nombre"], localidad = data["localidad"], email = data["email"], salon = data["salon"])
            nombre.save()
            
            return render(req, "inicio.html")
        
    else:
        lugarFormulario = LugarFormulario()
        return render(req, "LugarFormulario.html",{"lugarFormulario": lugarFormulario})

def trabajoFormulario(req):
    print('method', req.method)
    print('POST',  req.POST)
    
    if req.method == 'POST':
        
        trabajoFormulario = TrabajoFormulario(req.POST)
    
        if trabajoFormulario.is_valid():
            
            data = trabajoFormulario.cleaned_data
            nombre = Trabajos_entregar(nombre = data["nombre"], fecha_entrega = data["fecha_entrega"], entregado = data["entregado"], link = data["link"])
            nombre.save()
            
            return render(req, "inicio.html")
        
    else:
        trabajoFormulario = TrabajoFormulario()
        return render(req, "TrabajoFormulario.html",{"trabajoFormulario": trabajoFormulario})

