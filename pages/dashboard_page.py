class DashboardPage:

    def __init__(self, page):
        self.page = page

        self.dashboard_heading = page.get_by_role(
            'heading', name='Dashboard'
        )

        self.user_profile = page.locator(
            '.oxd-userdropdown-tab'
        )

        self.logout_menu_item = page.get_by_role(
            'menuitem', name='Logout'
        )

    def logout(self):
        self.user_profile.click()
        self.logout_menu_item.click(timeout=60000)