# path: función para declarar una ruta URL y a qué vista apunta
from django.urls import path
# views: el módulo con todas las funciones-vista de esta app
from . import views

# urlpatterns: la lista de rutas que Django revisa, en orden, para cada URL
urlpatterns = [
    # '': la página de inicio de la Semana 3; no la borres
    path('', views.inicio, name='inicio'),
    # /servicios/: listado (Semana 3), ahora filtrado por usuario
    path('servicios/', views.servicios, name='servicios'),
    # /servicios/nuevo/: crear (Semana 5)
    path('servicios/nuevo/', views.crear_servicio, name='crear_servicio'),
    # /servicios/<id>/editar/: editar (Semana 5)
    path('servicios/<int:pk>/editar/', views.editar_servicio, name='editar_servicio'),
    # /servicios/<id>/eliminar/: eliminar con confirmación (Semana 5)
    path('servicios/<int:pk>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),
    # /registro/: NUEVA, pantalla de alta de cuenta
    path('registro/', views.registro, name='registro'),
    # /login/: NUEVA, pantalla de inicio de sesión propia (reemplaza al login prestado de /admin)
    path('login/', views.iniciar_sesion, name='login'),
    # /logout/: NUEVA, cierra la sesión activa
    path('logout/', views.cerrar_sesion, name='logout'),
# cierra la lista urlpatterns
]