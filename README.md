# CDV1C02 - Python CI/CD Pipeline & Code Quality Automation

A comprehensive Continuous Integration and Continuous Deployment (CI/CD) implementation for a modular Python web application. This project features a Flask-based web interface (secured with Flask-WTF), automated testing, coverage thresholds, static code analysis, cross-platform Jenkins pipeline orchestration, and streamlined environment management using Makefiles and direnv.

---

## 🛠️ Tech Stack & Tools

* **Language:** Python 3.9+
* **Web Framework & Security:** Flask, Flask-WTF (CSRF Protection)
* **Testing Framework:** `pytest`, `pytest-cov`, `pytest-mock`
* **Static Code Analysis:** `pylint`, SonarQube Cloud
* **CI/CD Automation:** Jenkins (Declarative Pipeline)
* **Environment Management:** `Makefile`, `direnv`
* **Version Control:** Git & GitHub (Feature Branch Workflow)

---

## 📁 Project Structure

    CDV1C02_Project2/
    │
    ├── src/
    │   ├── __init__.py
    │   ├── student.py          # Student model with getters, setters, and comparators
    │   └── class_group.py      # ClassGroup collection manager with abstraction logic
    │
    ├── templates/
    │   └── index.html          # Web interface template with CSRF tokens
    │
    ├── tests/
    │   ├── __init__.py
    │   ├── test_student.py      # Unit tests & mocks for Student class
    │   └── test_class_group.py  # Unit tests & edge cases for ClassGroup class
    │
    ├── .envrc                   # direnv configuration for directory jumps (Local/Gitignored)
    ├── .gitignore               # Environment and cache ignore rules
    ├── app.py                   # Flask application routing and logic
    ├── Jenkinsfile              # Cross-platform Declarative Pipeline script
    ├── Makefile                 # Environment build and Git workflow automation
    ├── requirements.txt         # Project dependencies
    └── README.md                # Project documentation

---

## 🚀 Environment & Workflow Automation (Makefile)

This project utilizes a `Makefile` to streamline local development, standardize the production environment, and accelerate Git workflows.

* **`make dev`**: Cleans the workspace, builds the local development environment with a `(DEV)` prompt, and installs dependencies.
* **`make prod`**: Builds the isolated production server environment with a `(PROD)` prompt and installs dependencies.
* **`make clean`**: Safely removes the existing virtual environment.
* **`make push m="your commit message"`**: Automates the `git add .`, `git commit -m`, and `git push origin master` sequence.