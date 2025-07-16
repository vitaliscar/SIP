# Sales Intelligence Platform (SIP)

Plataforma de inteligencia de ventas para gestión comercial, análisis y automatización de procesos en empresas.

## ¿Qué se espera del sistema?
SIP está diseñado para transformar la gestión comercial y la toma de decisiones en empresas que buscan optimizar sus procesos de ventas y atención al cliente. El sistema debe permitir:

- **Centralizar la información comercial**: Unificar datos de clientes, sucursales, productos, ventas y usuarios en una sola plataforma accesible y segura.
- **Automatizar procesos clave**: Facilitar la importación masiva de datos, la gestión de usuarios y sucursales, y la administración de productos y ventas.
- **Mejorar la inteligencia de negocio**: Integrar modelos de IA y reportes para analizar tendencias, predecir oportunidades y detectar riesgos comerciales.
- **Optimizar la gestión de sucursales**: Permitir la administración eficiente de sucursales, asignación de clientes y seguimiento de desempeño por zona geográfica.
- **Facilitar el trabajo colaborativo**: Proveer herramientas para que asesores, gerentes y administradores trabajen sobre la misma base de datos, con permisos y roles diferenciados.
- **Escalabilidad y seguridad**: Soportar el crecimiento de la empresa y proteger la información sensible mediante buenas prácticas y despliegue en entornos seguros.

El objetivo final es que SIP sea el núcleo digital de la operación comercial, permitiendo a la empresa tomar decisiones informadas, automatizar tareas repetitivas y potenciar el crecimiento a través de la tecnología.

## Características principales
- Gestión de clientes, sucursales, productos, ventas y usuarios
- Panel de administración personalizado
- Importación masiva de datos
- Integración con modelos de IA y reportes
- Soporte para PostgreSQL
- Arquitectura modular con Django

## Estructura del proyecto
- `apps/`: Aplicaciones principales (clients, users, products, sales, goals, reporting, ai_models, core)
    - **clients/templates/clients/**: client_detail.html, client_form.html, client_list.html, sucursal_detail.html, sucursal_form.html, sucursal_list.html
    - **products/templates/products/**: product_detail.html, product_form.html, product_list.html
    - **sales/templates/sales/**: quote_detail.html, quote_form.html, quote_list.html
    - **goals/templates/goals/**: goal_form.html, goal_fulfillment.html, goal_list.html
    - **reporting/templates/reporting/**: dashboard.html
    - **users/templates/users/**: login.html, password_reset.html, password_reset_confirm.html, password_reset_done.html, profile.html, register.html, user_detail.html, user_list.html
    - **ai_models/templates/ai_models/**: forecast_results.html
- `config/`: Configuración de Django y settings por entorno
- `static/` y `media/`: Archivos estáticos y multimedia
- `templates/`: Plantillas base y por módulo (base.html, includes/)
- `requirements.txt`: Dependencias del proyecto
- `Dockerfile` y `docker-compose.yml`: Contenedores y despliegue

## Instalación rápida
1. Clona el repositorio:
   ```bash
   git clone https://github.com/vitaliscar/SIP.git
   cd SIP
   ```
2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configura la base de datos en `config/settings/base.py`
4. Ejecuta migraciones:
   ```bash
   python manage.py migrate
   ```
5. Crea un superusuario:
   ```bash
   python manage.py createsuperuser
   ```
6. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

## Despliegue en producción
- Edita `config/settings/production.py` para tu dominio y seguridad
- Usa Docker para despliegue automatizado

## Autor
- vitaliscar

## Licencia
MIT

## Ejemplo de uso básico

Crear un cliente:
```bash
python manage.py shell
>>> from apps.clients.models import Client
>>> Client.objects.create(name="Empresa Ejemplo", email="contacto@ejemplo.com")
```

Importar ventas desde CSV:
```bash
python manage.py import_sales path/to/archivo.csv
```

## Roles y permisos

| Rol          | Permisos principales                         |
|--------------|---------------------------------------------|
| Administrador| Gestión total del sistema                   |
| Gerente      | Reportes, administración de sucursales      |
| Asesor       | Gestión de clientes y ventas                |

## Contribuir

1. Haz un fork del repositorio.
2. Crea una rama para tu mejora/bug.
3. Envía un Pull Request describiendo el cambio.
4. Responde preguntas y comentarios de la revisión.

## Preguntas frecuentes

- **¿Cómo cambio la configuración de base de datos?**
  Modifica `config/settings/base.py` o usa variables de entorno.

- **¿Cómo reporto un bug?**
  Abre un issue en GitHub con el mayor detalle posible.
