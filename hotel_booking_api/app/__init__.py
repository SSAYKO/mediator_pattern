from flask import Flask
from services.booking_service import BookingService
from services.payment_service import PaymentService
from services.notification_service import NotificationService
from services.inventory_service import InventoryService
from mediator.hotel_booking_mediator import HotelBookingMediator

app = Flask(__name__)

# Instanciación de servicios y el mediador
booking_service = BookingService()
payment_service = PaymentService()
notification_service = NotificationService()
inventory_service = InventoryService()
mediator = HotelBookingMediator(booking_service, payment_service, notification_service, inventory_service)

# Asignación del mediador a cada servicio
booking_service.mediator = mediator
payment_service.mediator = mediator
notification_service.mediator = mediator
inventory_service.mediator = mediator
