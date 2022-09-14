"""lhb-backend.tests.test_recipients."""
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from .utils import create_recipient, create_campaign
from .fixtures import app, session, client


def test_get_all_recipients(
        app: FastAPI,
        session: Session,
        client: TestClient,
):
    for i in range(1, 4):
        create_recipient(session, i)
    response = client.get('/api/v1/orders/')
    assert response.status_code == 200
    recipients = response.json()
    assert len(recipients) == 3


def test_get_recipients_for_email(
        app: FastAPI,
        session: Session,
        client: TestClient,
):
    create_recipient(session)
    response = client.get('/api/v1/orders/?email=test@email.com')
    assert response.status_code == 200
    recipients = response.json()
    first_recipient = recipients[0]
    assert first_recipient['email'] == 'test@email.com'
    assert first_recipient['order_number'] == '0000'
    assert first_recipient['street'] == 'Strasse 1'
    assert first_recipient['zip_code'] == '12345'
    assert first_recipient['city'] == 'Berlin'
    assert first_recipient['destination_country_iso3'] == 'DEU'
    assert first_recipient['campaign_id'] == '12345678'
    assert first_recipient['order_status'] == 'Order processed'


def test_get_recipients_for_unknown_email(
        app: FastAPI,
        session: Session,
        client: TestClient,
):
    email_address = 'unknown@email.com'
    response = client.get('/api/v1/orders/?email=%s' % email_address)
    assert response.status_code == 404
    assert response.json() == {'detail': 'No orders found for email: %s' % email_address}  # noqa


def test_get_recipient_by_id(
        app: FastAPI,
        session: Session,
        client: TestClient,
):
    recipient = create_recipient(session)
    create_campaign(session)
    response = client.get(f'/api/v1/orders/{recipient.id}')
    assert response.status_code == 200
    recipient = response.json()
    assert recipient['order_number'] == '0000'
    assert recipient['email'] == 'test@email.com'
    assert recipient['street'] == 'Strasse 1'
    assert recipient['zip_code'] == '12345'
    assert recipient['city'] == 'Berlin'
    assert recipient['destination_country_iso3'] == 'DEU'
    assert recipient['campaign_id'] == '12345678'
    assert recipient['order_status'] == 'Order processed'
    campaign_articles = recipient['campaign_articles']
    assert len(campaign_articles) > 0
    first_article = campaign_articles[0]
    assert first_article['campaign_id'] == '12345678'
    assert first_article['article_no'] == 'A-B1-C'
    assert first_article['article_image_url'] == 'https://cdn.com/image.png'
    assert first_article['quantity'] == 1
    assert first_article['product_name'] == 'T-shirt'
    assert first_article['warehouse'] == 'Munich'


def test_get_recipient_for_unknown_id(
        app: FastAPI,
        session: Session,
        client: TestClient,
):
    recipient_id = 2
    response = client.get('/api/v1/orders/%i' % recipient_id)
    assert response.status_code == 404
    assert response.json() == {'detail': 'No order found with id: %s' % recipient_id}  # noqa
