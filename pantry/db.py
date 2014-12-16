from pantry.models.food import Food
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

Base = declarative_base()

engine = create_engine('sqlite:////tmp/test.db', echo=True)

def create_seed(session):
    """puts toy data into the db
    """
    session.add_all([
        Food(name='apple', amount=3),
        Food(name='banana', amount=4),
    ])
    session.commit()

def init_db():
    """determines if db needs to be seeded
    """
    # I'm creating the db here
    # This can't be best practice?
    Base.metadata.create_all(engine)

    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    session = Session()

    # if seed data isn't in db, create it
    if session.query(Food).count() < 0:
        create_seed(session)
