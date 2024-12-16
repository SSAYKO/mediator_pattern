class NotificationService:
    def __init__(self, mediator=None):
        self.mediator = mediator
        self.notifications = []

    def send_confirmation(self, booking_id):
        print(" --- Sending booking confirmation --- ")
        self.notifications.append({"booking_id": booking_id, "type": "confirmation"})
        if self.mediator:
            self.mediator.notify(self, "confirmation_sent", booking_id)
        return {"status": "Confirmation sent"}

    def send_cancellation(self, booking_id):
        print("NotificationService: Sending booking cancellation.")
        self.notifications.append({"booking_id": booking_id, "type": "cancellation"})
        if self.mediator:
            self.mediator.notify(self, "cancellation_sent", booking_id)
        return {"status": "Cancellation sent"}
