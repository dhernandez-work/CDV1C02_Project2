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
* **Version Control:** Git & GitHub (Feature Branch Workflow, Semantic Versioning)

---

## 📁 Project Structure

    CDV1C02_Project2/
    │
    ├── src/
    │   ├── __init__.py         # Package initialization and single-source versioning (__version__)
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
    ├── Makefile                 # Environment build, Git, and Release automation
    ├── requirements.txt         # Project dependencies
    └── README.md                # Project documentation

---

## 🚀 Environment & Workflow Automation (Makefile)

This project utilizes a `Makefile` to streamline local development, standardize the production environment, and accelerate Git workflows.

* **`make dev`**: Cleans the workspace, builds the local development environment with a `(DEV)` prompt, and installs dependencies.
* **`make prod`**: Builds the isolated production server environment with a `(PROD)` prompt and installs dependencies.
* **`make clean`**: Safely removes the existing virtual environment.
* **`make push m="your commit message"`**: Automates the `git add .`, `git commit -m`, and `git push origin HEAD` sequence to dynamically push the current active branch.
* **`make tag v="1.0.0" m="Release notes"`**: Automates tagging the current commit and pushing the Semantic Version tag to GitHub for releases.

---

## 🧪 Testing Architecture & Coverage

* Implemented 17 unit test cases using `pytest` (9 for `test_student.py` and 8 for `test_class_group.py`)[cite: 1, 2].
* Validated core functionality, including object construction, getters/setters, equality, comparators, and string representations[cite: 2].
* Utilized `pytest-mock` to isolate the `assign_random_username` method, forcing `mock_random.randint` to return predictable integer values for consistent evaluation[cite: 2].
* Handled strict edge cases, such as comparing `Student` objects to integers, matching identical birthdays, and safely removing the final student in a `ClassGroup` array[cite: 1, 2].

---

## ⚙️ Continuous Integration Pipeline

The Jenkins pipeline provides automated verification of code quality after every build by performing the following stages:
* Constructs the isolated Python virtual environment automatically upon build initialization.
* Executes the comprehensive `pytest` suite and generates an XML coverage report.
* Performs thorough static code analysis via the `pysonar` CLI scanner.
* Packages and deploys artifacts to the local Production server environment.

---

## 📊 Code Quality & Metrics

The project successfully passed the SonarQube Quality Gate with the following metrics:
* Maintained **99.0%** overall code coverage with exactly **0.0%** duplicated lines.
* Achieved a perfect **'A' rating** across Security, Reliability, and Maintainability.
* **0** Bugs
* **0** Vulnerabilities
* **0** Security Hotspots
* **0** Code Smells

---

## 🌿 Git Workflow

Development was carried out using feature branches before merging into the `master` branch. 

Feature branches included:
* `feature/flask-deployment`
* `security/patch-secret-key`
* `security/patch-csrf-and-debug`
* `chore/ignore-coverage`

This workflow allowed new functionality, security patches, and pipeline improvements to be developed and tested independently before integration.

---

## ℹ️ About

Fork of **shittake/project2** for **CDV1C02 Project Part 2**.

The project demonstrates the practical application of Continuous Integration by combining automated builds, unit testing, code coverage analysis, static code analysis, and version control using industry-standard DevOps tools.