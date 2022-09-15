"""lhb-backend.src.crud.recipient."""
import typing as t
from sqlalchemy.orm import Session
from ..models.recipient import Recipient


def get_recipients(db: Session) -> t.List[Recipient]:
    """Get all recipients."""
    return db.query(Recipient).all()  # type: ignore


def get_recipients_by_email(db: Session, email: str) -> t.List[Recipient]:
    """Get all recipients filtering by email."""
    return db.query(Recipient).filter(Recipient.email == email).all()  # type: ignore


def get_recipient_by_id(db: Session, recipient_id: int) -> Recipient:
    """Get all recipients filtering by id."""
    return db.query(Recipient).filter(Recipient.id == recipient_id).first()  # type: ignore
