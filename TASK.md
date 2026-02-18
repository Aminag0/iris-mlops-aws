# Activity Task: MLOps with Docker Compose

## Objective

Deploy a Machine Learning model using Docker Compose with Redis caching.

---

## Tasks

### Task 1: Train the Model
Run:
    python train.py

This should generate:
    model.pkl

---

### Task 2: Build and Run Containers
Use Docker Compose:

    docker compose up --build

---

### Task 3: Test the API
Send a POST request:

    curl -X POST http://localhost:5000/predict \
    -H "Content-Type: application/json" \
    -d "{\"features":[5.1,3.5,1.4,0.2]}"

---

### Task 4: Verify Caching

Call the API twice with the same input.

First response:
    "cached": false

Second response:
    "cached": true

---

## Reflection Questions

1. Why do we use Docker Compose instead of Docker only?
2. What role does Redis play?
3. What happens if Redis container stops?
4. How would this architecture scale in production?

---

## Submission

Submit:
- Screenshot of running containers
- Screenshot of API response
- Short explanation (5–6 lines) of the architecture
