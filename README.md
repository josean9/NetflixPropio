# NetflixPropio

## Descripción
**NetflixPropio** es una plataforma de streaming inspirada en Netflix que incluye funcionalidades para gestionar películas, series, y playlists personalizadas, además de un mini juego de Snake. Desarrollado con **Django**, utiliza **SQLite** (inicialmente) como base de datos y cuenta con un diseño moderno y responsivo.

---

## Funcionalidades Principales

### 1. **Autenticación y Perfiles de Usuario**
- Registro, inicio y cierre de sesión.
- Edición de perfil con avatar personalizado, biografía y fecha de nacimiento.
- Integración del avatar en la barra de navegación.

### 2. **Gestión de Contenido**
- Películas y series clasificadas por tendencias, novedades y calificaciones.
- Búsqueda por nombre de películas y series.
- Creación de una playlist personalizada para usuarios.

### 3. **Mini Juego de Snake**
- Tablero dinámico con cuadrícula visible.
- Comida circular y colores personalizables.
- Puntuaciones en tiempo real (actual y récord).
- Estilo visual moderno y controles optimizados.

---

## Estructura del Proyecto

### **Carpetas Principales**
- **`authentication`**: Manejo de autenticación y perfiles.
- **`streaming`**: Gestión de películas, series y playlists.
- **`snake`**: Implementación del mini juego de Snake.
- **`netflixuax`**: Configuración global del proyecto.

### **Bases de Datos**
- Inicialmente **SQLite**, con transición planeada a **PostgreSQL** para despliegue.

---

## Despliegue
- Se intentó desplegar en **Vercel**, pero se encontraron problemas de configuración con PostgreSQL.
- Posibilidad de migrar a **Heroku** o solucionar los problemas actuales para completar el despliegue.

---

## Ideas Futuras
1. **Recomendaciones Personalizadas** basadas en el contenido de la playlist.
2. **Integración de APIs Externas** para sincronizar películas y series populares.
3. **Modo Multijugador para Snake** con puntuaciones globales.
4. Mejora en el diseño general y funcionalidad de la plataforma.

---

## Configuración
### Instalación de Dependencias
```bash
pip install -r requirements.txt


Películas populares: http://localhost:8000/api/popular/
Detalles de una película (ejemplo con movie_id=550): http://localhost:8000/api/movie/550/
