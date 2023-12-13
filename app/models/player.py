from database import Base
from sqlalchemy import Column, String, DATETIME, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class Player(Base, TimestampMixin):
    __tablename__ = 'players'
    uuid = Column(UUIDType(binary=False),
                  primary_key=True,
                  default=uuid4)
    name = Column(String(128), nullable=False)
    player_number = Column(Integer, nullable=False)
    code = Column(String(128), nullable=False)
    postion = Column(String(128), nullable=False)
    weight = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)

    user_id = Column(UUIDType(binary=False),
                     ForeignKey('users.uuid'),
                     nullable=False)
    team_id = Column(UUIDType(binary=False),
                     ForeignKey('teams.uuid'),
                     nullable=False)
    season_id = Column(UUIDType(binary=False),
                       ForeignKey('seasons.uuid'),
                       nullable=False)

    user = relationship(
        'User',
        back_populates='players'
    )

    team = relationship(
        'Teams',
        back_populates='players'
    )

    season = relationship(
        'Season',
        back_populates='players'
    )

    player_match_infos = relationship(
        'PlayerMatchInfo',
        back_populates='player'
    )

    attacks = relationship(
        'Attack',
        back_populates='player'
    )
