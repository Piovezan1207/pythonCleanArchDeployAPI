from ..interfaces.GatewaysInterfaces import ApplicationGatewayInterface
from ..interfaces.ExternalInterfaces import ApplicationExternalInterface
from ..entities.Application import Application
from ..entities.Reservation import Reservation
from ..entities.DateTime import DateTime

from typing import List, Optional

class ApplicationGateway(ApplicationGatewayInterface):
    def __init__(self, applicationExternal: ApplicationExternalInterface):
        self.applicationExternal = applicationExternal
    
    def instantiate(self, application: Application) -> Optional[str]: 
        applicationUrl = self.applicationExternal.requestCloudDeploy(application.id)
        if applicationUrl == None: raise Exception("Houve um erro na comunicação com a clouda para o deploy da aplicação")
        return applicationUrl
        
    def scheduleDeletion(self, reservation: Reservation) -> Optional[DateTime]: 
        dateTiem = self.applicationExternal.scheduleRequest(reservation.application.id, reservation.finalHour)
        if dateTiem == None: raise Exception("Houve um erro ao tentar agendar o delete da aplicação.")
        return dateTiem
    
    def delete(self, application: Application) -> Optional[bool]:
        status = self.applicationExternal.requestCloudDelete(application.id)
        if status == None: raise Exception("Houve um ero ao tentar deletar a aplicação.")
        return status
    
    def getApplicationById(self, applicationId: str) -> Optional[Application]:
        self.applicationExternal