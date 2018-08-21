from features.base.browser import Browser


class CreateAccount(Browser):
    # create account page locators  Locators
    _first_name = ".posr [name='first_name']"
    _last_name = ".posr [name='last_name']"
    _email = ".posr [name='email']"
    _password = ".posr [name='password']"
    _phone = ".posr [name='telephone']"
    _selected_flag = ".selected-flag"
    _date_of_birth = ".posr [name='date_of_birth']"
    _country = "#form-addr_country"
    _chosen_country = ".chosen-single"
    _postcode = ".posr [name='addr_zip']"
    _address = ".posr [name='addr_street']"
    _city = ".posr [name='addr_city']"
    _next_button = "#button-step"
    _error_field = "[ng-message]"
    _other_error_field = "[ng-message][ng-if]"

    def type_first_name(self, data="Ivan"):
        self.send_keys_to_element(data, self._first_name)

    def type_last_name(self, data="Coric"):
        self.send_keys_to_element(data, self._last_name)

    def type_email(self, data="ivan.coric@tradecore.com"):
        self.send_keys_to_element(data, self._email)

    def type_password(self, data="Ivanori1"):
        self.send_keys_to_element(data, self._password)

    def select_phone_country(self):
        pass

    def type_phone(self, data="381616468058"):
        self.send_keys_to_element(data, self._phone)

    def type_date_of_birth(self, data="20/07/1991"):
        self.send_keys_to_element(data, self._date_of_birth)

    def select_country(self, data):
        self.select_from_dropdown(data, self._country)

    def verified_country_is_selected(self, data):
        result = self.text_of_element(data, self._chosen_country)
        return result

    def type_postcode(self, data="11000"):
        self.send_keys_to_element(data, self._postcode)

    def type_address(self, data="Radnicka 51"):
        self.send_keys_to_element(data, self._address)

    def type_city(self, data="Beograd"):
        self.send_keys_to_element(data, self._city)

    def click_next(self):
        self.wait_for_element_to_be_clickable(self._next_button)
        self.click_on_element(self._next_button)

    def verified_this_field__is_required_visible(self, inner_text):
        result = self.text_of_element(inner_text, self._error_field)
        return result

    def verified_other_error_message(self, inner_text):
        result = self.text_of_element(inner_text, inner_text)
        return result

    def verified_selected_flag(self, country):
        result = self.attribute_value_of_element("title", self._selected_flag)
        if country in result:
            return True
