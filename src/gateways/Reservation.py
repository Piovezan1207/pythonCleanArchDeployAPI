from ..interfaces.GatewaysInterfaces import ReservationGatewayInterface
from ..interfaces.ExternalInterfaces import ReservationsExternalInterface
from ..entities.DateTime import DateTime

from typing import List, Optional

class ReservationGateway(ReservationGatewayInterface):
    def __init__(self, reservationsExternal: ReservationsExternalInterface):
        self.reservationsExternal = reservationsExternal

    def getReservationfromApi(self, id: str) -> Optional[DateTime]: 
        date = self.reservationsExternal.requestForReservation(id)
        if date == None: raise Exception("Houve um erro em se comunicar com a API da reserva.")
        return date
    