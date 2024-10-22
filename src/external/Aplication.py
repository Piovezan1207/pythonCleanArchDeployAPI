from ..interfaces.ExternalInterfaces import ApplicationExternalInterface
from ..entities.DateTime import DateTime
from ..entities.Application import Application

from typing import List, Optional

from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient

import os
import subprocess
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

class NoderedAzure(ApplicationExternalInterface):
    def __init__(self):
       self.azureTenantId = os.getenv("AZURE_TENANT_ID")
       self.azureClientId = os.getenv("AZURE_CLIENT_ID")
       self.azureClientSecret = os.getenv("AZURE_CLIENT_SECRET")
       self.azureSubscriptionId = os.getenv("AZURE_SUBSCRIPTION_ID")
       self.azureResourceGroupName = os.getenv("AZURE_RESOURCE_GROUP_NAME")
       self.azureAppServicePlanName= os.getenv("AZURE_APP_SERVICE_PLAN_NAME")
       self.azureLocation = os.getenv("AZURE_LOCATION")
       

    def requestCloudDeploy(self, applicationId: str) -> Optional[str]:
        
        # return "www.nodered.hubsenai.com"
        
        credential = ClientSecretCredential(self.azureTenantId, 
                                            self.azureClientId, 
                                            self.azureClientSecret)
        
        azureAppServiceName = "nodered-{}".format(applicationId)
        noderedDockerImage = "piovezan1207/nodered-dashboard:v1.0.0"
        dockerRegistryServerUrl = "https://index.docker.io"
        
        azureWebClient = WebSiteManagementClient(credential, self.azureSubscriptionId)
        
        azureAppServicePlanNew = "plan-nodered-{}".format(applicationId)
        
        azureResourceClient = ResourceManagementClient(credential, self.azureSubscriptionId)
        
        # azureResourceGroupName = "{}-{}".format(self.azureResourceGroupName, applicationId)
        
        print("Criando serviço nodered:\n Grupo de recursos: {}\n Nome app service:{}\n Plano de recursos: {}".format(
            self.azureResourceGroupName,
            azureAppServiceName,
            azureAppServicePlanNew))
        
        azureResourceClient.resource_groups.create_or_update(
            self.azureResourceGroupName,
            {'location': self.azureLocation}
        )
        
        azureAppServicePlan = azureWebClient.app_service_plans.begin_create_or_update(
            self.azureResourceGroupName,
            # self.azureAppServicePlanName,
            azureAppServicePlanNew,
            {
                "location": self.azureLocation,
                "sku": {"name": "B1", "size": "10", "family": "B", "capacity": 1},
                "reserved": True  # Para Linux, defina como True
            }
        ).result()
        
        azureAppService = azureWebClient.web_apps.begin_create_or_update(
            self.azureResourceGroupName,
            azureAppServiceName,
            {
                "location": self.azureLocation,
                "server_farm_id": azureAppServicePlan.id, #app_service_plan.id,
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
        
        print("{} criado com sucesso.".format(azureAppServiceName))
        
        return azureAppService.default_host_name
        
    
    def requestCloudDelete(self, applicationId: str) -> Optional[bool]:
        credential = ClientSecretCredential(self.azureTenantId, 
                                            self.azureClientId, 
                                            self.azureClientSecret)
        
        azureAppServiceName = "nodered-{}".format(applicationId)
        
        
        azureWebClient = WebSiteManagementClient(credential, self.azureSubscriptionId)
        # azureResourceGroupName = "{}-{}".format(self.azureResourceGroupName, applicationId)
        
        
        print("Excluindo serviço nodered:\n Grupo de recursos: {}\n Nome app service:{}".format(
            self.azureResourceGroupName,
            azureAppServiceName))
  
        try:
            delete_operation = azureWebClient.web_apps.delete(
                self.azureResourceGroupName,
                azureAppServiceName
            )
            print("{} excluido com sucesso.".format(azureAppServiceName))
            return True
        
        except Exception as e:
            raise Exception(e)
    
    def scheduleRequest(self, id: str, dateTime: DateTime) -> Optional[DateTime]:
        #IMPLEMENTAR!!
        
        adicionalTimeToCallSchedule = 1 
        
        newDateTime = dateTime.value + timedelta(minutes=adicionalTimeToCallSchedule)
        
        now = datetime.now().astimezone()
        tempInMinutsToCallSchedule =  int((newDateTime - now).total_seconds()/60)
        
        appUrl = os.getenv("APP_URL")
        requestToDeleteUrl = "{}/nodered/delete?id={}".format(appUrl, id)
        command = "echo \"curl -X GET {}\" | at now + {} minutes".format(requestToDeleteUrl, tempInMinutsToCallSchedule)
        
        os.system(command)
        
        print(command)
        
        return DateTime(newDateTime.strftime("%Y-%m-%dT%H:%M:%S.%f%z")) 
    
    def getAPplicationById(self, applicationId: str) -> None:
        #IMPLEMENTAR!!
        return   Application("", applicationId, "")