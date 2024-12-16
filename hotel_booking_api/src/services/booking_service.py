from datetime import datetime

class BookingService:
    def __init__(self, mediator=None):
        self.mediator = mediator
        self.bookings = {}

    def create_booking(self, booking_id, user_data, date=None):
        print(" --- Creating a new booking --- ")
        
        if booking_id in self.bookings:
            return {"status": "Error: Booking ID already exists", "booking_id": booking_id}

        date = date or datetime.now().isoformat()
        self.bookings[booking_id] = {"user_data": user_data, "date": date}

        if self.mediator:
            self.mediator.notify(self, "booking_created", booking_id)
        
        return {"status": "Booking created successfully", "booking_id": booking_id, "date": date}

    def cancel_booking(self, booking_id):
        if booking_id in self.bookings:
            print(" --- Cancelling booking --- ")
            del self.bookings[booking_id]
            if self.mediator:
                self.mediator.notify(self, "booking_cancelled", booking_id)
            return {"status": "Booking cancelled successfully"}
        return {"status": "Booking not found"}
