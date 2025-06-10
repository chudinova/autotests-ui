class SidebarComponent:
    def __init__(self, page):
        self.users_list_item = page.get_by_test_id('users-list-item')
        self.courses_list_item = page.get_by_test_id('courses-list-item')
        self.accounts_list_item = page.get_by_test_id('accounts-list-item')

    def navigate_to_users_page(self):
        self.users_list_item.click()

    def navigate_to_courses_page(self):
        self.courses_list_item.click()

    def navigate_to_accounts_page(self):
        self.accounts_list_item.click()
