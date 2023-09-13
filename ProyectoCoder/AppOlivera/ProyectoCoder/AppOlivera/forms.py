from django import forms



class ServicioFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    evento = forms.CharField(max_length=40)
    email = forms.CharField(max_length=40)
    tipo_servicio = forms.CharField(max_length=40)
    
class ClienteFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email= forms.EmailField()
    
class LugarFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    localidad = forms.CharField(max_length=40)
    email = forms.EmailField()
    salon = forms.CharField(max_length=40)
    
class TrabajoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField()
    link = forms.CharField(max_length=256)

    

    

    

