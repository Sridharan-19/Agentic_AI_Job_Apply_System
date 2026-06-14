from playwright.sync_api import (
    sync_playwright
)

from resume_agent.profile.profile_loader import (
    ProfileLoader
)


class LeverApplier:

    def apply(

            self,

            job,

            resume_path

    ):

        profile = (

            ProfileLoader()

            .get()

        )

        with sync_playwright() as p:

            browser = (

                p.chromium.launch(

                    headless=False,

                    slow_mo=300

                )

            )

            page = browser.new_page()

            print()

            print(

                "Opening:",

                job.title

            )

            page.goto(

                job.url,

                wait_until="networkidle"

            )

            page.pause()

            browser.close()

            return True