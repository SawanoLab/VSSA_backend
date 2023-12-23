from database import Base
from sqlalchemy import Column, String, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class Season(Base, TimestampMixin):
    __tablename__ = 'seasons'
    uuid = Column(UUIDType(binary=False),
                  primary_key=True,
                  default=uuid4)
    start_day = Column(DATETIME, nullable=False)
    end_day = Column(DATETIME, nullable=False)
    season_name = Column(String(128), nullable=False)
    game_format = Column(String(128), nullable=False)
    code = Column(String(128), nullable=False)

    user_id = Column(UUIDType(binary=False),
                     ForeignKey('users.uuid'),
                     nullable=False)

    user = relationship(
        'User',
        back_populates='seasons'
    )

    teams = relationship(
        'Teams',
        back_populates='season'
    )

    players = relationship(
        'Player',
        back_populates='season'
    )

    matchs = relationship(
        'Match',
        back_populates='season'
    )
