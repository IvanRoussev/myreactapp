# Access my React app:

http://52.142.37.60/

# React App Containerization Guide

This guide will help you run a containerized React application using the provided Python script and Docker.

## Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your system:

- Python 3.x
- Docker

## Usage

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
