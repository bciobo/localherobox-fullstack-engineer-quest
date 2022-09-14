"""lhb-backend.src.models.recipient."""
from sqlalchemy import Column, Integer, String
from ..database import Base


class Recipient(Base):  # type: ignore
    """SQLAlchemy data model class for recipients to interact with DB."""

    __tablename__ = 'recipients'

    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String)
    street = Column(String)
    zip_code = Column(String)
    city = Column(String)
    destination_country_iso3 = Column(String)
    email = Column(String, index=True)
    campaign_id = Column(String)
    order_status = Column(String)
