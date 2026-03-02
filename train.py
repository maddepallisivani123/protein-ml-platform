import os
import pandas as pd
from sqlalchemy import text
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import joblib
from shared.db import get_engine

TABLE = "training_data"
MODEL_PATH = os.environ.get("MODEL_PATH", "/artifacts/model.joblib")

def main():
    engine = get_engine()

    with engine.begin() as conn:
        # Ensure table exists
        conn.execute(text(f"SELECT 1 FROM information_schema.tables WHERE table_name='{TABLE}'"))
    df = pd.read_sql(f"SELECT age, income, tenure_months, score, label FROM {TABLE}", engine)

    if df.empty:
        raise RuntimeError("No training data found. Run ETL first.")

    X = df[["age", "income", "tenure_months", "score"]]
    y = df["label"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000))
    ])

    pipeline.fit(X_train, y_train)
    probs = pipeline.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, probs)

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump({"model": pipeline, "auc": auc}, MODEL_PATH)

    print(f"Training complete. AUC={auc:.4f}. Saved model to {MODEL_PATH}")

if __name__ == "__main__":
    main()
