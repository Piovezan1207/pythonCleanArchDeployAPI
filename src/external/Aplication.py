from ..interfaces.ExternalInterfaces import ApplicationExternalInterface
from ..entities.DateTime import DateTime

from typing import List, Optional

from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient

class NoderedAzureDeploy(ApplicationExternalInterface):
    def __init__(self):
       self.azureTenantId = None
       self.azureClientId = None
       self.azureClientSecret = None
       self.azureSubscriptionId = None
       self.azureResourceGroupName = None
       self.azureAppServicePanName = None
       self.azureLocation = None
       
       

    def requestCloudDeploy(self, applicationId: str) -> Optional[str]:
        
        credential = ClientSecretCredential(self.azureTenantId, 
                                            self.azureClientId, 
                                            self.azureClientSecret)
        
        azureAppServiceName = "nodered-{}".format(applicationId)
        noderedDockerImage = "piovezan1207/nodered-dashboard:v1.0.0"
        dockerRegistryServerUrl = "https://index.docker.io"
        
        azureWebClient = WebSiteManagementClient(credential, self.azureSubscriptionId)
        
        azureAppServicePlanId = "/subscriptions/730334bd-73f4-46b7-b300-83ddf84eb4c5/resourceGroups/resourceGroupNoderedCiber2/providers/Microsoft.Web/serverfarms/PlanAppServiceNoderedCiber2"
        
        azureAppService = azureWebClient.web_apps.begin_create_or_update(
            self.azureResourceGroupName,
            azureAppServiceName,
            {
                "location": self.azureLocation,
                "server_farm_id": azureAppServicePlanId, #app_service_plan.id,
                "site_config": {
                    "linux_fx_version": f"DOCKER|{noderedDockerImage}"
                },
                "app_settings": [
                    {
                        "name": "DOCKER_REGISTRY_SERVER_URL",
                        "value": dockerRegistryServerUrl,
                    }
                ]
            }
        ).result()
        
        return azureAppService.default_host_name
        
    
    def requestCloudDelete(self, applicationId: str) -> Optional[bool]:
        pass
    
    def scheduleRequest(self, id: str, datetime: DateTime) -> Optional[DateTime]:
        pass
    
    def getAPplicationById(self, applicationId: str) -> None:
        pass