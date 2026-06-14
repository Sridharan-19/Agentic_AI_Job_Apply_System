from resume_agent.browser.session_manager import SessionManager


session = SessionManager()

session.open_browser()

session.open_url(
    "https://www.google.com"
)

input(
    "Press enter to close browser..."
)

session.close()