"""lhb-backend.src.models.campaign."""
from sqlalchemy import Column, Integer, String

from ..database.session import Base


class Campaign(Base):  # type: ignore
    """SQLAlchemy data model class for campaigns to interact with DB."""

    __tablename__ = 'campaigns'

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(String, index=True)
    article_no = Column(String)
    article_image_url = Column(String)
    quantity = Column(Integer)
    product_name = Column(String)
    warehouse = Column(String)
