from database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class Player(Base, TimestampMixin):
    __tablename__ = 'players'
    uuid = Column(UUIDType(binary=False),
                  primary_key=True,
                  default=uuid4)
    number = Column(Integer, nullable=False)
    player_code = Column(String(128), nullable=False)
    surname = Column(String(128), nullable=False)
    name = Column(String(128), nullable=False)
    nickname = Column(String(128), nullable=False)
    position = Column(String(128), nullable=False)

    teams_players = relationship(
        'TeamsPlayer',
        back_populates='player'
    )

    season_players = relationship(
        'SeasonPlayer',
        back_populates='player'
    )

