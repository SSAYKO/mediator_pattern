class InventoryService:
    def __init__(self, mediator=None):
        self.mediator = mediator
        self.inventory = {"available_rooms": 10}

    def update_availability(self, booking_id,  cancel=False):
        if cancel:
            print("--- Restoring availability due to booking cancellation ---")
            self.inventory["available_rooms"] += 1
        else:
            print("--- Reducing availability due to new booking --- ")
            self.inventory["available_rooms"] -= 1
        if self.mediator:
            event = "availability_restored" if cancel else "availability_updated"
            self.mediator.notify(self, event, booking_id)
        return {"status": "Availability updated", "available_rooms": self.inventory["available_rooms"]}
    
    def check_availability(self):
        available_rooms = self.inventory.get("available_rooms", 0)
        print(f"--- Checking availability: {available_rooms} rooms available ---")
        return available_rooms > 0
