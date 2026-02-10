# Chuck Norris API - Documentación

## Descripción General

### ¿Qué hace la API?
Esta aplicación consume la **API oficial de Chuck Norris (chucknorris.io)** para obtener chistes aleatorios y categorizados sobre Chuck Norris. Actúa como una capa intermedia que estructura y sirve estos datos a través de una API RESTful construida con FastAPI.

### Funcionalidades
- Obtener un chiste aleatorio de Chuck Norris.
- Filtrar chistes por categoría (ej: "dev", "movie", "food").
- Listar todas las categorías disponibles.

### Tecnologías utilizadas
- **FastAPI**: Framework web moderno y rápido.
- **Httpx**: Cliente HTTP asíncrono para consumir la API externa.
- **Pydantic**: Validación y serialización de datos.

---

## Endpoints Disponibles

La API expone los siguientes endpoints:

### 1. Obtener Chiste Aleatorio

Obtiene un chiste al azar. Puede filtrarse opcionalmente por una categoría.

- **URL**: `/api/chuck/random`
- **Método HTTP**: `GET`
- **Parámetros de Consulta (Query Params)**:
  - `category` (opcional): Filtra el chiste por una categoría específica.

#### Ejemplo de Uso

**Petición (Sin filtro):**
```http
GET http://localhost:8000/api/chuck/random
```

**Petición (Con filtro):**
```http
GET http://localhost:8000/api/chuck/random?category=dev
```

**Respuesta Exitosa (JSON):**
```json
{
  "id": "m8r5t7g9d2s4",
  "value": "Chuck Norris doesn't debug code, he stares at it until it confesses.",
  "url": "https://api.chucknorris.io/jokes/m8r5t7g9d2s4",
  "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
  "categories": ["dev"],
  "created_at": "2020-01-05 13:42:26.766831",
  "updated_at": "2020-01-05 13:42:26.766831"
}
```

### 2. Listar Categorías

Obtiene la lista de todas las categorías de chistes disponibles.

- **URL**: `/api/chuck/categories`
- **Método HTTP**: `GET`

#### Ejemplo de Uso

**Petición:**
```http
GET http://localhost:8000/api/chuck/categories
```

**Respuesta Exitosa (JSON):**
```json
[
  "animal",
  "career",
  "celebrity",
  "dev",
  "explicit",
  "fashion",
  "food",
  "history",
  "money",
  "movie",
  "music",
  "political",
  "religion",
  "science",
  "sport",
  "travel"
]
```

### 3. Home (Verificación)

Endpoint raíz para verificar que la API está funcionando.

- **URL**: `/`
- **Método HTTP**: `GET`

---

## 🚀 Instalación y Ejecución

### Prerrequisitos
- Python 3.7+
- pip

### 1. Clonar el repositorio y navegar a la carpeta
(Asegúrate de estar en la carpeta raíz del proyecto `taller api`)

### 2. Crear y activar entorno virtual (Recomendado)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
uvicorn main:app --reload
```
La API estará disponible en `http://localhost:8000`.

### 5. Documentación Interactiva

Una vez iniciada la aplicación, puedes acceder a la documentación automática generada por Swagger UI:
- **URL**: `http://localhost:8000/docs`

---

## Estructura del Proyecto

```
taller api/
├── main.py                 # Punto de entrada de la aplicación
├── appsettings.py          # Configuraciones
├── requirements.txt        # Dependencias
├── README.md               # Documentación
├── controllers/            # Controladores de la API
│   └── chuckController.py  # Endpoints de Chuck Norris
├── services/               # Lógica de negocio
│   └── chuckServices.py    # Servicio para obtener chistes
├── clients/                # Clientes HTTP
│   └── chuckClient.py      # Cliente para api.chucknorris.io
└── DTOs/                   # Objetos de Transferencia de Datos
    └── chuckDtos.py        # Modelos Pydantic
```