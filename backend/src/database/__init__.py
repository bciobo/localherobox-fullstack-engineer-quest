"""lhb-backend.src.database."""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'example')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'lhb')

SQLALCHEMY_DATABASE_URL = 'postgresql://{}:{}@localhost:5432/{}'.format(
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
