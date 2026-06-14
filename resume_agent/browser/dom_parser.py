from bs4 import BeautifulSoup


class DOMParser:

    @staticmethod
    def extract_html(page):

        return page.content()

    @staticmethod
    def extract_visible_text(page):

        html = page.content()

        soup = BeautifulSoup(
            html,
            "lxml"
        )

        return soup.get_text(
            separator=" ",
            strip=True
        )

    @staticmethod
    def extract_forms(page):

        html = page.content()

        soup = BeautifulSoup(
            html,
            "lxml"
        )

        forms = []

        for form in soup.find_all("form"):

            forms.append(str(form))

        return forms