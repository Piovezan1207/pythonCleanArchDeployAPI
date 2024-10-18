from .DateTime import DateTime
from typing import List, Optional

class Application:
    def __init__(self, name: str, id: str, url: str):
        if name is None: raise ValueError("Nome invalido.")
        
        self._name = name
        self._id = id
        self._url = url
        self._scheduledForDeletionInMinuts = None
        
        
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def url(self) -> str:
        return self._url
    
    @url.setter
    def url(self, url):
        self._url= url
    
    @property
    def scheduledForDeletionInMinuts(self) -> Optional[DateTime]:
        return self._scheduledForDeletionInMinuts
    
    @scheduledForDeletionInMinuts.setter
    def scheduledForDeletionInMinuts(self, scheduledForDeletionInMinuts):
        self._scheduledForDeletionInMinuts = scheduledForDeletionInMinuts
