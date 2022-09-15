import typing as t

from fastapi import Depends
from fastapi import APIRouter
from fastapi import HTTPException
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
        recipients = get_recipients_by_email(db, email=email)
        if not recipients:
            raise HTTPException(status_code=404, detail=f'No orders found for email: {email}')
        return recipients

    return get_recipients(db)


@router.get("/{order_id}", response_model=RecipientWithCampaigns)
async def order_detail(order_id: int,
                       db: Session = Depends(get_db)) -> t.Any:
    recipient_model = get_recipient_by_id(db, order_id)
    if not recipient_model:
        raise HTTPException(status_code=404, detail=f'No order found with id: {order_id}')
    recipient = RecipientWithCampaigns.from_orm(get_recipient_by_id(db, order_id))
    articles = [Campaign.from_orm(a) for a in get_articles_by_campaign_id(db, recipient.campaign_id)]
    recipient.campaign_articles = articles
    return recipient
