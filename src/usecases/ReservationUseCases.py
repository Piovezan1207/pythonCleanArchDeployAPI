from ..interfaces.GatewaysInterfaces import ReservationGatewayInterface
from ..entities.Reservation import Reservation, DateTime

from typing import List, Optional

class ReservationUseCases:
    
    @staticmethod
    def createReservation(reservationId: str, application: str):
        return Reservation(reservationId, application, None)
    
    @staticmethod
    def getReservationFromApi(reservationGateway: ReservationGatewayInterface, reservation: Reservation) -> Optional[DateTime]:
        reservationApiEndTime = reservationGateway.getReservationfromApi(reservation.id)
        # if response == None: raise Exception(response[0])
        # finalHour = DateTime(reservationApiEndTime) #Essa responsabilidade foi passada para o gateway
        # print(reservationApiEndTime.value)
        reservation.finalHour = DateTime(reservationApiEndTime)
        return reservation