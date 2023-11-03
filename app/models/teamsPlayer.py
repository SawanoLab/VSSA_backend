from database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from .mixins import TimestampMixin
from uuid import uuid4

class TeamsPlayer(Base, TimestampMixin):
    __tablename__ = 'teamsPlayers'
    uuid = Column(UUIDType(binary=False),
                    primary_key=True,
                    default=uuid4)
    # UUID (foreignKey links to Teams table's UUID)
    team_id = Column(UUIDType(binary=False),
                     ForeignKey('teams.uuid'),
                     nullable=False)
    # UUID (foreignKey links to Players table's UUID)
    player_id = Column(UUIDType(binary=False),
                       ForeignKey('players.uuid'),
                       nullable=False)
    # UUID (foreignKey links to Seasons table's UUID)
    season_id = Column(UUIDType(binary=False),
                       ForeignKey('seasons.uuid'),
                       nullable=False)

    team = relationship(
        'Team',
        back_populates='teams_players'
    )

    player = relationship(
        'Player',
        back_populates='teams_players'
    )

    season = relationship(
        'Season',
        back_populates='teams_players'
    )
