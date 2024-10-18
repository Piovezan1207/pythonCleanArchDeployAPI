from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.DateTime import DateTime
from ..entities.Application import Application
from ..entities.Reservation import Reservation

class ReservationGatewayInterface(ABC):

    @abstractmethod 
    def getReservationfromApi(id: str) -> Optional[DateTime]: 
        pass

class ApplicationGatewayInterface(ABC):
    
    @abstractmethod
    def instantiate(application: Application) -> Optional[str]: 
        pass
    
    @abstractmethod
    def scheduleDeletion(reservation: Reservation) -> Optional[DateTime]: 
        pass
    
    @abstractmethod
    def delete(application: Application) -> Optional[bool]:
        pass
    
    @abstractmethod
    def getApplicationById(applicationId: str) -> Optional[Application]:
        pass