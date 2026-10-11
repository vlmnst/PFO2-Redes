# PFO 2: Sistema de Gestión de Tareas con API y Base de Datos

Este proyecto es una aplicación cliente-servidor desarrollada en Python que implementa una API REST utilizando **Flask**, persistencia de datos local con **SQLite**, autenticación segura con contraseñas hasheadas y un cliente interactivo por consola.

---

## 📂 Estructura del Proyecto

El proyecto está diseñado bajo una arquitectura modular y limpia:

```text
PFO2/
│
├── helpers/
│   └── validations.py       # Funciones auxiliares de validación de entradas
│
├── routes/
│   ├── auth_routes.py       # Endpoints de autenticación (/registro, /login)
│   └── tasks_routes.py      # Endpoints de gestión de tareas (/tareas)
│
├── templates/
│   └── tareas.html          # Plantilla HTML de bienvenida
│
├── cliente.py               # Cliente en consola interactivo
├── servidor.py              # Archivo principal de la API Flask
├── database.db              # Base de datos SQLite (se genera automáticamente)
└── README.md                # Documentación del proyecto
```

---

## 🛠️ Requisitos e Instalación

Asegúrate de tener instalado **Python** (versión 3.9 o superior) en tu computadora.

### 1. Clonar o descargar el repositorio

Descarga o ubícate en la carpeta raíz del proyecto en tu terminal.

### 2. Instalar las dependencias necesarias

El servidor utiliza **Flask** para la API y el manejo de bases de datos, mientras que el cliente de consola utiliza **`requests`** para comunicarse con el servidor.

Ejecuta el siguiente comando en tu terminal para instalar ambas dependencias:

```bash
python3 -m pip install flask requests
```

## Cómo Ejecutar el Proyecto

Para ejecutar y probar el sistema, necesitarás abrir **dos terminales independientes**: una para el servidor (API) y otra para el cliente en consola.

### 1. Iniciar el Servidor API

Abre una terminal en la carpeta raíz del proyecto y ejecuta el servidor Flask:

```bash
python3 servidor.py
```

Esto iniciará la API en http://localhost:5000 y creará automáticamente el archivo de base de datos local database.db.

### 2. Ejecutar el Cliente en Consola

Abre otra pestaña o ventana de la terminal (manteniendo la del servidor encendida) y ejecuta el cliente interactivo:

```bash
python3 cliente.py
```

Desde el menú interactivo que aparecerá en la consola podrás:

Registrar un nuevo usuario.

Iniciar sesión con tus credenciales.

Acceder a la ruta protegida de tareas (GET /tareas), que descargará y mostrará el código HTML de bienvenida proporcionado por el servidor.
