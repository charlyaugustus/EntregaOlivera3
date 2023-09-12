from django.db import models

# Create your models here.
class Tipo_Servicio(models.Model):

    nombre = models.CharField(max_length=40)
    evento = models.CharField(max_length=40)
    email  = models.EmailField()
    tipo_servicio = models.EmailField()
    
    def __str__(self) -> str:
        return f'{self.nombre} - {self.evento} - {self.email}  - {self.tipo_servicio}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email= models.EmailField()
    
    def __str__(self) -> str:
        return f'{self.nombre} - {self.apellido} - {self.email}'

class Lugar_Evento(models.Model):
    nombre = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    email = models.EmailField()
    salon = models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return f'{self.nombre} - {self.localidad} - {self.email} - {self.salon}'
    
class Trabajos_entregar(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
    link = models.CharField(max_length=256, null=True)
    trabajo_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return f'{self.nombre} - {self.fecha_entrega} - {self.entregado} - {self.link}'