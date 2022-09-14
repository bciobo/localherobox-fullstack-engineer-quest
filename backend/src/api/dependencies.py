import typing as t
from sqlalchemy.orm import Session

from ..database.session import SessionLocal


def get_db() -> t.Generator[Session, t.Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
