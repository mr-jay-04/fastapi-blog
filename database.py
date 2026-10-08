from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///./blog.db'

engine = create_async_engine(              # creates an SQLAlchemy Engine object
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,) # creates a factory for creating session

class Base(DeclarativeBase):  # Base class for all my SQLALchemy models like User, Post
    pass

async def get_db(): # creates a database session and gives it to your API endpoint
    async with AsyncSessionLocal() as session:
        yield session



