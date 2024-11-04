# Mediator Pattern Hotel Booking API

Este repositorio fue creado para demostrar el funcionamiento del **patrón de comportamiento Mediator** utilizando una API de reservas de hoteles desarrollada en **Python**.

## Descripción

El patrón Mediator promueve la comunicación entre objetos sin que estos tengan que referirse directamente entre sí, lo que reduce el acoplamiento y mejora la mantenibilidad del código. En este proyecto, se implementa este patrón para gestionar la interacción entre diferentes componentes de una API de reservas de hoteles.

## Estructura del Proyecto

A continuación se detalla la estructura del proyecto y se proporcionan enlaces a carpetas específicas:

- **[app](https://github.com/SsaylemMurillo/mediator_pattern/tree/main/hotel_booking_api/app)**: Inicialización de servicios y rutas de la API.
- **[mediator](https://github.com/SsaylemMurillo/mediator_pattern/tree/main/hotel_booking_api/mediator)**: Contiene toda la lógica del patrón Mediator a implementar.
- **[services](https://github.com/SsaylemMurillo/mediator_pattern/tree/main/hotel_booking_api/services)**: Contiene los diferentes servicios, incluyendo inventario, pagos, notificaciones y reservas.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/SsaylemMurillo/mediator_pattern.git

## Ejecución del Programa

El programa se ejecuta utilizando el archivo `run.py`. A continuación, se presentan algunas rutas que puedes utilizar para probar la API:

### Rutas para Probar

#### Crear una Reserva

- **Método**: POST  
- **URL**: [http://localhost:5000/create_booking](http://localhost:5000/create_booking)

**Cuerpo del Request**:
```json
{
  "booking_id": "B001",
  "user_data": {
    "name": "Josh Dun",
    "email": "joshdun123@example.com"
  }
}
