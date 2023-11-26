from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.session import Session
from typing import Generator

from env import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_NAME,
)

engine = create_engine(
    DATABASE,
    echo=True,
    pool_pre_ping=True
)

SessionLocal = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

metadata = MetaData(naming_convention={
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    # %(constraint_name)sを使用するとConstraintで明示的な名前が必要になるため無効化
    # 'ck': 'ck_%(table_name)s_`%(constraint_name)s`',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
})
Base = declarative_base(metadata=metadata)
Base.query = SessionLocal.query_property()


# Dependency
def get_db() -> Generator[Session, None, None]:
    db = None
    try:
        print('db.start()')
        db = SessionLocal()
        yield db
    except Exception as e:
        print(f'Error: {e}')
        print('Rolling back the session.')
        if db:
            db.rollback()
    finally:
        if db:
            print('db.close()')
            db.close()

