class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        locator.click()

    def fill(self, locator, value):
        locator.fill(value)

    def get_text(self, locator):
        return locator.inner_text()

    def navigate(self, url):
        self.page.goto(url)