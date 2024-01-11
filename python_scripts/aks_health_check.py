import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.containerservice import ContainerServiceClient
from kubernetes import client, config


def get_aks_cluster_credentials(resource_group_name, aks_cluster_name):
    # Authenticate with Azure
    credentials = DefaultAzureCredential()
    subscription_id = (
        "ca812dd6-3090-4981-8e92-e00e9bb060c2"  # Replace with your subscription ID
    )

    # Initialize Azure SDK for AKS
    aks_client = ContainerServiceClient(credentials, subscription_id)

    # Get AKS cluster credentials
    aks_cluster = aks_client.managed_clusters.get(resource_group_name, aks_cluster_name)
    kubeconfig = aks_client.managed_clusters.get_access_profile(
        resource_group_name, aks_cluster_name, "clusterUser"
    ).kube_config

    # Set kubeconfig
    kubeconfig_str = kubeconfig.decode("utf-8")  # Decode the byte data to a string
    with open(os.path.expanduser("~/.kube/config"), "w") as kubeconfig_file:
        kubeconfig_file.write(kubeconfig_str)

    # Load Kubernetes configuration
    config.load_kube_config()


def monitor_pod_health():
    api = client.CoreV1Api()
    pods = api.list_pod(namespace="default")

    print("Pods in AKS Cluster:")
    for pod in pods.items:
        print(f"Pod: {pod.metadata.name}, Status: {pod.status.phase}")


def monitor_service_ports():
    api = client.CoreV1Api()
    services = api.list_service(namespace="default")

    print("Services in AKS Cluster:")
    for service in services.items:
        ports = ", ".join([str(port.port) for port in service.spec.ports])
        print(f"Service: {service.metadata.name}, Ports: {ports}")


def monitor_deployment_health():
    extensions_v1beta1 = client.ExtensionsV1beta1Api()
    deployments = extensions_v1beta1.list_deployment_for_all_namespaces()

    print("Deployments in AKS Cluster:")
    for deployment in deployments.items:
        desired_replicas = deployment.spec.replicas
        available_replicas = deployment.status.available_replicas

        print(f"Deployment: {deployment.metadata.name}")
        print(f"Desired Replicas: {desired_replicas}")
        print(f"Available Replicas: {available_replicas}")
        print()


if __name__ == "__main__":
    resource_group_name = "Denshi"
    aks_cluster_name = "myDenshi-aks"  # Replace with your AKS cluster name

    get_aks_cluster_credentials(resource_group_name, aks_cluster_name)

    monitor_pod_health()
    print("\n" + "=" * 40 + "\n")
    monitor_service_ports()
    print("\n" + "=" * 40 + "\n")
    monitor_deployment_health()
