from abc import ABC, abstractmethod
from typing import List, Optional

class ApplicationAdapterInterfaces(ABC):
    
    @abstractmethod
    def jsonApplicationCreated() -> Optional[dict]:
        pass
    
    @abstractmethod
    def jsonApplicationDeleted() -> Optional[dict]:
        pass
    
    