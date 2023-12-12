import sys
import pytest
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from env import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
from database import get_db
from main import app

sys.path.append(
    os.path.abspath(
        os.path.dirname(os.path.abspath(__file__)) +
        "/../app/"))


class TestingSession(Session):
    def commit(self):
        '''
        Override commit() function to prevent data from being persisted.
        '''
        self.flush()
        self.expire_all()


@pytest.fixture
def test_db():
    print('test_db')
    DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
        DB_USER,
        DB_PASSWORD,
        DB_HOST,
        DB_NAME,
    )

    engine = create_engine(
        DATABASE,
        encoding='utf-8',
    )

    TestSessionLocal = scoped_session(
        sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine,
            class_=TestingSession
        )
    )

    db = TestSessionLocal()

    Base = declarative_base()
    Base.query = TestSessionLocal.query_property()

    def get_db_for_testing():
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = get_db_for_testing

    yield db

    db.rollback()  # rollback after test


@pytest.fixture()
def client():
    ''' Getting testclient of app '''
    with TestClient(app) as client:
        yield client

