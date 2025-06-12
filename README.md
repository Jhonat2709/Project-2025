# 📚 SAPIENT - Repositorio Científico Digital de la UNEFA

SAPIENT es un sistema web desarrollado con **Python y Django** para la gestión y consulta de trabajos de investigación (tesis) realizadas por estudiantes de ingeniería de la **Universidad Nacional Experimental Politécnica de la Fuerza Armada Nacional (UNEFA)**. Este repositorio digital tiene como objetivo facilitar el acceso público a los trabajos de grado, permitiendo su carga, búsqueda, visualización y descarga.

---

## 🚀 Características Principales

- Panel principal con las tesis más recientes.
- Motor de búsqueda con filtros por título, autor, carrera y período académico.
- Subida de tesis en formato PDF con extracción automática de resumen.
- Clasificación por categorías y carreras.
- Sistema de autenticación de usuario:
  - **Administrador**: encargado de la carga de tesis y gestión de categorías.
  - **Visitante**: usuario que consulta y descarga los documentos.
- Diseño intuitivo, con identidad visual institucional.

---

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3, Django
- **Frontend:** HTML5, CSS3, Bootstrap (a definir)
- **Base de Datos:** SQLite3 (en desarrollo), migrable a PostgreSQL o MySQL
- **Control de versiones:** Git + GitHub

---

## 📂 Estructura Inicial del Proyecto

```
sapient-unefa/
│
├── manage.py
├── requirements.txt
├── .env
│
├── sapient-unefa/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/
│   │
│   ├── core/
│   │   ├── migrations/
│   │   │
│   │   ├── templates/
│   │   │   └── core/
│   │   │       ├── base.html
│   │   │       ├── dashboard.html
│   │   │       └── layouts/
│   │   │           ├── navbar.html
│   │   │           ├── footer.html
│   │   │           └── ...
│   │   │
│   │   ├── static/
│   │   │   └── core/
│   │   │       ├── css/
│   │   │       ├── js/
│   │   │       └── images/
│   │   │           ├── logo_sapient.png
│   │   │           └── fachada_unefa.jpg
│   │   │
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── forms.py
│   │
│   ├── thesis_management/
│   │   ├── migrations/
│   │   │
│   │   ├── templates/
│   │   │   ├── upload_thesis.html
│   │   │   └── upload_categories.html
│   │   │
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── forms.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   └── thesis/
│       ├── migrations/
│       │
│       ├── templates/
│       │   ├── thesis_detail.html
│       │   └── search_results.html
│       │
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py
│       ├── urls.py
│       └── views.py
│
└── media/
    └── thesis/
        └── example_thesis.pdf
```

---

## 📌 Estado del Proyecto

🟠 *En desarrollo*  
✔️ Estructura inicial y modelos definidos  
🔜 Próxima tarea: todo :b

---