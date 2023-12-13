from database import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = 'users'
    uuid = Column(UUIDType(binary=False),
                  primary_key=True,
                  default=uuid4)
    username = Column(String(128), nullable=False)

    seasons = relationship(
        'Season',
        back_populates='user'
    )

    teams = relationship(
        'Teams',
        back_populates='user'
    )

    players = relationship(
        'Player',
        back_populates='user'
    )

    matchs = relationship(
        'Match',
        back_populates='user',
        primaryjoin='User.uuid == Match.user_id'
    )

    attacks = relationship('Attack', back_populates='user')
