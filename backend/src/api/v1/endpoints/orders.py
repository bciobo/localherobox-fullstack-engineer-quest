import typing as t

from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.src.api.dependencies import get_db
from backend.src.crud.recipient import get_recipients_by_email, get_recipients, get_recipient_by_id
from backend.src.crud.article import get_articles_by_campaign_id
from backend.src.schemas.recipient import Recipient, RecipientWithCampaigns
from backend.src.schemas.campaign import Campaign

router = APIRouter()


@router.get("/", response_model=t.List[Recipient])
async def orders(email: str | None = None,
                 db: Session = Depends(get_db)) -> t.Any:
    if email:
        return get_recipients_by_email(db, email=email)
    return get_recipients(db)


@router.get("/{order_id}", response_model=RecipientWithCampaigns)
async def order_detail(order_id: int,
                       db: Session = Depends(get_db)) -> t.Any:
    recipient = RecipientWithCampaigns.from_orm(get_recipient_by_id(db, order_id))
    articles = [Campaign.from_orm(a) for a in get_articles_by_campaign_id(db, recipient.campaign_id)]
    recipient.campaign_articles = articles
    return recipient
