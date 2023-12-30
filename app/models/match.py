from database import Base
from sqlalchemy import Column, ForeignKey, String, Enum
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class Match(Base, TimestampMixin):
    __tablename__ = 'matchs'
    uuid = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    home_team_id = Column(UUIDType(binary=False),
                          ForeignKey('teams.uuid'),
                          nullable=False)
    away_team_id = Column(UUIDType(binary=False),
                          ForeignKey('teams.uuid'),
                          nullable=False)
    season_id = Column(UUIDType(binary=False),
                       ForeignKey('seasons.uuid'),
                       nullable=False)
    user_id = Column(UUIDType(binary=False),
                     ForeignKey('users.uuid'),
                     nullable=False)
    youtube_url = Column(String(128),
                         nullable=False)
    player_match_info = relationship(
        'PlayerMatchInfo',
        back_populates='match',
        cascade="all, delete-orphan"
    )

    user = relationship(
        'User',
        back_populates='matchs'
    )

    home_team = relationship(
        'Teams',
        foreign_keys=[home_team_id],
        back_populates='home_matches'
    )

    away_team = relationship(
        'Teams',
        foreign_keys=[away_team_id],
        back_populates='away_matches'
    )

    season = relationship(
        'Season',
        back_populates='matchs'
    )

    attacks = relationship(
        'Attack',
        back_populates='match',
        cascade="all, delete-orphan"
    )

    matchsetscore = relationship(
        'MatchSetScore',
        back_populates='match',
        cascade="all, delete-orphan"
    )
