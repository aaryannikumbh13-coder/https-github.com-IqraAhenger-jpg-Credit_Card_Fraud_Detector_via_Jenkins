# Credit Card Fraud Detector via Jenkins

This is a complete Machine Learning + DevOps project that predicts whether a credit card transaction is legitimate or fraudulent.

## Features
- Fraud prediction using Logistic Regression
- Clean Flask frontend UI
- Trained model and scaler included
- Dockerized deployment on port 5001
- Jenkins pipeline for CI/CD
- GitHub-ready project structure

## Project Structure
```text
Credit_Card_Fraud_Detector_viaJenkins/
├── app.py
├── train_model.py
├── requirements.txt
├── Jenkinsfile
├── Dockerfile
├── docker-compose.yml
├── README.md
├── VIVA_QA.md
├── model.pkl
├── scaler.pkl
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── data/
    └── creditcard.csv
```

## Run Locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python train_model.py
python app.py
```

Open in browser:
```bash
http://localhost:5001
```

## Run with Docker
```bash
docker build -t credit-card-fraud-detector .
docker run -p 5001:5001 credit-card-fraud-detector
```

## Run with Docker Compose
```bash
docker-compose up --build
```

## Jenkins Pipeline Flow
1. Checkout code from GitHub
2. Create Python virtual environment
3. Install requirements
4. Train model
5. Build Docker image
6. Deploy app container on port 5001

## Notes
- The app expects 30 numeric input features.
- `model.pkl` and `scaler.pkl` are already included for demo use.
- The included dataset is a small demo dataset created for project packaging and testing.
