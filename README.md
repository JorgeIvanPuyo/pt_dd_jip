# Delivery App

Esta es una aplicación para gestionar rutas, conductores y órdenes. El proyecto incluye:
- **Frontend:** Interfaz de usuario (ReactJS).
- **Backend:** API RESTful (Flask).
- **Base de datos relacional:** PostgreSQL.

La documentación detallada del proyecto se encuentra en la [wiki del repositorio](https://github.com/JorgeIvanPuyo/pt_dd_jip/wiki).

---

## Instrucciones para Desplegar la Aplicación en Local

1. **Requisitos previos:**
   Asegúrate de tener instaladas las siguientes herramientas:
   - [Docker](https://www.docker.com/) versión 4.24.2 o superior.
   - [Git](https://git-scm.com/) para clonar el repositorio.

2. **Clonar el repositorio:**
   Ejecuta los siguientes comandos:
   ```bash
   git clone https://github.com/JorgeIvanPuyo/pt_dd_jip.git
   cd pt_dd_jip
   ```

3. **Levantar la aplicación con Docker Compose:**
   Navega a la raíz del proyecto y ejecuta:
   ```bash
   docker compose up --build
   ```

4. **Acceder a los servicios:**
   - **Frontend:** [http://localhost:3000](http://localhost:3000)
   - **Backend (API):** [http://localhost:5000](http://localhost:5000)

5. **Base de datos:**
   - Se incluye una instancia de PostgreSQL que se configura automáticamente al iniciar los contenedores.
   - La base de datos se pobla automáticamente al crear las tablas por primera vez, por lo que al arrancar la aplicación ya habrá datos disponibles.
   - También se proporciona un archivo `db_dump.sql` en caso de que sea necesario importar manualmente la base de datos.

---

## Estructura del Archivo Comprimido

Se incluye en el archivo `prueba_tecnica_JIP.zip` los siguientes elementos:

```plaintext
  |-- backend/
  |-- frontend/
  |-- json-server/
  |-- db_dump.sql
  |-- .git/
  |-- docker-compose.yml
  |-- README.md
```

### Detalles del `docker-compose.yml`:
- Configura y levanta los siguientes servicios:
  - **Frontend:** Aplicación web en [http://localhost:3000](http://localhost:3000).
  - **Backend:** API en [http://localhost:5000](http://localhost:5000).
  - **JSON Server:** Servidor mock para datos externos.
  - **Base de datos PostgreSQL:** Instancia en `localhost:5432`.

---

## Notas Adicionales

1. **Automatización de la base de datos:**
   El backend incluye una automatización que puebla la base de datos automáticamente al crear las tablas por primera vez. No es necesario importar manualmente la base de datos, pero se incluye el archivo `db_dump.sql` en caso de ser requerido.
