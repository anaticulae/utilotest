pipeline {
    agent {
        docker {
            image '169.254.149.20:6001/arch_python_baw:0.14.0'
            args '-v $WORKSPACE:/var/workdir'
        }
    }

    parameters {
        string(name: 'BRANCH', defaultValue: 'master')
        booleanParam(name: 'RELEASE', defaultValue: false)
    }

    stages{
        stage('sync'){
            steps{
                sh 'ls -al /tmp'
                sh 'baw sync all'
            }
        }
        stage('doctest'){
            steps{
                sh 'baw test docs -n1'
            }
        }
        stage('fast'){
            steps{
                sh 'baw test fast -n5'
            }
        }
        stage('all'){
            steps{
                sh 'baw test all -n8  --cov --junit_xml=report.xml'
                junit '**/report.xml'
            }
        }
        stage('lint'){
            steps{
                sh 'baw lint'
            }
        }
        stage('release'){
            when {
                expression { return params.RELEASE }
            }
            steps{
                sh 'baw install && baw release && baw publish'
                // TODO: GIT COMMIT?
            }
        }
    }
}
