from sqlalchemy import Column, Integer, String, text
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class Campaign(Base):
    """SQLAlchemy data model class for campaigns to interact with DB"""
    __tablename__ = 'campaigns'

    id = Column(UUID(as_uuid=True), server_default=text("gen_random_uuid()"), primary_key=True)
    campaign_id = Column(String, index=True)
    article_no = Column(String)
    article_image_url = Column(String)
    quantity = Column(Integer)
    product_name = Column(String)
    warehouse = Column(String)


class Recipient(Base):
    """SQLAlchemy data model class for recipients to interact with DB

    When accessing the attribute "campaign" in a Recipient, it will contain a Campaign
    SQLAlchemy model from the campaigns table. It will use the campaign_id attribute/column
    with its foreign key to know which record to get from the campaigns table.
    """
    __tablename__ = 'recipients'

    id = Column(UUID(as_uuid=True), server_default=text("gen_random_uuid()"), primary_key=True)
    order_number = Column(String)
    street = Column(String)
    zip_code = Column(String)
    city = Column(String)
    destination_country_iso3 = Column(String)
    email = Column(String, index=True)
    campaign_id = Column(String)
    order_status = Column(String)
