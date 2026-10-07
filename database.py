from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine(              # creates an SQLAlchemy Engine object
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # creates a factory for creating session

class Base(DeclarativeBase):  # Base class for all my SQLALchemy models like User, Post
    pass

def get_db(): # creates a database session and gives it to your API endpoint
    with SessionLocal() as db:
        yield db



