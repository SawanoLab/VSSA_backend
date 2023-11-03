from database import Base
from sqlalchemy import Column, String, DATETIME
from sqlalchemy import Column, ForeignKey, String
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

    teams_players = relationship(
        'TeamsPlayer',
        back_populates='season'
    )

    season_players = relationship(
        'SeasonPlayer',
        back_populates='season'
    )
