from database import Base
from sqlalchemy import Column, String, DATETIME, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class PlayerMatchInfo(Base, TimestampMixin):
    __tablename__ = 'playerMatchInfo'
    uuid = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    player_id = Column(String(225), ForeignKey('players.uuid'), nullable=False)
    match_id = Column(String(255), ForeignKey('matchs.uuid'), nullable=False)
    on_court = Column(Boolean, nullable=False)
    zone_code = Column(String(255), nullable=False)
    libero = Column(Boolean, nullable=False)

    player = relationship('Player', back_populates='player_match_infos')
    match = relationship('Match', back_populates='player_match_info')
