from ..entities.Application import Application
from ..entities.Reservation import Reservation
from ..entities.DateTime import DateTime
from ..interfaces.GatewaysInterfaces import ApplicationGatewayInterface

import uuid
from datetime import datetime

class ApplicationUseCases:
    
    @staticmethod
    def createApplication(name: str):
        url = None #Uma aplicação começa sem uma url definida
        applicationId = uuid.uuid4()
        application = Application(name, applicationId, url)
        return application
    
    @staticmethod
    def loadApplication(applicationId: str, applicationGateway: ApplicationGatewayInterface):
        application = applicationGateway.getAPplicationById(applicationId) #NÃO IMPLEMENTADO
        
        application = Application("", applicationId, "")
        return application
    
    @staticmethod
    def instantiateApplication(applicationGateway: ApplicationGatewayInterface, application: Application):
        instantiatedApplication = applicationGateway.instantiate(application)
        if instantiatedApplication == None: raise Exception("Houve um problema ao instanciar a aplicação.")
        application.url = instantiatedApplication
        return application
    
    @staticmethod
    def scheduleApplicationDeletion(applicationGateway: ApplicationGatewayInterface, reservation: Reservation):
        schedule = applicationGateway.scheduleDeletion(reservation)
        if schedule == None: raise Exception("Houve um erro no momento de agendar a remoção da aplicação.")
        reservation.application.scheduledForDeletionInMinuts = ApplicationUseCases.dateTimeToMinuts(schedule)
        return reservation
    
    @staticmethod
    def dateTimeToMinuts(dateTime: DateTime):
        now = datetime.now().astimezone()
        return int((dateTime.value - now).total_seconds()/60)
    
    @staticmethod
    def deleteApplication(applicationGateway: ApplicationGatewayInterface, application: Application):
        status = applicationGateway.delete(application)
        return status