from .mediator_interface import BookingMediator

class HotelBookingMediator(BookingMediator):
    def __init__(self, booking_service, payment_service, notification_service, inventory_service):
        self.booking_service = booking_service
        self.payment_service = payment_service
        self.notification_service = notification_service
        self.inventory_service = inventory_service

    def notify(self, sender, event, booking_id):
        if event == "booking_created":
            print("Mediator: Processing booking creation...")
            self.inventory_service.update_availability(booking_id)
            self.payment_service.process_payment(booking_id)
            self.notification_service.send_confirmation(booking_id)
        elif event == "booking_cancelled":
            print("Mediator: Processing booking cancellation...")
            self.inventory_service.update_availability(booking_id, cancel=True)
            self.payment_service.refund_payment(booking_id)
            self.notification_service.send_cancellation(booking_id)
        elif event == "payment_processed":
            print(f"Mediator: Payment for booking {booking_id} has been processed.")
        elif event == "payment_refunded":
            print(f"Mediator: Payment for booking {booking_id} has been refunded.")
        elif event == "confirmation_sent":
            print(f"Mediator: Confirmation for booking {booking_id} has been sent.")
        elif event == "cancellation_sent":
            print(f"Mediator: Cancellation for booking {booking_id} has been sent.")
        elif event == "availability_updated":
            print(f"Mediator: Availability updated after booking {booking_id}.")
        elif event == "availability_restored":
            print(f"Mediator: Availability restored after cancellation of booking {booking_id}.")
