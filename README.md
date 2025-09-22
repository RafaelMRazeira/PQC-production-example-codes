# PQC Production Example Codes

## Overview
This repository provides example code demonstrating the usage of Post-Quantum Cryptography (PQC) in production environments. It aims to showcase practical implementations of PQC algorithms to help developers integrate quantum-resistant cryptographic techniques into their applications.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction
Post-Quantum Cryptography (PQC) refers to cryptographic algorithms designed to be secure against quantum computing attacks. This repository includes Python-based examples to demonstrate how to implement PQC algorithms for real-world applications, focusing on usability and production readiness. Those examples are VERY simplified, so use with CAUTION!

## Features
- Implementation of NIST-standardized PQC algorithms (e.g., Kyber, Dilithium).
- Examples of key generation, encryption, decryption, and digital signatures.
- Production-ready code with error handling and performance considerations.
- Modular design for easy integration into existing systems.
- Docker support for simplified setup and deployment.

## Installation
To use the code in this repository, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/RafaelMRazeira/PQC-production-example-codes.git
   cd PQC-production-example-codes
   ```

2. **Set up a Python environment**:
   Ensure you have Python 3.8+ installed. It's recommended to use a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   Install the required Python packages (e.g., `oqs-python` for liboqs integration):
   ```bash
   pip install -r requirements.txt
   ```

   *Note*: Ensure you have the necessary libraries (e.g., `liboqs`) installed. Refer to the [liboqs-python documentation](https://github.com/open-quantum-safe/liboqs-python) for setup instructions.

## Usage - Docker (Recommended)
The repository includes a `Dockerfile` and `docker-compose.yml` for easy setup and execution of the PQC application in a containerized environment. This approach ensures consistent dependencies and simplifies deployment.

### Prerequisites
- Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).

### Steps
1. **Start the application**:
   Run the following command to build and start the server using Docker Compose:
   ```bash
   docker compose up -d
   ```
   This command starts the server in detached mode, allowing it to run in the background.

2. **Build and run the client**:
   Execute the following commands to build and run the client application:
   ```bash
   make build_client
   make run_client
   ```
   These commands generate a private/public key pair and send a test message from the client to the server.

3. **Verify output**:
   Check the server logs in the Docker Compose terminal to confirm successful operation. You should see output similar to the following:
   ```bash
   pqc-server-1  | 2025-09-22T11:23:47.694226+00:00 | INFO | Key set successfully | {}
   pqc-server-1  | 2025-09-22T11:23:47.698460+00:00 | INFO | Message received: Hello, secure world! | {}
   ```

4. **Stop the application**:
   When finished, stop and remove the Docker containers:
   ```bash
   docker compose down
   ```

### Notes
- Ensure ports used by the application (defined in `docker-compose.yml`) are not occupied.
- If you encounter issues, check the Docker logs for debugging:
  ```bash
  docker compose logs
  ```

## Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Please ensure your code follows the repository's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or suggestions, feel free to reach out to the repository owner:

- GitHub: [RafaelMRazeira](https://github.com/RafaelMRazeira)