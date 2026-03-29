# Temperature Sensor IoT Simulation

## Purpose:
The purpose of this project is to showcase skills relevant to DevOps and Cloud Engineering. This project includes the development of three microservices with a PostgreSQL DB as a single two-tiered application, from app development to AWS provisioning. 

## Phase 1: Dev Environment Setup & App Development
### Development Enironment:
The first step was setup the environment that I would use for development. I converted a custom built gaming PC into a level 1 Hypervisor; using ESXi. On this I created a VM of Ubuntu Server 24.04 as the machine for housing source code and testing Docker Compose orchestration. After setting up the server I created the GitHub repository with two branches Main & Dev, cloning the blank (only containing this README and a .gitignore) repo in order to establish a connection. 

### Application Development:
The app itself is comprised of three microservices:
* Ingestor - This is the entry point for the application. It ingests simulated temperature sensor data and appends those entries to a PostgreSQL database.
* Alert - Queries the database to look for entries with a status other than normal, logging them in order to optimize readability. This service could integrate something like a Slack notification later (but that was beyond the scope of the purpose of the project since the focus was displaying clean coding practices, CI/CD and IaC)
* Simulator - A python script that creates a data payload, generating a random temp value and a sensor ID between 1 and 10
