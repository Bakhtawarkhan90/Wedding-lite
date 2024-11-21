pipeline {
    agent any
    environment {
        SONAR_HOME = tool "Sonar"
        GITHUB_TOKEN = credentials('GithubToken')  // Use a Jenkins credential for GitHub PAT
        GITHUB_USERNAME = 'Bakhtawarkhan90'   // Replace with your GitHub username

    }
    stages {
        stage('Code Clone') {
            steps {
                git url: 'https://github.com/Bakhtawarkhan90/Wedding-lite.git', branch: 'main'

            }
        }

        stage('Code Quality Analysis') {
            steps {
                withSonarQubeEnv("Sonar") {
                    sh "$SONAR_HOME/bin/sonar-scanner -Dsonar.projectName=Weddding -Dsonar.projectKey=Wedding -X"
                }
            }
        }

        stage('Building Image With Docker') {
            steps {
                sh "docker build . -t wedding:latest"
            }
        }

        stage('Trivy Image Scanning') {
            steps {
                sh "trivy image wedding:latest"
            }
        }

        stage('Push To Docker-Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: "dockerHub", passwordVariable: "dockerHubPass", usernameVariable: "dockerHubUser")]) {
                    sh "echo \$dockerHubPass | docker login -u \$dockerHubUser --password-stdin"
                    sh "docker tag wedding:latest ${env.dockerHubUser}/wedding:latest"
                    sh "docker push ${env.dockerHubUser}/wedding:latest"
                }
            }
        }

        stage('OWASP DC') {
            steps {
                  dependencyCheck additionalArguments: '--scan .', odcInstallation: 'OWASP'
                  dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }


        stage('Deploy On K8s') {
            steps {
               sh " cd /var/lib/jenkins/workspace/Barista_cafe/k8s "
               sh " kubectl apply -f . "
               sh " kubectl port-forward svc/cafe 5000:5000 --address 0.0.0.0 & "
            }
        }
    }
}
