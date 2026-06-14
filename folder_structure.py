from pathlib import Path

# Root project directory
ROOT_DIR = "resume_agent"

# Folder structure
folders = [
    "agents",
    "browser",
    "scrapers",
    "database",
    "database/migrations",
    "vectorstore",
    "graph",
    "prompts",
    "profile",
    "notifications",
    "monitoring",
    "api",
    "scheduler",
    "config",
    "tests",
    "logs",
    "docker",
]

# Files to create
files = [
    "main.py",
    "requirements.txt",
    ".env",
    "Dockerfile",
    "docker-compose.yml",

    # config
    "config/config.yaml",
    "config/settings.py",

    # database
    "database/models.py",
    "database/session.py",
    "database/crud.py",

    # browser
    "browser/playwright_manager.py",
    "browser/session_manager.py",
    "browser/dom_parser.py",

    # agents
    "agents/search_agent.py",
    "agents/tailor_agent.py",
    "agents/apply_agent.py",
    "agents/screening_agent.py",
    "agents/retry_agent.py",
    "agents/notify_agent.py",

    # graph
    "graph/workflow.py",
    "graph/state.py",
    "graph/nodes.py",

    # vectorstore
    "vectorstore/embedding_manager.py",
    "vectorstore/faiss_manager.py",
    "vectorstore/resume_rag.py",

    # scrapers
    "scrapers/linkedin_scraper.py",
    "scrapers/greenhouse_scraper.py",
    "scrapers/lever_scraper.py",
    "scrapers/remoteok_scraper.py",
    "scrapers/wellfound_scraper.py",

    # prompts
    "prompts/tailoring_prompt.txt",
    "prompts/screening_prompt.txt",
    "prompts/apply_prompt.txt",

    # profile
    "profile/profile.yaml",

    # notifications
    "notifications/email_notify.py",
    "notifications/telegram_notify.py",
    "notifications/slack_notify.py",

    # monitoring
    "monitoring/logger.py",
    "monitoring/metrics.py",

    # api
    "api/app.py",
    "api/routes.py",

    # scheduler
    "scheduler/scheduler.py",
]


def create_structure():
    root = Path(ROOT_DIR)

    # Create root directory
    root.mkdir(exist_ok=True)

    # Create folders
    for folder in folders:
        path = root / folder
        path.mkdir(parents=True, exist_ok=True)

        # Create __init__.py inside every folder
        init_file = path / "__init__.py"
        init_file.touch(exist_ok=True)

    # Create files
    for file in files:
        file_path = root / file
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch(exist_ok=True)

    print(f"✅ Project structure created successfully under '{ROOT_DIR}/'")


if __name__ == "__main__":
    create_structure()
