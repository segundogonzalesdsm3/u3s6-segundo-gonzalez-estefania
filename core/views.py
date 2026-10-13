# render: junta una plantilla con datos · redirect: manda al navegador a otra URL · get_object_or_404: busca un registro o responde 404
from django.shortcuts import render, redirect, get_object_or_404
# connection: datos de la conexión a la base (lo usa la vista "inicio" de la Semana 3)
from django.db import connection
# login_required: decorador que exige sesión iniciada antes de entrar a la vista
from django.contrib.auth.decorators import login_required
# Servicio: el modelo de la Semana 4, importado desde este mismo directorio
from .models import Servicio
# ServicioForm: el ModelForm que creaste en el paso 01
from .forms import ServicioForm


# inicio: la vista de la Semana 3 que muestra a qué base estás conectado (no cambia)
def inicio(request):
    # settings_dict: diccionario con ENGINE, HOST, NAME, etc. de la conexión activa
    info_bd = connection.settings_dict
    # contexto: los datos que la plantilla podrá usar
    contexto = {
        # motor: el tipo de base de datos (debe decir mysql)
        'motor': info_bd['ENGINE'],
        # host: el servidor de la base (en Aiven termina en aivencloud.com)
        'host': info_bd['HOST'],
    # cierre del diccionario contexto
    }
    # render: junta inicio.html con el contexto y devuelve la página
    return render(request, 'core/inicio.html', contexto)


# servicios: la vista del listado de la Semana 4 (no cambia)
def servicios(request):
    # .objects.all(): pide TODOS los servicios a MySQL
    lista_servicios = Servicio.objects.all()
    # entrega la lista a la plantilla con el nombre "servicios"
    return render(request, 'core/servicios.html', {'servicios': lista_servicios})


# @login_required: si nadie inició sesión, Django lo manda a LOGIN_URL (el login de /admin)
@login_required
# crear_servicio: la vista que atiende /servicios/nuevo/
def crear_servicio(request):
    # request.method: distingue si el navegador pide el formulario (GET) o lo está enviando (POST)
    if request.method == 'POST':
        # ServicioForm(request.POST): reconstruye el formulario con los datos que el usuario tecleó
        form = ServicioForm(request.POST)
        # is_valid(): corre todas las validaciones del modelo (tipos, max_length, campos obligatorios)
        if form.is_valid():
            # commit=False: crea el objeto Servicio en memoria SIN guardarlo todavía en MySQL
            nuevo = form.save(commit=False)
            # propietario: se asigna aquí, no en el formulario, para que nadie pueda falsificarlo
            nuevo.propietario = request.user
            # save(): ahora sí guarda el registro completo en MySQL
            nuevo.save()
            # redirect('servicios'): evita reenvíos duplicados si el usuario recarga la página
            return redirect('servicios')
    # si no es POST, es GET: el usuario apenas abrió la página
    else:
        # ServicioForm() sin datos: formulario vacío
        form = ServicioForm()
    # render: dibuja la plantilla, pasándole el formulario (vacío o con errores)
    return render(request, 'core/servicio_form.html', {'form': form, 'titulo_pagina': 'Nuevo servicio'})

# @login_required: solo usuarios con sesión iniciada pueden editar
@login_required
# pk: la clave primaria (id) que Django extrae del pedazo <int:pk> de la URL (paso 05)
def editar_servicio(request, pk):
    # busca el Servicio con ese id; si no existe, responde 404 automáticamente
    servicio = get_object_or_404(Servicio, pk=pk)
    # si el usuario envió el formulario con cambios, la petición llega como POST
    if request.method == 'POST':
        # instance=servicio: le dice al formulario "actualiza ESTE registro, no crees uno nuevo"
        form = ServicioForm(request.POST, instance=servicio)
        # is_valid(): revisa tipos de dato y campos obligatorios
        if form.is_valid():
            # save(): al tener instance=, guarda los cambios sobre el mismo registro (UPDATE, no INSERT)
            form.save()
            # redirect: regresa al listado después de guardar
            return redirect('servicios')
    # si no es POST, es GET: se acaba de abrir la pantalla de edición
    else:
        # instance=servicio sin datos de POST: precarga el formulario con los valores actuales
        form = ServicioForm(instance=servicio)
    # render: reutiliza servicio_form.html con el título "Editar servicio"
    return render(request, 'core/servicio_form.html', {'form': form, 'titulo_pagina': 'Editar servicio'})

# @login_required: solo usuarios con sesión iniciada pueden borrar
@login_required
# eliminar_servicio: recibe el pk (id) desde la URL /servicios/<pk>/eliminar/
def eliminar_servicio(request, pk):
    # busca el registro exacto a borrar, igual que en editar_servicio
    servicio = get_object_or_404(Servicio, pk=pk)
    # solo se borra si llega un POST (el botón de confirmar), nunca con un simple GET
    if request.method == 'POST':
        # delete(): borra la fila de MySQL de verdad
        servicio.delete()
        # redirect: regresa al listado, ya sin el registro borrado
        return redirect('servicios')
    # si es GET, solo muestra la pantalla de "¿Seguro?"; todavía no borra nada
    return render(request, 'core/servicio_confirm_delete.html', {'servicio': servicio})