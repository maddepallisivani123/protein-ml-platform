# 🚀 Cloud-Native Distributed ML Training Platform

A production-style Machine Learning Platform that demonstrates:

- ✅ Distributed ETL Pipeline
- ✅ PostgreSQL Data Layer
- ✅ Containerized ML Training Jobs
- ✅ Model Artifact Management
- ✅ FastAPI Inference Service
- ✅ Docker + Kubernetes Deployment
- ✅ CI/CD with GitHub Actions
- ✅ Reproducible ML Workflows

This project simulates how modern ML infrastructure teams build scalable training and serving systems in cloud environments (AWS ECS / Kubernetes).

---

# 🏗 Architecture Overview

```
        Raw Data (CSV / S3)
                ↓
        ETL Service (Docker Container)
                ↓
        PostgreSQL (Relational Store)
                ↓
        Training Job (Containerized)
                ↓
        Model Artifact (.joblib)
                ↓
        FastAPI Inference API
```

Infrastructure:
- Docker
- Docker Compose
- Kubernetes (Jobs + Deployments)
- PostgreSQL
- GitHub Actions CI

---

# 🧠 What This Project Demonstrates

### 1️⃣ Distributed ETL Pipeline
- Schema validation
- Data cleaning
- Relational data ingestion
- Idempotent loading into PostgreSQL
- Modular containerized execution

### 2️⃣ Reproducible Model Training
- Config-driven ML pipeline
- Train/test split with stratification
- AUC evaluation
- Model artifact versioning
- Saved model stored in shared volume

### 3️⃣ Inference API
- FastAPI service
- Loads trained artifact dynamically
- Health endpoint
- Model metadata endpoint
- Prediction endpoint

### 4️⃣ Cloud-Ready Deployment
- Dockerized microservices
- Kubernetes Job for ETL
- Kubernetes Job for Training
- Deployment + Service for Inference API
- CI pipeline builds containers automatically

---

# 🛠 Tech Stack

| Layer | Technology |
|--------|------------|
| Language | Python 3.11 |
| ML | scikit-learn |
| Database | PostgreSQL |
| API | FastAPI |
| Containers | Docker |
| Orchestration | Kubernetes |
| CI/CD | GitHub Actions |
| ORM | SQLAlchemy |

---

# ⚙️ Local Setup (Docker Compose)

## 1️⃣ Clone Repo

```bash
git clone https://github.com/YOUR_USERNAME/ml-platform.git
cd ml-platform
```

## 2️⃣ Setup Environment

```bash
cp .env.example .env
```

## 3️⃣ Start Services

```bash
docker compose up --build -d postgres api
```

## 4️⃣ Run ETL Job

```bash
docker compose run --rm etl
```

## 5️⃣ Run Training Job

```bash
docker compose run --rm training
```

## 6️⃣ Test API

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"age":35,"income":70000,"tenure_months":18,"score":0.82}'
```

---

# ☸️ Kubernetes Deployment (Optional Advanced)

Apply namespace:

```bash
kubectl apply -f k8s/namespace.yaml
```

Deploy PostgreSQL:

```bash
kubectl apply -f k8s/postgres.yaml
```

Run ETL job:

```bash
kubectl apply -f k8s/etl-job.yaml
```

Run Training job:

```bash
kubectl apply -f k8s/training-job.yaml
```

Deploy API:

```bash
kubectl apply -f k8s/api.yaml
```

---

# 📦 CI/CD Pipeline

GitHub Actions automatically:
- Lints Python code
- Builds Docker images
- Validates container builds

This mirrors production ML platform workflows.

---

# 🔍 Why This Project Matters

Modern ML teams need more than notebooks.  
They need:

- Structured data pipelines
- Reproducible training jobs
- Containerized execution
- Distributed compute readiness
- Deployment automation
- Observability-ready services

This project demonstrates those core infrastructure patterns.

---

# 🚀 Future Enhancements

- Add MLflow experiment tracking
- Add Prometheus + Grafana monitoring
- Integrate S3 for artifact storage
- Use Terraform for AWS provisioning
- Add horizontal autoscaling

---

# 👤 Author

Sivani Maddepalli  
Machine Learning Engineer | ML Infrastructure | Cloud-Native Systems  

---

# 📄 License

MIT License
