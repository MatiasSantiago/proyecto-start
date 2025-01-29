# Caos News

**Caos News** es una plataforma de noticias donde los usuarios pueden registrarse, iniciar sesión y publicar noticias. Estas noticias deben ser aprobadas por un administrador antes de ser visibles en la página principal.

##  Características
- Registro e inicio de sesión de usuarios.
- Publicación de noticias por parte de los usuarios.
- Revisión de noticias por el administrador (aprobar/rechazar).
- Página de noticias aprobadas visibles para todos.
- Página de "Mis Noticias" donde los usuarios pueden ver el estado de sus noticias.
- Panel de administración para gestionar publicaciones.
- Página de contacto para enviar sugerencias o consultas.
- **Carrusel de imágenes** en la página principal.
- proyecto echo de manera responsiva(que se adapte a la mayoria de dispositivos)

---

## Instalación y Configuración

### 1️⃣ **Clonar el repositorio**
```bash
git clone https://github.com/TU-USUARIO/caos-news.git
cd caos-news

###2️⃣ **crear un entorno virtual y activarlo**
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

###3️⃣ **Instalar dependencias**
pip install -r requirements.txt

###4️⃣ **ejecutar el servidor**
python manage.py runserver
