from resume_agent.browser.playwright_manager import PlaywrightManager

class SessionManager:

    def __init__(self):

        self.browser = PlaywrightManager()

        self.page = None

    def open_browser(self):

        self.page = self.browser.start()

    def open_url(
        self,
        url
    ):

        self.page.goto(
            url,
            wait_until="networkidle"
        )

    def save_session(self):

        print(
            "Session automatically stored in browser_profile/"
        )

    def close(self):

        self.browser.close()