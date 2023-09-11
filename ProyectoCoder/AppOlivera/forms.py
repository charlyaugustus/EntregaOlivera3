from django import forms

class ServicioFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    evento = forms.CharField(max_length=40)
    
    