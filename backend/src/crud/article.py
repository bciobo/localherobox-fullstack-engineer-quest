"""lhb-backend.src.crud.article."""
import typing as t
from sqlalchemy.orm import Session
from ..models.campaign import Campaign


def get_articles_by_campaign_id(db: Session, campaign_id: str) -> t.List[Campaign]:
    """Get all articles filtering by campaign id."""
    return db.query(Campaign).filter(Campaign.campaign_id == campaign_id).all()  # type: ignore
