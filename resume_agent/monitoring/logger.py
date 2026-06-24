import sys
from pathlib import Path
from loguru import logger

# Create logs directory
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def setup_logger(log_level="INFO"):
    """Configures loguru logger with console and file handlers."""
    # Remove default handler
    logger.remove()

    # Add console handler
    logger.add(
        sys.stderr,
        level=log_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    )

    # Add file handler for all logs
    logger.add(
        LOG_DIR / "app.log",
        rotation="10 MB",
        retention="1 week",
        level=log_level,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        compression="zip"
    )

    # Add separate file handler for errors
    logger.add(
        LOG_DIR / "error.log",
        rotation="10 MB",
        retention="1 month",
        level="ERROR",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        backtrace=True,
        diagnose=True
    )

    return logger

# Initialize logger
setup_logger()
