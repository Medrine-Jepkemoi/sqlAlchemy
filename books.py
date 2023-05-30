from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# creating the engine
engine = create_engine('sqlite:///books.db')

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

    


# Base.metadata.create_all(engine)

# Inserting data into the table
#Creating instances of the table class

books1 = Books(title="How to live", genre = "Life", publication_year = 2000)

# Add data to session

session.add(books1)

# Commit changes to the db
session.commit()

