"""lhb-backend.tests.test_recipients."""
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from ..src.main import app
from ..src.database import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_get_all_recipients():  # noqa
    response = client.get('/recipients/')
    assert response.status_code == 200
    recipients = response.json()
    assert len(recipients) > 0


def test_get_recipients_for_email():  # noqa
    response = client.get('/recipients/?email=test@email.com')
    assert response.status_code == 200
    recipients = response.json()
    first_recipient = recipients[0]
    assert first_recipient['email'] == 'test@email.com'
    assert first_recipient['order_number'] == '1111'
    assert first_recipient['street'] == 'Strasse 1'
    assert first_recipient['zip_code'] == '12345'
    assert first_recipient['city'] == 'Berlin'
    assert first_recipient['destination_country_iso3'] == 'DEU'
    assert first_recipient['campaign_id'] == '12345678'
    assert first_recipient['order_status'] == 'Order processed'


def test_get_recipients_for_unknown_email():  # noqa
    email_address = 'unknown@email.com'
    response = client.get('/recipients/?email=%s' % email_address)
    assert response.status_code == 404
    assert response.json() == {'message': 'No recipients found for email: %s' % email_address}  # noqa


def test_get_recipient_by_id():  # noqa
    response = client.get('/recipients/1234')
    assert response.status_code == 200
    recipient = response.json()
    assert recipient['order_number'] == '1234'
    assert recipient['email'] == 'test@email.com'
    assert recipient['street'] == 'Strasse 1'
    assert recipient['zip_code'] == '12345'
    assert recipient['city'] == 'Berlin'
    assert recipient['destination_country_iso3'] == 'DEU'
    assert recipient['campaign_id'] == '12345678'
    assert recipient['order_status'] == 'Order processed'
    articles = recipient['articles']
    assert len(articles) > 0
    first_article = articles[0]
    assert first_article['campaign_id'] == '12345678'
    assert first_article['article_no'] == 'A-B2-U'
    assert first_article['article_image_url'] == 'https://cdn.com/image.png'
    assert first_article['quantity'] == 1
    assert first_article['product_name'] == 'T-shirt'
    assert first_article['warehouse'] == 'Munich'


def test_get_recipient_for_unknown_id():  # noqa
    recipient_id = 9999
    response = client.get('/recipients/%i' % recipient_id)
    assert response.status_code == 404
    assert response.json() == {'message': 'No recipient found with number: #%i' % recipient_id}  # noqa
