# MLOps Docker Compose Activity – Iris ML Model Deployment

This repository contains a hands-on MLOps lab activity for BS students demonstrating:

- ML model training
- Containerization using Docker
- Multi-container orchestration using Docker Compose
- Redis caching integration
- REST API model serving

## Setup Instructions

1. Train Model:
   python train.py

2. Run Docker Compose:
   docker compose up --build

3. Test API:
   curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"features\":[5.1,3.5,1.4,0.2]}"

Expected:
First call → cached: false
Second call → cached: true
