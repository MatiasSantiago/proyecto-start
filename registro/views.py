from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from .forms import NoticiaForm  
from .models import Noticia, Categoria
from django.shortcuts import get_object_or_404, redirect
from .forms import ContactoForm


def index(request):
    noticias = Noticia.objects.filter(estado='APROBADA')  # Solo noticias aprobadas
    return render(request, 'registro/index.html', {'noticias': noticias})


def lista_noticias(request):
    noticias = Noticia.objects.filter(estado='APROBADA')  # Solo noticias aprobadas
    return render(request, 'registro/lista_noticias.html', {'noticias': noticias})

def detalle_noticia(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    return render(request, 'registro/detalle_noticia.html', {'noticia': noticia})

def crear_admin():
    if not User.objects.filter(username='matias').exists():
        User.objects.create_superuser('matias', 'ma.candiad@duocuc.cl', '12345678')
crear_admin()

@login_required
def agregar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user  # Asocia la noticia al usuario actual
            noticia.estado = 'EN_REVISION'  # Estado inicial
            noticia.save()
            return redirect('mis_noticias')  # Redirige a "Mis Noticias"
    else:
        form = NoticiaForm()
    return render(request, 'registro/agregar_noticia.html', {'form': form})

def crear_categorias():
    categorias = ['Deportes', 'Política', 'Tecnología', 'Cultura', 'Salud']
    for nombre in categorias:
        if not Categoria.objects.filter(nombre=nombre).exists():
            Categoria.objects.create(nombre=nombre)
crear_categorias()

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Logea automáticamente al usuario registrado
            return redirect('index')  # Redirige a la página de inicio
    else:
        form = RegistroForm()
    return render(request, 'registro/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirige a la página de inicio
    else:
        form = AuthenticationForm()
    return render(request, 'registro/iniciar_sesion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('index')  # Redirige a la página de inicio

@login_required
def mis_noticias(request):
    noticias = Noticia.objects.filter(autor=request.user)
    return render(request, 'registro/mis_noticias.html', {'noticias': noticias})

@staff_member_required
def moderar_noticia(request, noticia_id, accion):
    noticia = Noticia.objects.get(id=noticia_id)
    if accion == 'aprobar':
        noticia.estado = 'APROBADA'
    elif accion == 'rechazar':
        noticia.estado = 'RECHAZADA'
    noticia.save()
    return redirect('lista_noticias')

@staff_member_required
def admin_lista_noticias(request):
    noticias = Noticia.objects.all()  # El administrador ve todas las noticias
    return render(request, 'registro/admin_lista_noticias.html', {'noticias': noticias})

@staff_member_required
def eliminar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    noticia.delete()
    return redirect('admin_lista_noticias')


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto')  # Redirige a la misma página después de enviar
    else:
        form = ContactoForm()
    return render(request, 'registro/contacto.html', {'form': form})
