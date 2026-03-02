import pandas as pd
from sqlalchemy import text
from shared.db import get_engine

RAW_PATH = "/data/raw.csv"
TABLE = "training_data"

def main():
    engine = get_engine()

    df = pd.read_csv(RAW_PATH)

    required = {"age", "income", "tenure_months", "score", "label"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Basic validation
    df = df.dropna()
    df["label"] = df["label"].astype(int)

    with engine.begin() as conn:
        conn.execute(text(f"""
            CREATE TABLE IF NOT EXISTS {TABLE} (
                id SERIAL PRIMARY KEY,
                age INT NOT NULL,
                income INT NOT NULL,
                tenure_months INT NOT NULL,
                score FLOAT NOT NULL,
                label INT NOT NULL
            );
        """))

    # Load (append)
    df[["age", "income", "tenure_months", "score", "label"]].to_sql(
        TABLE, engine, if_exists="append", index=False
    )

    print(f"ETL complete. Loaded {len(df)} rows into {TABLE}.")

if __name__ == "__main__":
    main()
