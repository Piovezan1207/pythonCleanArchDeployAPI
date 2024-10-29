from ..interfaces.GatewaysInterfaces import ReservationGatewayInterface
from ..interfaces.ExternalInterfaces import ReservationsExternalInterface
from ..entities.DateTime import DateTime

from typing import List, Optional

class ReservationGatewayImp(ReservationGatewayInterface):
    def __init__(self, reservationsExternal: ReservationsExternalInterface):
        self.reservationsExternal = reservationsExternal

    def getReservationfromApi(self, id: str) -> Optional[DateTime]: 
        response = self.reservationsExternal.requestForReservation(id)
        if response == None: raise Exception("Houve um erro em se comunicar com a API da reserva.")
        return response
    
