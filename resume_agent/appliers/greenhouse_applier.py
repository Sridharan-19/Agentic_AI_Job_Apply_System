from playwright.sync_api import sync_playwright

from resume_agent.profile.profile_loader import (
    ProfileLoader
)

from resume_agent.agents.screening_question_agent import (
    ScreeningQuestionAgent
)

class GreenhouseApplier:

    def __init__(self):

        self.profile = (
            ProfileLoader()
            .get()
        )

        self.screening_agent = (
            ScreeningQuestionAgent()
        )
    
    
    def upload_resume(
        self,
        page,
        resume_path
        ):

        try:

            page.locator(

                "#resume"

            ).set_input_files(

                resume_path

            )

            print(

                "✓ Resume uploaded"

            )

            return True

        except Exception as e:

            print()

            print(

                "Resume upload failed"

            )

            print(

                e

            )

            return False

    
    def safe_fill(
            self,
            page,
            labels,
            value
        ):

            if value is None:

                return False

            for label in labels:

                #
                # Label
                #

                try:

                    page.get_by_label(

                        label,

                        exact=False

                    ).fill(

                        str(value)

                    )

                    print(

                        f"✓ Filled {label}"

                    )

                    return True

                except:

                    pass

                #
                # Placeholder
                #

                try:

                    page.get_by_placeholder(

                        label,

                        exact=False

                    ).fill(

                        str(value)

                    )

                    print(

                        f"✓ Filled placeholder {label}"

                    )

                    return True

                except:

                    pass

            return False
    
    

    def safe_fill_by_id(
        self,
        page,
        field_id,
        value
        ):


        if value is None:

            return False

        try:

            page.locator(

                f"#{field_id}"

            ).fill(

                str(value)

            )

            print(

                f"✓ Filled {field_id}"

            )

            return True

        except Exception:

            print(

                f"✗ Could not fill {field_id}"

            )

            return False


    def answer_screening_questions(
            self,
            page
        ):

            fields = []

            inputs = page.locator(
                'input[id^="question_"]'
            )

            textareas = page.locator(
                'textarea[id^="question_"]'
            )

            for i in range(inputs.count()):

                fields.append(

                    inputs.nth(i)

                )

            for i in range(textareas.count()):

                fields.append(

                    textareas.nth(i)

                )

            print()

            print(

                f"{len(fields)} screening questions found"

            )

            for field in fields:

                try:

                    question_id = field.get_attribute(
                        "id"
                    )

                    label = (

                        page.locator(

                            f'label[for="{question_id}"]'

                        )

                        .inner_text()

                    )

                    print()

                    print(

                        "Question:"

                    )

                    print(

                        label

                    )

                    answer = (

                        self.screening_agent

                        .answer_question(

                            label

                        )

                    )

                    print()

                    print(

                        "Answer:"

                    )

                    print(

                        answer

                    )

                    field.fill(

                        answer

                    )

                except Exception as e:

                    print(

                        e

                    )


    def answer_dropdown_questions(
            self,
            page
        ):

            dropdowns = page.locator(

                'select[id^="question_"]'

            )

            count = dropdowns.count()

            print()

            print(

                f"{count} dropdown questions found"

            )

            for i in range(count):

                try:

                    field = dropdowns.nth(i)

                    question_id = field.get_attribute(

                        "id"

                    )

                    label = (

                        page.locator(

                            f'label[for="{question_id}"]'

                        )

                        .inner_text()

                    )

                    options = (

                        field.locator(

                            "option"

                        )

                        .all_inner_texts()

                    )

                    print()

                    print(

                        "Question:"

                    )

                    print(

                        label

                    )

                    print(

                        options

                    )

                    answer = (

                        self.screening_agent

                        .choose_option(

                            label,

                            options

                        )

                    )

                    print(

                        "Selected:",

                        answer

                    )

                    field.select_option(

                        label=answer

                    )

                except Exception as e:

                    print(

                        e

                    )



    def answer_radio_questions(
            self,
            page
        ):

            radios = page.locator(
                'input[type="radio"]'
            )

            count = radios.count()

            print()

            print(
                f"{count} radio buttons found"
            )

            visited = set()

            for i in range(count):

                try:

                    radio = radios.nth(i)

                    name = radio.get_attribute(
                        "name"
                    )

                    if name in visited:

                        continue

                    visited.add(
                        name
                    )

                    radio.check()

                    print(
                        f"✓ Selected radio group {name}"
                    )

                except:

                    pass

    
    def answer_checkbox_questions(
            self,
            page
        ):

            checkboxes = page.locator(
                'input[type="checkbox"]'
            )

            count = checkboxes.count()

            print()

            print(
                f"{count} checkboxes found"
            )

            for i in range(count):

                try:

                    checkbox = checkboxes.nth(i)

                    label = checkbox.evaluate(
                        """
                        el => {
                            const lbl =
                            document.querySelector(
                            `label[for="${el.id}"]`
                            );

                            return lbl ?
                            lbl.innerText :
                            "";
                        }
                        """
                    )

                    if any(

                        x.lower() in label.lower()

                        for x in [

                            "agree",

                            "consent",

                            "privacy",

                            "terms"

                        ]

                    ):

                        checkbox.check()

                        print(

                            f"✓ Checked {label}"

                        )

                except:

                    pass


    def safe_select(
        self,
        page,
        labels,
        value
        ):

        if value is None:

            return False

        for label in labels:

            try:

                page.get_by_label(

                    label,

                    exact=False

                ).select_option(

                    label=str(value)

                )

                print(

                    f"✓ Selected {label}"

                )

                return True

            except:

                pass

            try:

                page.get_by_label(

                    label,

                    exact=False

                ).select_option(

                    str(value)

                )

                print(

                    f"✓ Selected {label}"

                )

                return True

            except:

                pass

        print(

            f"✗ Could not select {labels}"

        )

        return False

    def safe_checkbox(
        self,
        page,
        labels
    ):

        for label in labels:

            try:

                page.get_by_label(

                    label,

                    exact=False

                ).check()

                print(

                    f"✓ Checked {label}"

                )

                return True

            except:

                pass

        print(

            f"✗ Checkbox not found {labels}"

        )

        return False

    def safe_radio(
        self,
        page,
        labels
    ):

        for label in labels:

            try:

                page.get_by_label(

                    label,

                    exact=False

                ).check()

                print(

                    f"✓ Selected radio {label}"

                )

                return True

            except:

                pass

        print(

            f"✗ Radio button not found {labels}"

        )

        return False

    def safe_click(
        self,
        page,
        texts
    ):

        for text in texts:

            try:

                page.get_by_text(

                    text,

                    exact=False

                ).click()

                print(

                    f"✓ Clicked {text}"

                )

                return True

            except:

                pass

        print(

            f"✗ Could not click {texts}"

        )

        return False

                    

    def apply(
            self,
            job,
            resume_path
        ):

        profile = self.profile

        with sync_playwright() as p:

            browser = p.chromium.launch(

                headless=False,

                slow_mo=300

            )

            page = browser.new_page()

            print()
            print(
                "Opening:",
                job.title
            )

            print(
                job.url
            )

            page.goto(
                job.url,
                wait_until="networkidle"
            )

            page.wait_for_timeout(
                5000
            )

            print()

            print(
                "Current URL"
            )

            print(
                page.url
            )

            print()

            print(
                "Page Title"
            )

            print(
                page.title()
            )

            #
            # Debug screenshot
            #

            page.screenshot(

                path="turing_page.png",

                full_page=True

            )

            #
            # Playwright Inspector
            #

            page.pause()

            #
            # Upload Resume
            #

            self.upload_resume(

                page,

                resume_path

            )

            #
            # Screening Questions
            #

            self.answer_screening_questions(page)

            self.answer_dropdown_questions(page)

            self.answer_radio_questions(page)

            self.answer_checkbox_questions(page)

            #
            # Name
            #

            first_name = (

                profile["name"]

                .split()[0]

            )

            last_name = (

                profile["name"]

                .split()[-1]

            )

            self.safe_fill_by_id(

                page,

                "first_name",

                first_name

            )

            self.safe_fill_by_id(

                page,

                "last_name",

                last_name

            )

            #
            # Contact
            #

            self.safe_fill_by_id(

                page,

                "email",

                profile["email"]

            )

            self.safe_fill_by_id(

                page,

                "phone",

                profile["phone"]

            )

            #
            # LinkedIn
            #

            self.safe_fill(

                page,

                [

                    "LinkedIn",

                    "LinkedIn Profile"

                ],

                profile["linkedin"]

            )

            #
            # Portfolio
            #

            self.safe_fill(

                page,

                [

                    "Website",

                    "Portfolio",

                    "Personal Website"

                ],

                profile["portfolio"]

            )

            #
            # Current Company
            #

            self.safe_fill(

                page,

                [

                    "Current Company",

                    "Company"

                ],

                profile["current_company"]["company"]

            )

            #
            # Current Role
            #

            self.safe_fill(

                page,

                [

                    "Current Title",

                    "Current Role",

                    "Job Title"

                ],

                profile["current_company"]["role"]

            )

            #
            # Expected Salary
            #

            self.safe_fill(

                page,

                [

                    "Expected Salary",

                    "Desired Salary",

                    "Compensation Expectations"

                ],

                profile["expected_salary"]["amount"]

            )

            #
            # Notice Period
            #

            self.safe_fill(

                page,

                [

                    "Notice Period",

                    "Availability"

                ],

                profile["notice_period"]

            )

            print()

            print(

                "=" * 80

            )

            print(

                "Review application manually."

            )

            print(

                "Do NOT auto-submit yet."

            )

            print(

                "=" * 80

            )

            input(

                "Press Enter to close browser..."

            )

            browser.close()

            return True
