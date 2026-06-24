from typing import Optional
from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API Keys
    OPENAI_API_KEY: Optional[str] = Field(None, description="OpenAI API Key for LLM operations")
    GEMINI_API_KEY: Optional[str] = Field(None, description="Gemini API Key for LLM operations")
    
    # LinkedIn Credentials
    LINKEDIN_EMAIL: Optional[str] = Field(None, description="LinkedIn login email")
    LINKEDIN_PASSWORD: Optional[str] = Field(None, description="LinkedIn login password")
    
    # Database
    DATABASE_URL: str = Field("sqlite:///resume_agent.db", description="Database connection URL")
    
    # Monitoring
    LOG_LEVEL: str = Field("INFO", description="Logging level")
    METRICS_PORT: int = Field(8000, description="Port for Prometheus metrics")
    
    # Browser Settings
    HEADLESS: bool = Field(True, description="Run browser in headless mode")
    SLOW_MO: int = Field(100, description="Slow down browser operations by ms")

    @model_validator(mode="after")
    def validate_at_least_one_key(self) -> 'Settings':
        if not self.OPENAI_API_KEY and not self.GEMINI_API_KEY:
            raise ValueError("Either OPENAI_API_KEY or GEMINI_API_KEY must be provided")
        return self

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": True,
        "extra": "ignore",  # Ignore extra environment variables in prod
    }


# Initialize settings with validation
try:
    settings = Settings()
except Exception as e:
    print(f"Configuration Error: {e}")
    # In production, we might want to exit if configuration is invalid
    # sys.exit(1)
    # For now, we'll allow it to continue so the user can fix it in .env
    settings = None
