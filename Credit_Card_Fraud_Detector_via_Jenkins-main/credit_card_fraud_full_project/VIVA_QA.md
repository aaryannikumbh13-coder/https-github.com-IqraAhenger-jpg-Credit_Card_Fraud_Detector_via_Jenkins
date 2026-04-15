# Viva Questions and Answers

## 1. What is the aim of this project?
This project aims to detect fraudulent credit card transactions using machine learning and automate deployment using Jenkins.

## 2. Which algorithm is used in this project?
Logistic Regression is used for binary classification of transactions into legitimate and fraudulent classes.

## 3. Why is fraud detection important?
It helps prevent financial loss and improves security in digital payment systems.

## 4. What is the target column in the dataset?
The target column is `Class`, where `0` means legitimate and `1` means fraud.

## 5. Why is feature scaling used?
Feature scaling standardizes the input values and improves model training performance.

## 6. What is Flask used for?
Flask is used to build the web interface for entering transaction data and showing predictions.

## 7. What is Jenkins used for?
Jenkins automates code checkout, dependency installation, training, Docker build, and deployment.

## 8. What is Docker used for?
Docker packages the project with all dependencies so it runs consistently across systems.

## 9. What is CI/CD?
CI/CD means Continuous Integration and Continuous Deployment, where code changes are automatically built and deployed.

## 10. What are `model.pkl` and `scaler.pkl`?
`model.pkl` stores the trained ML model and `scaler.pkl` stores the fitted StandardScaler.

## 11. Why is the dataset often imbalanced in fraud detection?
Fraud cases are much fewer than normal transactions, so the classes are uneven.

## 12. What port does this app use?
The app uses port `5001`.

## 13. What happens in the Jenkins pipeline?
It checks out code, creates the environment, installs dependencies, trains the model, builds the Docker image, and deploys the container.

## 14. What technologies are used in this project?
Python, Flask, Scikit-learn, Docker, Jenkins, GitHub, HTML, and CSS.

## 15. What is the advantage of combining ML and DevOps?
It makes the solution practical by automating training, packaging, deployment, and delivery.
