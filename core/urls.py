# path: función para declarar una ruta URL y a qué vista apunta
from django.urls import path
# views: el módulo con todas las funciones-vista de esta app
from . import views

# urlpatterns: la lista de rutas que Django revisa, en orden, para cada URL
urlpatterns = [
    # '': la página de inicio de la Semana 3 ("Hola desde MySQL"); no la borres
    path('', views.inicio, name='inicio'),
    # /servicios/: la vista de listado que ya existía desde la Semana 3
    path('servicios/', views.servicios, name='servicios'),
    # /servicios/nuevo/: formulario en blanco para crear un registro
    path('servicios/nuevo/', views.crear_servicio, name='crear_servicio'),
    # /servicios/<int:pk>/editar/: <int:pk> captura el id de la URL y lo pasa como argumento a la vista
    path('servicios/<int:pk>/editar/', views.editar_servicio, name='editar_servicio'),
    # /servicios/<int:pk>/eliminar/: mismo patrón, para la pantalla de confirmación de borrado
    path('servicios/<int:pk>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),
# cierra la lista urlpatterns
]