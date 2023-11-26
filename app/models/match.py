from database import Base
from sqlalchemy import Column, String, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class Match(Base, TimestampMixin):
    __tablename__ = 'matchs'
    uuid = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    home_team_id = Column(String(225), ForeignKey(
        'teams.uuid'), nullable=False)
    away_team_id = Column(String(225), ForeignKey(
        'teams.uuid'), nullable=False)
    season_id = Column(String(225), ForeignKey('seasons.uuid'), nullable=False)
    user_id = Column(String(225), ForeignKey('users.uuid'), nullable=False)
    matchscore_id = Column(String(225), ForeignKey(
        'match_scores.uuid'), nullable=False)

    player_match_info = relationship('PlayerMatchInfo', back_populates='match')

    user = relationship('User', back_populates='matchs')

    home_team = relationship('Teams', foreign_keys=[
                             home_team_id], back_populates='home_matches')
    away_team = relationship('Teams', foreign_keys=[
                             away_team_id], back_populates='away_matches')
    season = relationship('Season', back_populates='matchs')

    matchscore = relationship('MatchScore', back_populates='match')
