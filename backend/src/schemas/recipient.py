"""lhb-backend.src.schemas.recipient."""
import typing as t
from pydantic import BaseModel, Field
from .campaign import Campaign


class RecipientBase(BaseModel):
    order_number: str
    street: str
    zip_code: str
    city: str
    destination_country_iso3: str
    email: str
    campaign_id: str
    order_status: str


class RecipientInDb(RecipientBase):
    id: int

    class Config:
        orm_mode = True


class Recipient(RecipientInDb):
    pass


class RecipientWithCampaigns(Recipient):
    campaign_articles: t.List[Campaign] = Field(default_factory=list)
