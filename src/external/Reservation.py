from ..interfaces.ExternalInterfaces import ReservationsExternalInterface
from ..entities.DateTime import DateTime

import json
import requests

class GacReservations(ReservationsExternalInterface):
    def __init__(self):
        self.gacUrl = None
    
    def requestForReservation(self, id):
        
        return DateTime('2024-10-18T18:23:45.739Z')
        
        parameter = "{}".format(id)
        url = "{}/{}".format(self.gacUrl, parameter)
        
        r = requests.get(url, timeout=2)
        
        if r.status_code != 200: return None #raise Exception("Houve um erro ao requisitar a reserva na gac.")
        
        try:
            content = r.content["final_time"]
        except:
            return None #raise Exception("A reserva da gac não retortou o horario de finalização.")
        
        return content 