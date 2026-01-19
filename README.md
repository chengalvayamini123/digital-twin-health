# Digital Twin Health Monitoring System

## Project Overview  
This project simulates a Digital Twin of a human health monitoring system using real-time sensor data.  
It visualizes Body Temperature, Heart Rate, SpO₂, Blood Pressure, and Fan Status on a live dashboard.  
The system is built using Python, Node-RED, Docker, and Kubernetes (Minikube).

---

## Objective  
To simulate real-time health vitals, visualize them on a dashboard, and deploy the system using containerization and orchestration tools.

---

## System Architecture  

Python Sensor Simulator → Node-RED HTTP API → Dashboard UI  
Deployed using Docker → Orchestrated using Kubernetes (Minikube)

---

## Technologies Used  

- Python (sensor simulation)  
- Node-RED (data processing and dashboard)  
- Node-RED Dashboard  
- Docker (containerization)  
- Kubernetes (Minikube)  
- YAML (deployment and service files)  

---

## Features  

- Real-time sensor data simulation  
- Live health monitoring dashboard  
- Automatic fan control based on temperature  
- Dockerized Node-RED environment  
- Kubernetes deployment  
- Scalable architecture  

---

## Project Structure  

DIGITAL-TWIN-HEALTH/
│
├── docker/
│ ├── Dockerfile
│ └── flows.json
│
├── k8s/
│ ├── deployment.yaml
│ └── service.yaml
│
├── node-red/
│
├── python/
│ └── sensor_sim.py

---

## How It Works  

1. Python script generates random health vitals  
2. Data is sent via HTTP POST to Node-RED  
3. Node-RED processes the data  
4. Dashboard displays live values  
5. Fan turns ON or OFF based on temperature  
6. System runs inside Docker  
7. Kubernetes manages the deployment  

---

## How to Run  

### Run Python Sensor  
python sensor_sim.py

### Build Docker Image  
docker build -t digital-twin-health .

### Run Container  
docker run -p 1880:1880 digital-twin-health

### Start Kubernetes  
minikube start
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
minikube service digital-twin-service


---

## Dashboard Output  

The dashboard displays:  
- Body Temperature  
- Heart Rate  
- SpO₂  
- Blood Pressure  
- Fan Status  

---

## Use Cases  

- Smart healthcare systems  
- Remote patient monitoring  
- IoT and Digital Twin simulations  
- DevOps and Cloud learning  

---

## Developer  

Yamini
Aspiring Software Engineer
Learning Cloud and DevOps through hands-on projects  

