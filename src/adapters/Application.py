from ..interfaces.AdapterInterfaces import ApplicationAdapterInterfaces
from ..entities.Application import Application

class ApplicationAdapter(ApplicationAdapterInterfaces):
    def __init__(self):
        pass
    
    def jsonApplicationCreated(self, application: Application):
        value = {"url" : "https://{}".format(application.url),
                 "tempToFinish" : application.scheduledForDeletionInMinuts}
        
        return value
    
    def jsonApplicationDeleted(self, application: Application):
        value = {"Deleted" : application.id}
        
        return value
    
    def jsonApplicationError(self, message):
        value = {"status" : "Error",
                 "message" : str(message) }
        
        return value
    
    