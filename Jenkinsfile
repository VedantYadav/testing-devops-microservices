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
	agent any
	stages {
		stage('Build') {
			steps {
				echo "Build"
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
	}
}