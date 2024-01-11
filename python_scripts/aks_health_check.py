import subprocess
from azure.identity import DefaultAzureCredential
from azure.mgmt.containerservice import ContainerServiceClient

# Replace these with your Azure subscription ID and AKS resource group and cluster name
subscription_id = "ca812dd6-3090-4981-8e92-e00e9bb060c2"
resource_group_name = "Denshi"
aks_cluster_name = "myDenshi-aks"
service_name = "react-app-service"
namespace = "default"


def check_aks_health():
    # Create Azure credentials
    credentials = DefaultAzureCredential()

    # Initialize the Azure Kubernetes Service client
    aks_client = ContainerServiceClient(credentials, subscription_id)

    try:
        # Get the AKS cluster
        aks_cluster = aks_client.managed_clusters.get(
            resource_group_name, aks_cluster_name
        )

        # Check the cluster provisioning state
        if aks_cluster.provisioning_state == "Succeeded":
            print("------------------------------------------------------------")
            print(f"AKS Cluster '{aks_cluster_name}' is provisioned and healthy.")
            print("------------------------------------------------------------")
            external_ip = get_service_external_ip(service_name)
            print(f"External IP of the service '{service_name}': {external_ip}")
            print("------------------------------------------------------------")
            print("Deployments in the cluster:")
            get_deployments_info(namespace)
            print("------------------------------------------------------------")
            print("Pods in the cluster:")
            get_pods_info(namespace)
            print("------------------------------------------------------------")
            print("Replicaset Info:")
            get_replicasets_info(namespace)
            print("------------------------------------------------------------")

        else:
            print(
                f"AKS Cluster '{aks_cluster_name}' is not yet provisioned or is in an unhealthy state."
            )

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def get_service_external_ip(service_name):
    try:
        command = f"kubectl get svc {service_name} -n {namespace} -o jsonpath='{{.status.loadBalancer.ingress[0].ip}}'"
        external_ip = subprocess.check_output(command, shell=True, text=True).strip()
        return external_ip
    except subprocess.CalledProcessError:
        return "External IP not available"


def get_pods_info(namespace):
    try:
        command = f"kubectl get pods -n {namespace} --show-labels"
        pods_info = subprocess.check_output(command, shell=True, text=True)
        print(pods_info)
    except subprocess.CalledProcessError:
        print("Error retrieving pod information")


def get_deployments_info(namespace):
    try:
        command = f"kubectl get deployments -n {namespace} --show-labels"
        deployments_info = subprocess.check_output(command, shell=True, text=True)
        print(deployments_info)
    except subprocess.CalledProcessError:
        return ["Error retrieving deployment information"]


def get_replicasets_info(namespace):
    try:
        command = f"kubectl get replicasets -n {namespace} --show-labels"
        replicasets_info = subprocess.check_output(command, shell=True, text=True)
        print(replicasets_info)
    except subprocess.CalledProcessError:
        return ["Error retrieving ReplicaSet information"]


if __name__ == "__main__":
    check_aks_health()
