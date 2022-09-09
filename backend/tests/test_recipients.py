"""lhb-backend.tests.test_recipients."""

from fastapi.testclient import TestClient

from backend.src.main import app

client = TestClient(app)


def test_get_all_orders(): # noqa
    response = client.get('/orders/')
    assert response.status_code == 200
    orders = response.json()
    assert len(orders) > 0


def test_get_orders_for_email(): # noqa
    response = client.get('/orders/?email=test@email.com')
    assert response.status_code == 200
    orders = response.json()
    first_order = orders[0]
    assert first_order['email'] == 'test@email.com'
    assert first_order['order_number'] == '1111'
    assert first_order['street'] == 'Strasse 1'
    assert first_order['zip_code'] == '12345'
    assert first_order['city'] == 'Berlin'
    assert first_order['destination_country_iso3'] == 'DEU'
    assert first_order['campaign_id'] == '12345678'
    assert first_order['order_status'] == 'Order processed'


def test_get_orders_for_unknown_email(): # noqa
    email_address = 'unknown@email.com'
    response = client.get('/orders/?email=%s' % email_address)
    assert response.status_code == 404
    assert response.json() == {'message': 'No orders found for email: %s' % email_address} # noqa


def test_get_order_by_id(): # noqa
    response = client.get('/orders/1234')
    assert response.status_code == 200
    order = response.json()
    assert order['order_number'] == '1234'
    assert order['email'] == 'test@email.com'
    assert order['street'] == 'Strasse 1'
    assert order['zip_code'] == '12345'
    assert order['city'] == 'Berlin'
    assert order['destination_country_iso3'] == 'DEU'
    assert order['campaign_id'] == '12345678'
    assert order['order_status'] == 'Order processed'
    articles = order['articles']
    assert len(articles) > 0
    first_article = articles[0]
    assert first_article['campaign_id'] == '12345678'
    assert first_article['article_no'] == 'A-B2-U'
    assert first_article['article_image_url'] == 'https://cdn.com/image.png'
    assert first_article['quantity'] == 1
    assert first_article['product_name'] == 'T-shirt'
    assert first_article['warehouse'] == 'Munich'



def test_get_order_for_unknown_id(): # noqa
    order_number = 9999
    response = client.get('/orders/%i' % order_number)
    assert response.status_code == 404
    assert response.json() == {'message': 'No order found with number: #%i' % order_number} # noqa
