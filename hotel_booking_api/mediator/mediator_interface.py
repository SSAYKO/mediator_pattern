from abc import ABC, abstractmethod

class BookingMediator(ABC):
    @abstractmethod
    def notify(self, sender, event, booking_id):
        raise NotImplementedError()
