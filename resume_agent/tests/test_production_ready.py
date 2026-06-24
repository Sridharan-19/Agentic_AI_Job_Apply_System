import unittest
import sys
import os
from unittest.mock import MagicMock, patch

# Add current directory to path
sys.path.append(os.getcwd())

from monitoring.logger import logger
from monitoring.metrics import JOBS_APPLIED

class TestProductionReadiness(unittest.TestCase):
    def test_logger_setup(self):
        """Test if logger is initialized and can log."""
        try:
            logger.info("Testing production logger")
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Logger failed: {e}")

    def test_settings_validation(self):
        """Test if settings validation works."""
        from config.settings import Settings
        with self.assertRaises(ValueError):
            # Should fail if API key is empty
            Settings(OPENAI_API_KEY="")

    def test_metrics_initialization(self):
        """Test if metrics are initialized."""
        self.assertIsNotNone(JOBS_APPLIED)
        # Check if labels work
        JOBS_APPLIED.labels(source="test", status="success")

    def test_db_connection_check(self):
        """Test database connection check logic."""
        import database.session
        from sqlalchemy import create_engine
        
        # Use a mock engine instead of patching the module attribute which is failing
        mock_engine = MagicMock()
        mock_conn = MagicMock()
        mock_engine.connect.return_value.__enter__.return_value = mock_conn
        
        # Temporarily swap engine
        original_engine = database.session.engine
        database.session.engine = mock_engine
        try:
            self.assertTrue(database.session.check_db_connection())
            mock_engine.connect.assert_called_once()
        finally:
            database.session.engine = original_engine

if __name__ == "__main__":
    unittest.main()
