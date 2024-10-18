from Reservation import Reservation
from DateTime import DateTime
from typing import List, Optional

class Aplication:
    def __init__(self, name: str, id: str, url: str):
        if name is None: raise ValueError("Nome invalido.")
        
        self._name = name
        self._id = id
        self._url = url
        self._scheduledForDeletion = None
        
        
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def url(self) -> str:
        return self._url
    
    @property
    def scheduledForDeletion(self) -> Optional[DateTime]:
        return self._scheduledForDeletion
