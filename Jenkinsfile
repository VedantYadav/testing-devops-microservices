// node {
// 	stage('Build') {
// 		echo "Build"
// 	}
// 	stage('Test') {
// 		echo "Test"
// 	}

// 	stage('Ingration test'){
// 		echo "Intergration Test"
// 	}

// }

pipeline {
	// agent any
	agent { docker { image 'python:alpine' } }
	stages {
		stage('Build') {
			steps {
				echo "Build"
				sh 'python --version'
			}
		}

		stage('Stage') {
			steps {
				echo "Stage"
			}
		}

		stage('Test') {
			steps {
				echo "test"
			}
		}
	} 
	post {
		always {
			echo "Do something"
		}
		success {
			echo "Success something"
		}
		failure {
			echo "Failure something"
		}

		// changed -> when status changed so added message to slack 
	}
}