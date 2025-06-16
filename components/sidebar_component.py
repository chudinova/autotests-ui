from elements.list_item import ListItem


class SidebarComponent:
    def __init__(self, page):
        self.users_list_item = ListItem(page, 'users-list-item', 'Users')
        self.courses_list_item = ListItem(page, 'courses-list-item', 'Courses')
        self.accounts_list_item = ListItem(page, 'accounts-list-item', 'Accounts')

    def navigate_to_users_page(self):
        self.users_list_item.click()

    def navigate_to_courses_page(self):
        self.courses_list_item.click()

    def navigate_to_accounts_page(self):
        self.accounts_list_item.click()
