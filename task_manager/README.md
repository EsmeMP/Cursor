# Gestor de Tareas Flask

Una aplicación web simple para gestionar tareas personales, construida con Flask.

## Características

- ✅ Crear, editar y eliminar tareas
- ✅ Marcar tareas como completadas
- ✅ Prioridades (Alta, Media, Baja)
- ✅ Interfaz responsive con Bootstrap
- ✅ Persistencia de datos en JSON
- ✅ API endpoints para integración
- ✅ Manejo de errores 404 y 500

## Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd /home/meme/Documentos/Algoritmos/cursor/task_manager
   ```

2. **Activar el entorno virtual**
   ```bash
   source ../venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

2. **Abrir en el navegador**
   ```
   http://localhost:5000
   ```

## Estructura del Proyecto

```
task_manager/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias Python
├── README.md             # Este archivo
├── tasks.json            # Archivo de datos (se crea automáticamente)
├── templates/            # Plantillas HTML
│   ├── base.html         # Plantilla base
│   ├── index.html        # Página principal
│   ├── edit_task.html    # Formulario de edición
│   ├── 404.html          # Página de error 404
│   └── 500.html          # Página de error 500
└── static/               # Archivos estáticos
    ├── css/
    │   └── style.css     # Estilos personalizados
    └── js/
        └── main.js       # JavaScript personalizado
```

## API Endpoints

- `GET /` - Página principal
- `POST /add_task` - Agregar nueva tarea
- `GET /complete_task/<id>` - Marcar tarea como completada
- `GET /delete_task/<id>` - Eliminar tarea
- `GET /edit_task/<id>` - Formulario de edición
- `POST /edit_task/<id>` - Actualizar tarea
- `GET /api/tasks` - Obtener todas las tareas (JSON)
- `GET /api/task/<id>` - Obtener tarea específica (JSON)

## Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework CSS**: Bootstrap 5
- **Iconos**: Font Awesome
- **Persistencia**: JSON

## Desarrollo

Para desarrollo, la aplicación se ejecuta en modo debug:
- Recarga automática al cambiar archivos
- Mensajes de error detallados
- Puerto: 5000

## Producción

Para producción, considera:
- Cambiar `app.secret_key` por una clave segura
- Usar una base de datos real (SQLite, PostgreSQL, etc.)
- Configurar un servidor WSGI (Gunicorn, uWSGI)
- Usar un servidor web (Nginx, Apache)

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
