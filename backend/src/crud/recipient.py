"""lhb-backend.src.crud.recipient."""
import typing as t
from sqlalchemy.orm import Session
from ..models import Recipient


def get_recipients(db: Session) -> t.List[Recipient]:
    return db.query(Recipient).all()


def get_recipients_by_email(db: Session, email: str) -> t.List[Recipient]:
    return db.query(Recipient).filter(Recipient.email == email).all()


def get_recipient_by_id(db: Session, recipient_id: int) -> Recipient:
    return db.query(Recipient).filter(Recipient.id == recipient_id).first()
