pipeline {
    agent any
    stages {
        stage('build') {
            steps{
                sh 'python3 setup.py build'
            }
        }
        stage('test'){
            steps{
                sh 'python3 -m pytest tests/ --junitxml=tests-$BUILD_NUMBER.xml'
            }
        }
        stage('deploy'){
            steps{
                sshPublisher(publishers: [sshPublisherDesc(configName: 'webserver', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: '', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'build/lib/pypineapple/**/*')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
                sshPublisher(publishers: [sshPublisherDesc(configName: 'webserver', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: '', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'setup.py')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
                sshPublisher(publishers: [sshPublisherDesc(configName: 'webserver', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: '', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'exampleConfigs/*')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
                sshPublisher(publishers: [sshPublisherDesc(configName: 'webserver', transfers: [sshTransfer(
                    execCommand: 'sudo /bin/bash /home/jenkins/exampleConfigs/deployPineapple.sh', execTimeout: 120000, usePty: true)])])
            }    
        }
    } 
    post {
        always {
            archiveArtifacts artifacts: 'build/lib/**/*'
            junit 'tests-$BUILD_NUMBER.xml'
        }
    }
}
