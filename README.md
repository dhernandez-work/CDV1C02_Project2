# CDV1C02 - Python CI/CD Pipeline & Code Quality Automation

An attempt at Continuous Integration and Delivery (CI/CD) implementation for a modular Python application (`Student` and `ClassGroup` entities), featuring automated testing, coverage thresholds, static code analysis, and cross-platform (macOS and Windows) Jenkins pipeline orchestration.

---

## 🛠️ Tech Stack & Tools

* **Language:** Python 3.9+
* **Testing Framework:** `pytest`, `pytest-cov`, `pytest-mock`
* **Static Code Analysis:** `pylint`, SonarQube Cloud
* **CI/CD Automation:** Jenkins (Declarative Pipeline)
* **Version Control:** Git & GitHub (Feature Branch Workflow)

---

## 📁 Project Structure

```text
CDV1C02_Project2/
│
├── src/
│   ├── __init__.py
│   ├── student.py          # Student model with getters, setters, and comparators
│   └── class_group.py      # ClassGroup collection manager with abstraction logic
│
├── tests/
│   ├── __init__.py
│   ├── test_student.py      # Unit tests & mocks for Student class
│   └── test_class_group.py  # Unit tests & edge cases for ClassGroup class
│
├── .gitignore               # Environment and cache ignore rules
├── Jenkinsfile              # Cross-platform Declarative Pipeline script
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation