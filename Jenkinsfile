pipeline {
    agent any
    
    // Define environment variables for the Python virtual environment
    environment {
        PYTHON_ENV = "venv"
    }

    stages {
        // --------------------------------------------------------
        // Stage 1: Checkout the code from the SCM (GitHub)
        // --------------------------------------------------------
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // --------------------------------------------------------
        // Stage 2: Set up the Python virtual environment
        // --------------------------------------------------------
        stage('Setup Environment') {
            steps {
                echo "Setting up Python virtual environment..."
                
                // Create a virtual environment to isolate dependencies
                // Using bat commands for Windows Jenkins agents
                bat '''
                    python -m venv %PYTHON_ENV%
                    call %PYTHON_ENV%\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        // --------------------------------------------------------
        // Stage 3: Run Unit Tests and Generate Coverage Report
        // --------------------------------------------------------
        stage('Unit Testing & Coverage') {
            steps {
                echo "Running pytest with coverage..."
                
                bat '''
                    call %PYTHON_ENV%\\Scripts\\activate
                    
                    :: Create a reports directory if it doesn't exist
                    if not exist reports mkdir reports
                    
                    :: Run pytest, output XML for Jenkins, and generate coverage report
                    pytest --cov=src tests/ --junitxml=reports/test-results.xml
                '''
            }
            post {
                always {
                    // Archive the JUnit-style XML report so Jenkins can visualize it
                    junit 'reports/test-results.xml'
                }
            }
        }

        // --------------------------------------------------------
        // Stage 4: Advanced Feature - Static Code Analysis
        // --------------------------------------------------------
        stage('Static Analysis (Pylint)') {
            steps {
                echo "Running Pylint for static code analysis..."
                
                bat '''
                    call %PYTHON_ENV%\\Scripts\\activate
                    
                    :: Run pylint on the src directory and output to a text file
                    :: The || exit 0 ensures the pipeline doesn't fail just because pylint found warnings
                    pylint src/ > reports/pylint-report.txt || exit 0
                '''
            }
            post {
                always {
                    // Save the static analysis report as a build artifact for review
                    archiveArtifacts artifacts: 'reports/pylint-report.txt', allowEmptyArchive: true
                }
            }
        }
    }

    // Post-build actions to handle pipeline outcomes
    post {
        success {
            echo "Pipeline executed successfully! Excellent work."
        }
        failure {
            echo "Pipeline failed. Review the logs, fix the code, and push again."
        }
    }
}