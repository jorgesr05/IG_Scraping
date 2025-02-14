# Scraping Instagram con Django 🚀

## 📌 Descripción del Proyecto
Este proyecto es una aplicación web desarrollada con **Django** y **Django REST Framework (DRF)** que permite:
- Registrar y autenticar usuarios.
- Agregar influencers y realizar scraping de la descripción de sus perfiles de Instagram.
- Almacenar la información en una base de datos.
- Mostrar una lista de influencers agregados.
- Exponer un **endpoint API** para obtener la descripción de un perfil de Instagram.

## 🛠️ Tecnologías Utilizadas
- **Python 3.x**
- **Django**
- **Django REST Framework (DRF)**
- **requests (para scraping)**
- **Bootstrap (Frontend)**
- **PostgreSQL / SQLite** (Base de Datos)

## 📂 Estructura del Proyecto
```
scrapingIG/
│── backend/       # Lógica del backend (API, scraping, autenticación)
│── frontend/      # Interfaz de usuario con Django Templates
│── scrapingIG/    # Configuración principal de Django
│── manage.py      # Script para ejecutar Django
```

## 🔥 Instalación y Configuración
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/jorgesr05/IG_Scraping.git
cd tu-repo
```

### 2️⃣ Crear y activar un entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar la base de datos
Por defecto, usa **SQLite**, pero puedes cambiarlo en `settings.py`.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Ejecuta las migraciones:
```bash
python manage.py migrate
```

### 5️⃣ Crear un superusuario
```bash
python manage.py createsuperuser
```

### 6️⃣ Iniciar el servidor
```bash
python manage.py runserver
```

Ahora puedes acceder a:
- **Frontend:** `http://127.0.0.1:8000/`
- **API:** `http://127.0.0.1:8000/api/`
- **Admin:** `http://127.0.0.1:8000/admin/`

---

## 📌 Endpoints de la API
### 🔐 Autenticación
| Método | URL | Descripción |
|--------|-----|-------------|
| `POST` | `/api/register/` | Registro de usuarios |
| `POST` | `/api/token/` | Obtiene token JWT |
| `POST` | `/api/token/refresh/` | Refresca el token |

### 👤 Influencers
| Método | URL | Descripción |
|--------|-----|-------------|
| `GET` | `/api/influencers/` | Listar influencers (solo los del usuario autenticado) |
| `POST` | `/api/influencers/` | Agregar un influencer (requiere autenticación) |

### 📡 Scraping
| Método | URL | Descripción |
|--------|-----|-------------|
| `GET` | `/api/scrape/{username}/` | Obtiene la biografía del usuario de Instagram |

**Ejemplo de petición con `curl`**:
```bash
curl -H "Authorization: Bearer <TOKEN>" http://127.0.0.1:8000/api/influencers/
```

---

## ⚡ Configuración de Cookies para Scraping
Para hacer scraping en Instagram, necesitas tu `sessionid`:
1. Inicia sesión en Instagram desde tu navegador.
2. Abre las herramientas de desarrollador (`F12` → `Application` → `Cookies`).
3. Copia el valor de `sessionid`.
4. En Postman o `curl`, envía tu sesión:
```bash
curl -X POST http://127.0.0.1:8000/api/set_instagram_session/ \
     -H "Authorization: Bearer <TOKEN>" \
     -H "Content-Type: application/json" \
     -d '{"sessionid": "tu-session-id"}'
```

---

## 🚀 Despliegue en Producción
1. Configura un entorno virtual y `pip install -r requirements.txt`
2. Aplica migraciones con `python manage.py migrate`
3. Configura `DEBUG = False` en `settings.py`
4. Usa un servidor como **Gunicorn** y un servicio como **AWS, Heroku o DigitalOcean**

---

## 📌 Mejoras Pendientes
✅ Mejorar el manejo de errores en scraping.  
✅ Solucionar problemas de autenticación en frontend.  
✅ Agregar pruebas unitarias.  

---



## 📩 Contacto
Si tienes dudas o sugerencias, puedes escribirme a [12100388@ue.edu.pe](mailto:12100388@ue.edu.pe).

🚀 ¡Gracias por revisar mi proyecto! 🎉
