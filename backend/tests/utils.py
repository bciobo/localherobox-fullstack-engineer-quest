from sqlalchemy.orm import Session
from ..src.models.recipient import Recipient


def create_recipient(db: Session, i=''):
    db_obj = Recipient(
        order_number=f'0000{i}',
        email=f'test@email.com{i}',
        street=f'Strasse 1{i}',
        zip_code='12345',
        city='Berlin',
        destination_country_iso3='DEU',
        campaign_id=f'12345678{i}',
        order_status='Order processed',
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
