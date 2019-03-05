#!groovy

node {

    try {

        stage 'Deploy'
            sh 'sh /home/ducdh/app/CICD-Django/deployment/deploy_prod.sh'

    }

    catch (err) {
        slackSend color: "danger", message: "Build failed :face_with_head_bandage: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"

        throw err
    }

}