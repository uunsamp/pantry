from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Food(Base):
    __tablename__ = 'food'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    amount = Column(Integer, unique=False)

    def __repr__(self):
        return '<Food %r>' % self.name
