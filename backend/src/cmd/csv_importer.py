"""backend.csv_importer"""
import logging
import csv
import os
import typer

from ..database import engine, SessionLocal, models

DATA_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data'))

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

models.Base.metadata.create_all(bind=engine)


def import_csvs():
    db = SessionLocal()
    campaigns = []
    recipients = []
    with open(os.path.join(DATA_DIR, 'campaigns.csv')) as campaigns_file, \
            open(os.path.join(DATA_DIR, 'recipients.csv')) as recipients_file:

        logger.info('Reading "data/campaigns.csv"...')
        campaigns_csv = csv.DictReader(campaigns_file, delimiter=';')
        for line in campaigns_csv:
            campaigns.append(
                models.Campaign(
                    campaign_id=line['campaignId'],
                    article_no=line['articleNo'],
                    article_image_url=line['articleImageUrl'],
                    quantity=line['quantity'],
                    product_name=line['product_name'],
                    warehouse=line['warehouse'],
                )
            )

        logger.info('Reading "data/recipients.csv"...')
        recipients_csv = csv.DictReader(recipients_file, delimiter=';')
        for line in recipients_csv:
            recipients.append(
                models.Recipient(
                    order_number=line['orderNo'],
                    street=line['street'],
                    zip_code=line['zip_code'],
                    city=line['city'],
                    destination_country_iso3=line['destination_country_iso3'],
                    email=line['email'],
                    campaign_id=line['campaignId'],
                    order_status=line['orderStatus'],
                )
            )
    db.add_all(recipients)
    db.add_all(campaigns)
    db.commit()
    db.close()

    logger.info('Data successfully stored in database.')


if __name__ == "__main__":
    typer.run(import_csvs)
