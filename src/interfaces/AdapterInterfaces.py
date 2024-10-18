from abc import ABC, abstractmethod
from typing import List, Optional

class ApplicationAdapterInterfaces(ABC):
    
    @abstractmethod
    def jsonApplication() -> Optional[dict]:
        pass