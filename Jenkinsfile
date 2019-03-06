#!groovy

node {

    try {

        stage 'Checkout'
            checkout scm

            slackSend color: "warning", message: "Started `${env.JOB_NAME}#${env.BUILD_NUMBER}`\n\n_The changes:_\n"

        stage 'Deploy'
            sh 'sh /home/ducdh/app/CICD-Django/deployment/deploy_prod.sh'

        stage 'Publish results'
            slackSend color: "good", message: "Build successful: `${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"

    }

    catch (err) {
        slackSend color: "danger", message: "Build failed :face_with_head_bandage: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"

        throw err
    } finally {
        // Post build steps here
        /* Success or failure, always run post build steps */
        // send email
        // publish test results etc etc
    }

}