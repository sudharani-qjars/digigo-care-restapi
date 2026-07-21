pipeline {
    agent any

    environment {
        // Defines where the UI automation repo will be temporarily stored
        UI_REPO_DIR = "${WORKSPACE}\\digigo-care-ui-automation"
    }

    stages {
        stage('Checkout API Repo') {
            steps {
                // Pulls the current API repository branch automatically
                checkout scm
            }
        }

        stage('Install API Dependencies') {
            steps {
                bat """
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Job 1: API Tests') {
            steps {
                bat "pytest -v --html=api_report.html --self-contained-html"
            }
        }

        stage('Checkout & Run Job 2: UI Tests') {
            steps {
                echo 'Checking out the second repository...'

                // Natively pulls your UI automation repository into its own workspace folder
                dir("${UI_REPO_DIR}") {
                    checkout([$class: 'GitSCM',
                        branches: [[name: '*/main']],
                        userRemoteConfigs: [[
                            url: 'https://github.com/sudharani-qjars/digigo-care-ui-automation.git',
                            credentialsId: 'ddc57b5a-bc0e-4dc1-a316-1e039735b4d0' // Replace with your Jenkins Git Credential ID if private
                        ]]
                    ])

                    bat """
                        echo Installing UI test packages...
                        python -m pip install --upgrade pip
                        pip install -r requirements.txt

                        echo Executing UI Automation Suite...
                        pytest -v --html=ui_report.html --self-contained-html
                    """
                }
            }
        }
    }

        post {
        always {
            // Publishes the API test report using correct pipeline syntax
            publishHTML([
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'api_report.html',
                reportName: 'Pytest API Report',
                reportTitles: 'API Test Results'
            ])

            // Publishes the UI test report using correct pipeline syntax
            publishHTML([
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'digigo-care-ui-automation',
                reportFiles: 'ui_report.html',
                reportName: 'Pytest UI Report',
                reportTitles: 'UI Test Results'
            ])
        }
    }

}
