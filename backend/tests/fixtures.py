import typing as t

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from ..src.main import init_app
from ..src.database.session import Base
from ..src.api.dependencies import get_db
from .config import engine, TestingSessionLocal


@pytest.fixture
def app() -> t.Generator[FastAPI, t.Any, None]:
    """Create a new database for each test case."""
    Base.metadata.create_all(engine)  # Create the tables.
    _app = init_app()
    yield _app
    Base.metadata.drop_all(engine)


@pytest.fixture
def session(app: FastAPI) -> t.Generator[Session, t.Any, None]:
    """Create FastAPI app fixture.

    Creates a fresh sqlalchemy session for each test that operates in a
    transaction. The transaction is rolled back at the end of each test ensuring
    a clean state.
    """
    connection = engine.connect()
    # begin a non-ORM transaction
    transaction = connection.begin()
    # bind an individual Session to the connection
    session = TestingSessionLocal(bind=connection)
    yield session  # use the session in tests.
    session.close()
    # rollback - everything that happened with the
    # Session above (including calls to commit())
    # is rolled back.
    transaction.rollback()
    # return connection to the Engine
    connection.close()


@pytest.fixture
def client(app: FastAPI, session: Session) -> t.Generator[TestClient, t.Any, None]:
    """Create a new FastAPI TestClient.

    This fixture uses the `session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client
