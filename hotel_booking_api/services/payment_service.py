class PaymentService:
    def __init__(self, mediator=None):
        self.mediator = mediator
        self.transactions = {}

    def process_payment(self, booking_id):
        print(" --- Processing payment --- ")
        self.transactions[booking_id] = "completed"
        if self.mediator:
            self.mediator.notify(self, "payment_processed", booking_id)
        return {"status": "Payment processed successfully"}

    def refund_payment(self, booking_id):
        if booking_id in self.transactions:
            print(" --- Refunding payment --- ")
            self.transactions[booking_id] = "refunded"
            if self.mediator:
                self.mediator.notify(self, "payment_refunded", booking_id)
            return {"status": "Payment refunded successfully"}
        return {"status": "Transaction not found"}
