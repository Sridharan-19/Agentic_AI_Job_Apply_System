import sys
import os

# Fix path for direct execution
sys.path.append(os.getcwd())

from database.models import Base
from database.session import engine, check_db_connection
from monitoring.logger import logger
from monitoring.metrics import start_metrics_server
from config.settings import settings
from agents.search_agent import SearchAgent

def run_search_agent():
    agent = SearchAgent()
    return agent.run()

def initialize_database():
    """Initializes the database schema."""
    try:
        Base.metadata.create_all(engine)
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        sys.exit(1)

def main():
    """Main entry point for the production-ready resume agent."""
    logger.info("Starting Autonomous Resume Agent")

    # 1. Validate Configuration
    if not settings:
        logger.error("Invalid configuration. Please check your .env file.")
        sys.exit(1)

    # 2. Start Metrics Server
    if start_metrics_server(settings.METRICS_PORT):
        logger.info(f"Metrics server started on port {settings.METRICS_PORT}")
    else:
        logger.warning(f"Failed to start metrics server on port {settings.METRICS_PORT}")

    # 3. Check Database
    if not check_db_connection():
        logger.error("Database connection check failed. Exiting.")
        sys.exit(1)

    # 4. Initialize Schema
    initialize_database()

    # 5. Start the Agent Workflow
    try:
        logger.info("Agent workflow initiated. (Simulated run for testing)")
        # run_search_agent()
    except KeyboardInterrupt:
        logger.info("Shutdown requested by user")
    except Exception as e:
        logger.critical(f"Unhandled exception in agent workflow: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
