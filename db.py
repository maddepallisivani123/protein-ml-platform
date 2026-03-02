import os
from dataclasses import dataclass
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

@dataclass(frozen=True)
class DbConfig:
    host: str
    port: int
    db: str
    user: str
    password: str

    @staticmethod
    def from_env() -> "DbConfig":
        return DbConfig(
            host=os.environ.get("POSTGRES_HOST", "localhost"),
            port=int(os.environ.get("POSTGRES_PORT", "5432")),
            db=os.environ.get("POSTGRES_DB", "ml_platform"),
            user=os.environ.get("POSTGRES_USER", "ml_user"),
            password=os.environ.get("POSTGRES_PASSWORD", "ml_pass"),
        )

    def url(self) -> str:
        return f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"

def get_engine() -> Engine:
    cfg = DbConfig.from_env()
    return create_engine(cfg.url(), pool_pre_ping=True)
