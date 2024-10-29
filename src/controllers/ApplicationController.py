from ..usecases.ReservationUseCases import ReservationUseCases
from ..usecases.ApplicationUseCases import ApplicationUseCases
from ..gateways.ReservationGateway import ReservationGatewayImp
from ..gateways.ApplicationGateway import ApplicationGatewayImp
from ..interfaces.ExternalInterfaces import ApplicationExternalInterface, ReservationsExternalInterface
from ..adapters.ApplicationPresenter import ApplicationAdapterImp

class ApplicationController:
    @staticmethod
    def instantiate(reservationId: str, 
                    applicationName: str,
                    applicationExternal: ApplicationExternalInterface, 
                    reservationExternal: ReservationsExternalInterface):
        
        reservationGateway = ReservationGatewayImp(reservationExternal)
        applicationGateway = ApplicationGatewayImp(applicationExternal)
        
        applicationAdapter = ApplicationAdapterImp()
    
        
        application = ApplicationUseCases.createApplication(applicationName)
        reservation = ReservationUseCases.createReservation(reservationId, application)

        reservation = ReservationUseCases.getReservationFromApi(reservationGateway, reservation)
        
        reservation.application = ApplicationUseCases.instantiateApplication(applicationGateway, reservation.application)
        reservation = ApplicationUseCases.scheduleApplicationDeletion(applicationGateway, reservation)
        
        
        return applicationAdapter.jsonApplicationCreated(application)
        
        
        
    
    @staticmethod
    def delete(applicationId: str,
               applicationExternal: ApplicationExternalInterface):
        
        applicationGateway = ApplicationGatewayImp(applicationExternal)
        
        application = ApplicationUseCases.loadApplication(applicationId, applicationGateway)
        status = ApplicationUseCases.deleteApplication(applicationGateway, application) 
        
        applicationAdapter = ApplicationAdapterImp()
        
        if status:
            return applicationAdapter.jsonApplicationDeleted(application)
        else:
            return applicationAdapter.jsonApplicationError("Erro ao deletar a aplicação de ID {}".format(application.id))