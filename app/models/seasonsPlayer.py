from database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class SeasonsPlayer(Base, TimestampMixin):
    __tablename__ = 'seasonsPlayers'
    uuid = Column(UUIDType(binary=False),
                  primary_key=True,
                  default=uuid4)
    # UUID (foreignKey links to Seasons table's UUID)
    season_id = Column(UUIDType(binary=False),
                       ForeignKey('seasons.uuid'),
                       nullable=False)
    # UUID (foreignKey links to Players table's UUID)
    player_id = Column(UUIDType(binary=False),
                       ForeignKey('players.uuid'),
                       nullable=False)

    season = relationship(
        'Season',
        back_populates='seasons_players'
    )

    player = relationship(
        'Player',
        back_populates='seasons_players'
    )
