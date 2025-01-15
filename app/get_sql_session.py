from typing import Iterator
from sqlalchemy.orm import Session
from app.modassembly.database.sql.get_sql_session import SessionLocal

def get_sql_session() -> Iterator[Session]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
