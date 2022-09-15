"""lhb-backend.src.schemas.campaign."""
from pydantic import BaseModel


class CampaignBase(BaseModel):
    campaign_id: str
    article_no: str
    article_image_url: str
    quantity: int
    product_name: str
    warehouse: str


class CampaignInDb(CampaignBase):
    id: int

    class Config:
        orm_mode = True


class Campaign(CampaignInDb):
    pass
