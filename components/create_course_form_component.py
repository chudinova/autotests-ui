class CreateCourseFormComponent:
    def __init__(self, page):
        self.page = page
        self.title_input = page.get_by_test_id('create-course-title-input')
        self.description_input = page.get_by_test_id('create-course-description-input')
        self.max_score_input = page.get_by_test_id('create-course-max-score-input')
        self.submit_button = page.get_by_test_id('create-course-submit-button')

    def fill_form(self, title, description, max_score):
        self.title_input.fill(title)
        self.description_input.fill(description)
        self.max_score_input.fill(max_score)

    def submit(self):
        self.submit_button.click()
