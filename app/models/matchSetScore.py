from uuid import uuid4
from database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy_utils import UUIDType
from sqlalchemy.orm import relationship
from .mixins import TimestampMixin


class MatchSetScore(Base, TimestampMixin):
    __tablename__ = 'match_set_score'
    uuid = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    match_id = Column(UUIDType(binary=False),
                      ForeignKey('matchs.uuid'),
                      nullable=False)
    set_number = Column(Integer, nullable=False, default=0)
    score_team_home = Column(Integer, nullable=False, default=0)
    score_team_away = Column(Integer, nullable=False, default=0)

    matchscore = relationship(
        'MatchScore',
        back_populates='match_set_score'
    )

    match = relationship(
        'Match',
        back_populates='matchsetscore'
    )

    # winner_team = relationship(
    #     'Teams',
    #     back_populates='matchsetscore'
    # )
