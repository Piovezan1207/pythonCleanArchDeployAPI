from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.Application import Application
from ..entities.DateTime import DateTime 

class ApplicationExternalInterface(ABC):
     
    @abstractmethod
    def requestCloudDeploy(applicationId: str) -> Optional[str]:
        pass
    
    @abstractmethod
    def requestCloudDelete(applicationId: str) -> Optional[bool]:
        pass
    
    @abstractmethod
    def scheduleRequest(id: str, datetime: DateTime) -> Optional[DateTime]:
        pass
    
    @abstractmethod
    def getAPplicationById(applicationId: str) -> None:
        pass

class ReservationsExternalInterface(ABC):
    
    @abstractmethod
    def requestForReservation(id: str) -> Optional[DateTime]:
        pass
