from django import forms

class ServicioFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    evento = forms.CharField(max_length=40)
    email = forms.CharField(max_length=40)
    tipo_servicio = forms.CharField(max_length=40)
    
    
    