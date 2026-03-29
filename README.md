![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

# Temperature Sensor IoT Simulation

## Purpose:
The purpose of this project is to showcase skills relevant to DevOps and Cloud Engineering. This project includes the development of three microservices with a PostgreSQL DB as a single two-tiered application, from app development to AWS provisioning. 

## [x] Phase 1: Dev Environment Setup & App Development

## 📂 Project Structure
```text

├── docker-compose.yml
├── .env.example
├── services/
│   ├── ingestor/         # Flask API
│   ├── alert_worker/     # Logic & Logging
│   └── simulator/       # Data Generation
├── scripts/
│   └── test_pipeline.sh  # Validation Script
└── README.md

`
### Development Enironment:
The first step was setup the environment that I would use for development. I converted a custom built gaming PC into a level 1 Hypervisor; using ESXi. On this I created a VM of Ubuntu Server 24.04 as the machine for housing source code and testing Docker Compose orchestration. After setting up the server I created the GitHub repository with two branches Main & Dev, cloning the blank (only containing this README and a .gitignore) repo in order to establish a connection. 

### Application Development:
The app itself is comprised of three microservices:
* Ingestor - This is the entry point for the application. It ingests simulated temperature sensor data and appends those entries to a PostgreSQL database.
* Alert - Queries the database to look for entries with a status other than normal, logging them in order to optimize readability. This service could integrate something like a Slack notification later (but that was beyond the scope of the purpose of the project since the focus was displaying clean coding practices, CI/CD and IaC)
* Simulator - A python script that creates a data payload, generating a random temp value and a sensor ID between 1 and 10

The application also uses a PostgreSQL DB. The three services listed above are containerized via docker and they alongside the DB are orchestrated via Docker Compose. A majority of the code edited was done via vscode ssh, editing files on the Ubuntu server from two different machines on the same network. 

| Layer | Technology |
| :--- | :--- |
| **Hypervisor** | VMWare ESXi 8.0 |
| **Runtime** | Docker / Docker Compose |
| **Database** | PostgreSQL 18.3 |
| **Backend** | Python 3.12 / Flask |
| **Virtualization** | Docker & Docker Compose|

### Lessons learned:
There were a few roadblocks. In initial iteration, I ran into errors about the other containers trying to communicate with the PostgreSQL container. These stemmed from misconfigurations in the actual code, as well as mismatches between env variables (between the file and then in practice), the files originally looking for sqlite (which was corrected to by copliot though it was not my intention) and the simulator function not looping so the infrastructure broke. 

I also would not edit code directly on the development server. Rather I would add a third branch (which I will be adding going into phase 2). I only included a main and dev branch, I should have created a staging branch to use for phase 2, and used the dev branch to automate the creation of the Docker containers so that the only access to that server would've been for checking logs to ensure the application was working as intended.
