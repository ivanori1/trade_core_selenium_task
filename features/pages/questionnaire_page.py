from features.base.browser import Browser


class Questionnaire(Browser):
    # Elements on Questionnaire page
    _read_terms = ".checkbox"
    _finish_button = "#button-step"
    _select_shares = "//select[@id='form-shares']"
    _visible_answer = "/following-sibling::div[1]"  # use selected_ + _visible_answer to combine for element locator

    def verify_read_terms_is_visible(self):
        self.wait_for_element_to_be_clickable(self._read_terms)
        result = self.is_visible_element(self._read_terms)
        return result

    def click_finish(self):
        self.wait_for_element_to_be_clickable(self._read_terms)
        self.click_on_element(self._finish_button)

    def select_from_shares(self, answer):
        self.select_from_dropdown(answer, self._select_shares, "xpath")

    def verify_answer_selected_from_shares(self, answer):
        result = self.text_of_element(answer, self._select_shares + self._visible_answer, "xpath")
        return result
