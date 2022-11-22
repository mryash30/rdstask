
pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
         stage('RDS Stopping Job') { 
            steps { 
                script{
                    sh '/bin/python3 ./main.py'
                }
            }
        }
    }
}
