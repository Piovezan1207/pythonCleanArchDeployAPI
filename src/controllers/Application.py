from ..usecases.ReservationUseCases import ReservationUseCases
from ..usecases.ApplicationUseCases import ApplicationUseCases
from ..gateways.Reservation import ReservationGateway
from ..gateways.Application import ApplicationGateway
from ..interfaces.ExternalInterfaces import ApplicationExternalInterface, ReservationsExternalInterface
from ..adapters.Application import ApplicationAdapter

class Application:
    @staticmethod
    def instantiate(reservationId: str, 
                    applicationName: str,
                    applicationExternal: ApplicationExternalInterface, 
                    reservationExternal: ReservationsExternalInterface):
        
        reservationGateway = ReservationGateway(reservationExternal)
        applicationGateway = ApplicationGateway(applicationExternal)
        
        applicationAdapter = ApplicationAdapter()
    
        
        application = ApplicationUseCases.createApplication(applicationName)
        reservation = ReservationUseCases.createReservation(reservationId, application)
        
        try:
            reservation = ReservationUseCases.getReservationFromApi(reservationGateway, reservation)
        except Exception as e:
            return applicationAdapter.jsonApplicationError(e)
        
        reservation.application = ApplicationUseCases.instantiateApplication(applicationGateway, reservation.application)
        reservation = ApplicationUseCases.scheduleApplicationDeletion(applicationGateway, reservation)
        
        
        return applicationAdapter.jsonApplicationCreated(application)
        
        
        
    
    @staticmethod
    def delete(applicationId: str,
               applicationExternal: ApplicationExternalInterface):
        
        applicationGateway = ApplicationGateway(applicationExternal)
        
        application = ApplicationUseCases.loadApplication(applicationId, applicationGateway)
        status = ApplicationUseCases.deleteApplication(applicationGateway, application) 
        
        applicationAdapter = ApplicationAdapter()
        
        if status:
            return applicationAdapter.jsonApplicationDeleted(application)
        else:
            return applicationAdapter.jsonApplicationError("Erro ao deletar a aplicação de ID {}".format(application.id))