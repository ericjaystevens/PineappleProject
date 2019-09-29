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
                sh 'python3 -m pytest tests/ --verbose'
            }
        }
        stage('deploy'){
            steps{
                sshPublisher(publishers: [sshPublisherDesc(configName: 'webserver', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: '', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'PineappleProject/build/lib/pypineapple/**/*')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
            }    
        }
    }
}