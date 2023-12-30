from database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class MatchScore(Base, TimestampMixin):
    __tablename__ = 'match_scores'
    uuid = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    match_set_score_id = Column(UUIDType(binary=False),
                                ForeignKey('match_set_score.uuid'),
                                nullable=False)
    score_team_id = Column(UUIDType(binary=False),
                           ForeignKey('teams.uuid'),
                           nullable=False)
    home_team_score = Column(Integer, nullable=False, default=0)
    away_team_score = Column(Integer, nullable=False, default=0)
    sequence_number = Column(Integer, nullable=False, default=0)

    match_set_score = relationship(
        'MatchSetScore',
        back_populates='matchscore',
    )

    score_team = relationship(
        'Teams',
        back_populates='matchscore'
    )
