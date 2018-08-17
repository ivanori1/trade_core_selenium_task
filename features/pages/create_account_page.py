from features.base.browser import Browser


class CreateAccount(Browser):
    # create account page locators  Locators
    _next_button ="#button-step"
    _required_field = "[ng-message='required']"

    def click_next(self):
        self.wait_for_element_to_be_clickable(self._next_button)
        self.click_on_element(self._next_button)

    def verified_required_field_visible(self):
        result = self.is_visible_element(self._required_field)
        return result
