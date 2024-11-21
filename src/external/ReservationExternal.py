from ..interfaces.ExternalInterfaces import ReservationsExternalInterface
from ..entities.DateTime import DateTime
from ..errors.ApiError import ApiError

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
        print(url)
        
        try:
            r = requests.get(url, timeout=2)
        except:
            raise Exception("Erro ao consultar o agendamento no sistema.")

        if r.status_code == 401 : raise ApiError(r.content)
        elif r.status_code != 200 : return None #raise Exception("Houve um erro ao requisitar a reserva na gac.")
        

        value = json.loads(r.content)
        print("Valor requisição" , value)

        
        if "final_time" in value:
            response = value["final_time"]
        elif "messagem" in value:
            response = value["messagem"]
            raise ApiError(response)
        else:
            return None
            
        return response 