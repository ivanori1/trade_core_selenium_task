from features.base.browser import Browser


class CreateAccount(Browser):
    # create account page locators  Locators
    _first_name = ".posr [name='first_name']"
    _last_name = ".posr [name='last_name']"
    _email = ".posr [name='email']"
    _password = ".posr [name='password'"
    _country = "#form-addr_country"
    _chosen_country = ".chosen-single"

    _next_button = "#button-step"
    _required_field = "[ng-message='required']"

    def click_next(self):
        self.wait_for_element_to_be_clickable(self._next_button)
        self.click_on_element(self._next_button)

    def verified_required_field_visible(self):
        result = self.is_visible_element(self._required_field)
        return result

    def select_country(self):
        self.select_from_dropdown("Armenia", self._country)

    def verified_country_is_selected(self):
        result = self.text_of_element("Armenia", self._chosen_country)
        return result