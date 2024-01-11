# Explaining

1. Pipeline
1. Python Automation Scripts

# Access my React app:

http://52.142.37.60/

The React app is hosted on a Kubernetes Cluster in Azure. To access the app, you can use the provided URL. Additionally, here are some deployment details:

- **Kubernetes Cluster:** Configured by deployment.yaml where it creates deployment and service for cluster
- **Continuous Integration and Deployment Pipeline:**

## Pipeline Overview

The continuous integration and deployment (CI/CD) pipeline for this project automates various tasks, including building, testing, and deploying the React application. Here's an overview of the pipeline stages and what each of them does:

### Stage 1: Build and Push Image

- **Description:** This stage builds a Docker image of the React application and pushes it to an Azure Container Registry (ACR).
- **Steps:**
  1. **Login to ACR:** Authenticate with the ACR using Docker.
  2. **Build Image and Push to ACR:** Build the Docker image from the specified Dockerfile and push it to the ACR.
- **Image Name:** The Docker image is tagged with a unique identifier (e.g., Build ID) and named 'react-app-image'.

### Stage 2: Test React App

- **Description:** This stage is responsible for testing the React application.
- **Steps:**
  1. **Testing App:** Executes any necessary tests for the application.
  2. **Successful Testing:** Indicates that the testing process has completed successfully.

### Stage 3: Deploy React App to Kubernetes Cluster

- **Description:** This final stage deploys the React application to a Kubernetes Cluster in Azure.
- **Steps:**
  1. **Kubernetes Deployment:** Utilizes a Kubernetes task to apply the configuration defined in `k8s/deployment.yaml`.
  2. **Azure Resource Manager Connection:** Uses Azure Resource Manager to connect to the Azure subscription.
  3. **Azure Container Registry:** Specifies the Azure Container Registry as the source for Docker images.
  4. **Kubernetes Cluster:** Deploys the application to the specified Kubernetes cluster.
  5. **Namespace:** Places the application in the 'default' namespace.
  6. **Secrets and Registry Configuration:** Manages Docker registry secrets and configurations.
  7. **Force Update:** Determines whether to force an update.

# React App Containerization Guide

This guide will help you run a containerized React application using the provided Python script and Docker.

## Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your system:

- Python 3.x
- Docker

## Usage

# About docker_automation.py

To run the container for the React app, follow these steps:

1. Open your terminal and navigate to the directory where your Python script is located.

2. Run the Python script `automate_build_process.py` with the following arguments:

   - `arg1`: React image name (e.g., `react-image`).
   - `arg2`: Path to the Dockerfile for the React app.
   - `arg3`: The desired container name (e.g., `reactapp`).
   - `arg4`: Use `--rebuild` if you want to rebuild the image. Leave it empty if you don't want to rebuild the image.

   Example:

   ```bash
   python3 automate_build_process.py react-image . reactapp --rebuild
   ```

   Also: Outputs Log to external file called `automation.log`

# About aks_health_check.py

Here's a brief explanation of the key functions in the script:

- `check_aks_health()`: This function checks the provisioning state of the AKS cluster and provides information about its health. It also retrieves the external IP of a specified service in the cluster.

- `get_service_external_ip(service_name)`: This function fetches the external IP of a Kubernetes service using the `kubectl` command.

- `get_pods_info(namespace)`: Retrieves information about pods within a specified namespace using the `kubectl` command.

- `get_deployments_info(namespace)`: Retrieves information about deployments within a specified namespace using the `kubectl` command.

- `get_replicasets_info(namespace)`: Retrieves information about replica sets within a specified namespace using the `kubectl` command.

To use the script:

1. Replace the placeholders for `subscription_id`, `resource_group_name`, `aks_cluster_name`, `service_name`, and `namespace` with the appropriate values for your AKS cluster.

2. Make sure you have the Azure SDK installed and `kubectl` configured correctly on your local machine.

3. Run the script using Python 3:

   ```bash
   python3 your_script_name.py
   ```
