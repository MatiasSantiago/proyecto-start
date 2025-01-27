from django import forms
from .models import Noticia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Noticia, Categoria
from .models import Contacto

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'autor', 'categoria', 'contenido', 'imagen']  # Campos que queremos en el formulario

class NoticiaForm(forms.ModelForm):
    nueva_categoria = forms.CharField(max_length=50, required=False, label='Nueva Categoría')

    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'imagen', 'nueva_categoria']

    def save(self, commit=True):
        # Si se escribió una nueva categoría, crearla
        nueva_categoria = self.cleaned_data.get('nueva_categoria')
        if nueva_categoria:
            categoria, created = Categoria.objects.get_or_create(nombre=nueva_categoria)
            self.instance.categoria = categoria
        return super().save(commit)


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }