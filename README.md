# TAT2
An automated immutable framework for CTFs and Bug Bounties

## Goal
The goal is for anybody to deploy the framework with the modules of their choice, and they will deploy successfully without dependencies preventing immutability.

## Features
- Automated module installation with version control.
- Standardized input/output format across modules.
- Modular architecture allowing users to select specific tools to prevent bloatware.
- Environment isolation to ensure consistent deployment using Docker.

## Module Requirements
- Each module should be a directory containing the main code, required imports, and specified version numbers.
- Modules must account for dependencies such as protocol requirements (e.g., http/s) for inputs.
- Modules should mark their tools' executing language and handle required library installations.
- Modules must produce standardized output (e.g., text files, database entries) and sanitize inputs for consistency.
- Modules must include a Dockerfile if they depend on non-Python languages or require compilation (e.g., Go).

## Workflow
1. Sub-domain Enumeration
2. Port Scanning
3. Web Crawling
4. WHOIS Lookup
5. DNS Enumeration
6. Vulnerability Scanning
7. Exploitation
8. Information Gathering
9. Reporting
10. Automation and Scripting
11. Utility

## Example Module Template (Go-lang)
```python
##### REQUIRED FOR MODULES #####
import os
import sys

# domain = input("Insert SINGLE domain you would like to run hakrawler scanner on: ")
cwd = os.getcwd()
os.environ['PATH'] = f'{cwd}/go/bin:' + os.environ['PATH']
os.environ['GOPATH'] = cwd
##### REQUIRED FOR MODULES #####
```

## Installation
1. Clone the repository.
2. Run `tat2_setup.sh` to set up the project structure.
3. Use `docker-compose` to start the backend, frontend, and selected modules.
4. Select tools during deployment to avoid installing unused modules.

## Usage
- To add a module, place it in the appropriate directory under `modules/`.
- Ensure each module follows the template and handles its own dependencies.
- Use the provided CI/CD pipeline to automate testing and deployment.
