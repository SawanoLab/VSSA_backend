import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from env import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
from sqlalchemy.ext.declarative import declarative_base


def load_sql_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sql_commands = file.read().split(';')
        for command in sql_commands:
            try:
                if command.strip() != '':
                    db.execute(command)
            except sqlalchemy.exc.SQLAlchemyError as e:
                print(f"Error executing command: {command}")
                print(f"Error: {e}")


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
SessionLocal = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
)
db = SessionLocal()
Base = declarative_base()
Base.metadata.create_all(bind=engine)
seed_file_path = './seed.sql'
load_sql_file(seed_file_path)
db.commit()
db.close()
print('seeded')
