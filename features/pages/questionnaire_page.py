from features.base.browser import Browser


class Questionnaire(Browser):
    # Elements on Questionnaire page
    _read_terms = ".checkbox"
    _finish_button = "#button-step"

    def verify_read_terms_is_visible(self):
        self.wait_for_element_to_be_clickable(self._read_terms)
        result = self.is_visible_element(self._read_terms)
        return result

    def click_finish(self):
        self.wait_for_element_to_be_clickable(self._read_terms)
        self.click_on_element(self._finish_button)
