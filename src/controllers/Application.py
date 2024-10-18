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
        
        application = ApplicationUseCases.createApplication(applicationName)
        reservation = ReservationUseCases.createReservation(reservationId, application)
        reservation = ReservationUseCases.getReservationFromApi(reservationGateway, reservation)
        reservation.application = ApplicationUseCases.instantiateApplication(applicationGateway, reservation.application)
        reservation = ApplicationUseCases.scheduleApplicationDeletion(applicationGateway, reservation)
        
        applicationAdapter = ApplicationAdapter()
        
        return applicationAdapter.jsonApplicationCreated(application)
        
        
        
    
    @staticmethod
    def delete(applicationId: str,
               applicationExternal: ApplicationExternalInterface):
        
        applicationGateway = ApplicationGateway(applicationExternal)
        
        application = ApplicationUseCases.loadApplication(applicationId)
        application = applicationGateway.delete(application)
        
        applicationAdapter = ApplicationAdapter()
        
        return applicationAdapter.jsonApplicationDeleted(application)
    