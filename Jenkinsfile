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
        // Stage 2: Set up the Python virtual environment & Log Version
        // --------------------------------------------------------
        stage('Setup Environment') {
            steps {
                echo "Setting up Python virtual environment..."
                
                // Create a virtual environment to isolate dependencies
                // Dynamically execute OS-specific commands
                script {
                    if (isUnix()) {
                        // macOS / Linux commands
                        sh '''
                            python3 -m venv ${PYTHON_ENV}
                            source ${PYTHON_ENV}/bin/activate
                            python3 -m pip install --upgrade pip
                            pip install -r requirements.txt
                            
                            echo "=== Building Application Version ==="
                            python3 -c "import src; print(src.__version__)"
                        '''
                    } else {
                        // Windows commands
                        bat '''
                            python -m venv %PYTHON_ENV%
                            call %PYTHON_ENV%\\Scripts\\activate.bat
                            python -m pip install --upgrade pip
                            pip install -r requirements.txt
                            
                            echo === Building Application Version ===
                            python -c "import src; print(src.__version__)"
                        '''
                    }
                }
            }
        }

        // --------------------------------------------------------
        // Stage 3: Run Unit Tests and Generate Coverage Report
        // --------------------------------------------------------
        stage('Unit Testing & Coverage') {
            steps {
                echo "Running pytest with coverage..."
                
                script {
                    if (isUnix()) {
                        sh '''
                            source ${PYTHON_ENV}/bin/activate
                            
                            # Create a reports directory if it doesn't exist
                            mkdir -p reports
                            
                            # Run pytest, output XML for Jenkins, and generate XML coverage report for SonarQube
                            pytest --cov=src tests/ --junitxml=reports/test-results.xml --cov-report=xml:reports/coverage.xml --cov-fail-under=90
                        '''
                    } else {
                        bat '''
                            call %PYTHON_ENV%\\Scripts\\activate.bat
                            
                            if not exist reports mkdir reports
                            
                            pytest --cov=src tests/ --junitxml=reports/test-results.xml --cov-report=xml:reports/coverage.xml --cov-fail-under=90
                        '''
                    }
                }
            }
            post {
                always {
                    // Archive the JUnit-style XML report so Jenkins can visualize it
                    junit 'reports/test-results.xml'
                }
            }
        }

        // --------------------------------------------------------
        // Stage 4: Static Code Analysis (SonarQube)
        // --------------------------------------------------------
        stage('SonarQube Analysis') {
            // Note: Ensure your SonarQube token is saved in Jenkins credentials as 'sonarqube-token'
            environment {
                SONAR_TOKEN = credentials('sonarqube-token') 
            }
            steps {
                echo "Running SonarScanner for Python..."
                
                script {
                    if (isUnix()) {
                        sh '''
                            source ${PYTHON_ENV}/bin/activate
                            pip install pysonar
                            
                            # Execute the scanner (it automatically reads sonar-project.properties)
                            pysonar -Dsonar.host.url=https://sonarcloud.io
                        '''
                    } else {
                        bat '''
                            call %PYTHON_ENV%\\Scripts\\activate.bat
                            pip install pysonar
                            
                            pysonar -Dsonar.host.url=https://sonarcloud.io
                        '''
                    }
                }
            }
        }

        // --------------------------------------------------------
        // Stage 5: Continuous Deployment
        // --------------------------------------------------------
        stage('Deploy') {
            steps {
                echo 'Packaging and Deploying to Production environment...'
                script {
                    if (isUnix()) {
                        sh '''
                            mkdir -p /tmp/Production_Server/CDV1C02_Web
                            cp -r src templates app.py requirements.txt Makefile /tmp/Production_Server/CDV1C02_Web/
                        '''
                    } else {
                        bat '''
                            if not exist "C:\\Production_Server\\CDV1C02_Web" mkdir "C:\\Production_Server\\CDV1C02_Web"
                            xcopy /E /Y /I src "C:\\Production_Server\\CDV1C02_Web\\src\\"
                            xcopy /E /Y /I templates "C:\\Production_Server\\CDV1C02_Web\\templates\\"
                            copy /Y app.py "C:\\Production_Server\\CDV1C02_Web\\"
                            copy /Y requirements.txt "C:\\Production_Server\\CDV1C02_Web\\"
                            copy /Y Makefile "C:\\Production_Server\\CDV1C02_Web\\"
                        '''
                    }
                }
                echo 'Deployment successful! Artifacts delivered to production directory.'
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