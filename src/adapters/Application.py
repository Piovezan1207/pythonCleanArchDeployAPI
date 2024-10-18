from ..interfaces.AdapterInterfaces import ApplicationAdapterInterfaces
from ..entities.Application import Application

class ApplicationAdapter(ApplicationAdapterInterfaces):
    def __init__(self, application: Application):
        pass
    
    def jsonApplicationCreated(self, application: Application):
        value = {"url" : application.url,
                 "tempToFinish" : application.scheduledForDeletionInMinuts}
        
        return value
    
    def jsonApplicationDeleted(self, application: Application):
        value = {"Deleted" : application.id}
        
        return value