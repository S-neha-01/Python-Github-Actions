# CI/CD Pipeline Implementation using GitHub Actions for a Python Application

<img width="2556" height="1450" alt="image" src="https://github.com/user-attachments/assets/9f0fdf9c-ba74-4472-8697-11ddd6221ebe" />



## 1. Repository Setup

### 1.1 Sample Python Application Repository

A sample Python application repository is used for this assignment:

Repository Link:
https://github.com/S-neha-01/Python-Github-Actions.git

This repository contains:
- A simple Python application (Factorial)
- Unit tests written using pytest
- A requirements.txt file for dependency management

<img width="2426" height="988" alt="image" src="https://github.com/user-attachments/assets/58772c3c-0a21-4540-b455-142ee27ca676" />

---

### 1.2 Branch Strategy

The repository uses the following branches:

- main – Represents the production-ready code
- staging – Used for validating changes before production

Both branches are created and maintained to support environment-based deployments.

<img width="1954" height="622" alt="image" src="https://github.com/user-attachments/assets/85b32311-d84a-4144-92b4-5685dedbeab8" />

---

## 2. GitHub Actions Workflow Setup

### 2.1 Workflow Directory

GitHub Actions workflows are stored inside the following directory:

.github/workflows/

This directory is created at the root of the repository.

---

### 2.2 Workflow File

A workflow file named ci.yml is created inside the directory:

.github/workflows/ci.yml

This file defines the complete CI/CD pipeline.

---

## 3. CI/CD Workflow Details

### 3.1 Workflow Triggers

The workflow is triggered on the following events:

- Push to main branch
- Push to staging branch
- Pull request to main branch
- Creation of a release tag

<img width="1962" height="656" alt="image" src="https://github.com/user-attachments/assets/d2633f87-8a51-4872-9309-fc01cdb954e5" />


---

### 3.2 Continuous Integration (CI) Job

The CI job ensures that the code is tested and ready for deployment.

Steps performed:

1. Checkout Code  
   Fetches the latest code from the GitHub repository.

2. Setup Python Environment  
   Installs the required Python version on the GitHub Actions runner.

3. Install Dependencies  
   Installs all Python dependencies using pip and requirements.txt.

4. Run Tests  
   Executes unit tests using the pytest framework.
   If tests fail, the pipeline stops.

5. Build Application  
   Prepares the application for deployment after successful tests.

---

### 3.3 Deploy to Staging

- Triggered when code is pushed to the staging branch
- Runs only after the CI job completes successfully
- Simulates deployment to a staging environment
- Ensures changes are validated before production release

---

### 3.4 Deploy to Production

- Triggered when a release tag is created
- Runs only after the CI job succeeds
- Simulates deployment to the production environment
- Ensures production deployment is version-controlled and stable

---

## 4. Environment Secrets

### 4.1 Use of GitHub Secrets

Sensitive data required during deployment is stored securely using GitHub Secrets.
This prevents exposure of confidential information in the source code.

---

### 4.2 Secrets Configuration

The following secrets are configured in the repository:

- STAGING_API_KEY
- PROD_API_KEY

<img width="2540" height="1416" alt="image" src="https://github.com/user-attachments/assets/55c1cea1-0bd0-43c9-b65b-9895a9b11bb9" />


<img width="2560" height="1440" alt="image" src="https://github.com/user-attachments/assets/0b5cfefc-c71c-44cf-9377-026c65a790a5" />

These secrets are accessed securely inside the GitHub Actions workflow.

The workflow configuration file is located at:

.github/workflows/ci-cd.yml

<img width="654" height="566" alt="image" src="https://github.com/user-attachments/assets/9346fecb-a884-4150-b048-f2199b731cb6" />

---

## 6. Workflow Execution Summary

Action | Outcome
------ | -------
Push to main | CI pipeline runs
Push to staging | CI + Staging deployment
Create release tag | CI + Production deployment
Test failure | Deployment is blocked



