
class DashboardPage:

    def __init__(self, page):
        self.page = page

        # Locators
        self.dashboard_heading = page.get_by_role(
            'heading', name='Dashboard'
        )
