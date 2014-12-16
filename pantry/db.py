from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_db():
    engine = create_engine('sqlite:////tmp/test.db', echo=True)
    import ipdb; ipdb.set_trace()
