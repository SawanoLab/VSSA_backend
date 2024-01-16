
from uuid import uuid4
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy_utils import UUIDType
from sqlalchemy.orm import relationship
from database import Base
from .mixins import TimestampMixin


class AttackTime(Base, TimestampMixin):
    __tablename__ = 'attack_times'
    uuid = Column(UUIDType(binary=False),
                  primary_key=True,
                  default=uuid4)
    start_time = Column(Integer,
                        nullable=False)
    sumnail_url = Column(String(128), nullable=False)

    match_id = Column(UUIDType(binary=False),
                      ForeignKey('matchs.uuid'),
                      nullable=False)

    match_img_path = Column(String(128), nullable=False)

    match = relationship(
        'Match',
        back_populates='attack_times'
    )
