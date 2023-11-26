from database import Base
from sqlalchemy import Column, String, DATETIME, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class MatchScore(Base, TimestampMixin):
    __tablename__ = 'match_scores'
    uuid = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    home_team_score = Column(Integer, nullable=False, default=0)
    away_team_score = Column(Integer, nullable=False, default=0)

    match = relationship('Match', back_populates='matchscore', uselist=False)
