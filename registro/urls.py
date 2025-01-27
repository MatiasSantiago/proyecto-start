from django.urls import path
from . import views  # Importa las vistas desde el archivo views.py


urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('noticias/', views.lista_noticias, name='lista_noticias'),  # Lista de noticias
    path('noticias/<int:noticia_id>/', views.detalle_noticia, name='detalle_noticia'),  # Detalle de una noticia
    path('agregar/', views.agregar_noticia, name='agregar_noticia'),  # Formulario para agregar noticias
      path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('mis_noticias/', views.mis_noticias, name='mis_noticias'),
    path('moderar/<int:noticia_id>/<str:accion>/', views.moderar_noticia, name='moderar_noticia'),
    path('admin_lista_noticias/', views.admin_lista_noticias, name='admin_lista_noticias'),
    path('eliminar/<int:noticia_id>/', views.eliminar_noticia, name='eliminar_noticia'),
    path('contacto/', views.contacto, name='contacto'),
    






]
