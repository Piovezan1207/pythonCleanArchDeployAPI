from DateTime import DateTime
from Application import Application

class Reservation:
    def __init__(self, id: str, application: Application, finalHour: DateTime):
        if id == None: raise ValueError("ID invalido.")
        if application == None: raise ValueError("Application invalida.")

        self._id = id
        self._application = application
        self._finalHour = finalHour
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def application(self) -> Application:
        return self._application
    
    @property
    def finalHour(self) -> DateTime:
        return self.finalHour