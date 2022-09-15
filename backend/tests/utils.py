import typing as t
from sqlalchemy.orm import Session
from ..src.models.recipient import Recipient
from ..src.models.campaign import Campaign


def create_db_obj(db: Session, db_obj: t.Union[Recipient, Campaign]):
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_recipient(db: Session, i=''):
    db_obj = Recipient(
        order_number=f'0000{i}',
        email='test@email.com',
        street='Strasse 1',
        zip_code='12345',
        city='Berlin',
        destination_country_iso3='DEU',
        campaign_id=f'12345678{i}',
        order_status='Order processed',
    )
    return create_db_obj(db, db_obj)


def create_campaign(db: Session, campaign_id='12345678', i=''):
    db_obj = Campaign(
        campaign_id=campaign_id,
        article_no=f'A-B1-C{i}',
        article_image_url='https://cdn.com/image.png',
        quantity=1,
        product_name='T-shirt',
        warehouse='Munich',
    )
    return create_db_obj(db, db_obj)
