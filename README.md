# Cloud-Native ML Platform (ETL → Train → Serve)

A minimal ML platform that demonstrates:
- ETL pipeline loading raw data into PostgreSQL
- Training job reading from PostgreSQL and producing model artifacts
- FastAPI inference service serving predictions
- Docker Compose for local runs
- Kubernetes manifests (Jobs + Deployments)
- GitHub Actions CI (lint + docker build)

## Quickstart (Docker Compose)
1) Copy env:
```bash
cp .env.example .env
docker compose up --build -d postgres api
docker compose run --rm etl
docker compose run --rm training
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"age": 35, "income": 70000, "tenure_months": 18, "score": 0.82}'
