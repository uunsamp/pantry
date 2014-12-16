from pantry.db import Base
from sqlalchemy import Column, Integer, String

class Food(Base):
    __tablename__ = 'food'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    amount = Column(Integer, unique=False)

    def __repr__(self):
        return '<Food %r>' % self.name
