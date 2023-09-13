

#
El proyecto se orienta a una página en la que una empresa pueda gestionar los servicios que ofrece. Organizar su agenda de trabajo recibiendo pedidos de servicios a traves de un formulario de contacto en el que puedan dejar datos los futuros clientes.


Se crearon 4 modelos:
Tipo_Servicio, Cliente, Lugar_Evento, Trabajos_entregar, con sus respectivos formularios. Esos formularios, son accesibles para el usuario(admin) con los siguientes path:
path("cliente-formulario/", clienteFormulario, name="ClienteFormulario"),
path("lugar-formulario/", lugarFormulario, name="LugarFormulario"),
path("trabajo-formulario/", trabajoFormulario, name="TrabajoFormulario") -- Luego se agregaran Botones con el acceso a ellos.
A su vez para el caso de un cliente podrá completar un formulario tocando en el boton de la Pág. Principal <boton : "Formulario Contacto".

Luego en la página se encuentran los botones:
Inicio: pág. inicio
Servicios: Lista Total de Servicios Confirmados/a Confirmar -por ahora disponible para Usuario (nuestro clientes) /clientes
Clientes:  acá los clientes que contrataron el servicio
Lugar del Evento: acá los clientes que contrataron el servicio y lugar del evento
Trabajos: "Trabajos entregados/a entregar"
Formulario Contacto: acá los clientes pueden dejar sus datos
Búsqueda Clientes: dejando un nombre nos devuelve los nombres de los clientes- (sigo buscando solución de cuando no encuentre un clientes no devuela  error)
Hasta acá creo haber cumplido la consigna y me falta muchas mejoras visuales, ordenar código, etc para poder llegar bien a la entrega final.

