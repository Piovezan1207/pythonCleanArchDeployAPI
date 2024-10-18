from ..interfaces.ExternalInterfaces import ReservationsExternalInterface
from ..entities.DateTime import DateTime

import json
import requests

import os
from dotenv import load_dotenv

load_dotenv()

class GacReservations(ReservationsExternalInterface):
    def __init__(self):
        self.gacUrl = os.getenv("GAC_URL")
    
    def requestForReservation(self, id):
        
        # return DateTime('2024-10-18T19:31:45.739Z')
        
        parameter = "{}".format(id)
        url = "{}/{}".format(self.gacUrl, parameter)
        
        r = requests.get(url, timeout=2)
        
        if r.status_code != 200: return None #raise Exception("Houve um erro ao requisitar a reserva na gac.")
        
        print(r.content)
        
        try:
            response = r.content["final_time"], True
        except:
            try:
                response = r.content["messagem"], False
            except:
                return None
            
            
        return response 