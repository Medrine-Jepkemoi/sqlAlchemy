from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# creating the engine
engine = create_engine('sqlite:///:memory:')

# Creating the session
Session = sessionmaker(bind=engine)
session = Session()


# Creating the table
Base = declarative_base()

class Books(Base):
    __tablename__ ='books'

    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    genre = Column(String(50))
    publication_year = Column(Integer)

Base.metadata.create_all(engine)


 