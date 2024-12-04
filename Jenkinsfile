pipeline {
    agent any

    environment {
        REPOSITORY_URL = 'https://github.com/o-laureano/Trabalho_DevOps_2395176.git'
        BRANCH_NAME = 'main'
    }

    stages {
        stage('Baixar código do Git') {
            steps {
                echo 'Clonando o repositório do Git...'
                git branch: "${BRANCH_NAME}", url: "${REPOSITORY_URL}"
            }
        }

        stage('Build e Deploy') {
            steps {
                script {
                    echo 'Iniciando o build e deploy dos serviços...'
                    sh '''
                        docker-compose build
                        docker-compose up -d
                    '''
                }
            }
        }

        stage('Rodar Testes') {
            steps {
                script {
                    echo 'Aguardando os serviços estarem prontos...'
                    sh '''
                        while ! docker ps | grep -q "trabalho-mariadb"; do
                            echo "Esperando os serviços iniciarem..."
                            sleep 5
                        done
                    '''
                    echo 'Executando os testes...'
                    sh 'docker-compose run --rm test'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executada com sucesso!'
        }
        failure {
            echo 'A pipeline falhou.'
        }
        always {
            echo 'Limpando contêineres...'
            sh 'docker-compose down'
        }
    }
}
