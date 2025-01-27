from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias/')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    ESTADO_CHOICES = [
        ('EN_REVISION', 'En Revisión'),
        ('APROBADA', 'Aprobada'),
        ('RECHAZADA', 'Rechazada'),
    ]

    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que creó la noticia
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias/')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='EN_REVISION')  # Estado de la noticia

    def __str__(self):
        return self.titulo
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
