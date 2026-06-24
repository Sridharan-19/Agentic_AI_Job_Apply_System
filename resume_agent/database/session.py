from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
try:
    from config.settings import settings
    from monitoring.logger import logger
except ImportError:
    from resume_agent.config.settings import settings
    from resume_agent.monitoring.logger import logger

# Use database URL from settings
DATABASE_URL = settings.DATABASE_URL if settings else "sqlite:///resume_agent.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
    pool_pre_ping=True, # Verify connection before using
    pool_recycle=3600,  # Recycle connections every hour
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def check_db_connection():
    """Verifies database connectivity."""
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        logger.info("Successfully connected to the database")
        return True
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        return False
