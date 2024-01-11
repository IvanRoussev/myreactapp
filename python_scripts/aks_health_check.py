from azure.identity import DefaultAzureCredential
from azure.mgmt.containerservice import ContainerServiceClient

# Authenticate using Azure AD credentials (you can also use other authentication methods)
credential = DefaultAzureCredential()
aks_client = ContainerServiceClient(credential, "<Azure_Subscription_ID>")


aks_clusters = aks_client.managed_clusters.list("<Resource_Group_Name>")


for cluster in aks_clusters:
    cluster_name = cluster.name
    cluster_rg = cluster.resource_group
    cluster_status = cluster.provisioning_state
    print(f"Cluster Name: {cluster_name}")
    print(f"Resource Group: {cluster_rg}")
    print(f"Provisioning State: {cluster_status}\n")
