from datetime import datetime
from tenacity import retry, stop_after_attempt, wait_exponential
from resume_agent.appliers.greenhouse_applier import GreenhouseApplier
from resume_agent.appliers.ashby_applier import AshbyApplier
from resume_agent.database.sqlite_manager import SQLiteManager
from resume_agent.monitoring.logger import logger
from resume_agent.monitoring.metrics import JOBS_APPLIED, PROCESSING_TIME

class ApplyAgent:
    def __init__(self):
        self.greenhouse = GreenhouseApplier()
        self.ashby = AshbyApplier()
        self.db = SQLiteManager()

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        reraise=True
    )
    def _execute_apply(self, job, resume_path):
        """Internal method to execute application with retries."""
        if job.source == "Greenhouse":
            return self.greenhouse.apply(job, resume_path)
        elif job.source == "Ashby":
            return self.ashby.apply(job, resume_path)
        else:
            logger.warning(f"No applier implemented for source: {job.source}")
            return False

    def apply(self, job, resume_path):
        """Main application entry point with error handling and monitoring."""
        start_time = datetime.now()
        success = False
        error_msg = None

        logger.info(f"Starting application process for {job.title} at {job.company} (Source: {job.source})")
        
        try:
            with PROCESSING_TIME.labels(stage="apply").time():
                success = self._execute_apply(job, resume_path)
            
            status = "APPLIED" if success else "FAILED"
            JOBS_APPLIED.labels(source=job.source, status=status).inc()
            
            if success:
                logger.info(f"Successfully applied to {job.company}")
            else:
                logger.warning(f"Failed to apply to {job.company} - check applier logs")

        except Exception as e:
            logger.exception(f"Critical error applying to {job.company}: {str(e)}")
            JOBS_APPLIED.labels(source=job.source, status="ERROR").inc()
            status = "ERROR"
            error_msg = str(e)
            success = False

        # Save to database with detailed status
        try:
            self.db.save_application(
                job_id=getattr(job, 'id', 1), # Fallback if job object is incomplete
                status=status,
                applied_at=datetime.now(),
                resume_path=resume_path,
                notes=f"{job.company} - {job.title} | Error: {error_msg}" if error_msg else f"{job.company} - {job.title}"
            )
        except Exception as db_e:
            logger.error(f"Failed to save application status to database: {db_e}")

        return success
