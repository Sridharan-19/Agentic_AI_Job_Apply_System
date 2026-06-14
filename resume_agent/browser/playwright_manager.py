from pathlib import Path
from playwright.sync_api import sync_playwright


PROFILE_DIR = Path("./browser_profile")


class PlaywrightManager:

    def __init__(
            self,
            headless=False
    ):

        self.headless = headless
        self.playwright = None
        self.context = None
        self.page = None

    def start(self):

        self.playwright = sync_playwright().start()

        self.context = (
            self.playwright.chromium.launch_persistent_context(
                user_data_dir=str(PROFILE_DIR),
                headless=self.headless,
                viewport={"width": 1600, "height": 900}
            )
        )

        if self.context.pages:
            self.page = self.context.pages[0]
        else:
            self.page = self.context.new_page()

        return self.page

    def close(self):

        if self.context:
            self.context.close()

        if self.playwright:
            self.playwright.stop()
