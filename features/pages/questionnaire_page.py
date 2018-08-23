from features.base.browser import Browser


class Questionnaire(Browser):
    # Elements on Questionnaire page
    _read_terms = ".checkbox"
    _finish_button = "#button-step"
    _select_shares = "//select[@id='form-shares']"
    _select_forex = "//select[@id='form-forex']"
    _select_cdfs = "//select[@id='form-cfds']"
    _select_relevant_experience = "//select[@id='form-relevant_experience']"
    _select_trading_accounts = "//select[@id='form-trading_accounts']"
    _select_currency = "//select[@id='form-currency']"
    _select_annual_income = "//select[@id='form-approx_annual_income']"
    _select_employment_status = "//select[@id='form-employment_status']"
    _select_liquid_savings = "//select[@id='form-liquid_savings']"
    _visible_answer = "/following-sibling::div[1]"  # use selected_ + _visible_answer to combine for element locator

    def verify_read_terms_is_visible(self):
        self.wait_for_element_to_be_clickable(self._read_terms)
        result = self.is_visible_element(self._read_terms)
        return result

    def click_finish(self):
        self.wait_for_element_to_be_clickable(self._read_terms)
        self.click_on_element(self._finish_button)

    def select_from_shares(self, answer):
        self.driver.execute_script("document.getElementById('form-shares').setAttribute('style', 'inline-block')")
        self.select_from_dropdown(answer, self._select_shares, "xpath")

    def verify_answer_selected_from_shares(self, answer):
        result = self.text_of_element(answer, self._select_shares + self._visible_answer, "xpath")
        return result

    def select_from_forex(self, answer):
        self.driver.execute_script("document.getElementById('form-forex').setAttribute('style', 'inline-block')")
        self.select_from_dropdown(answer, self._select_forex, "xpath")

    def verify_answer_selected_from_forex(self, answer):
        result = self.text_of_element(answer, self._select_forex + self._visible_answer, "xpath")
        return result

    def select_from_cdfs(self, answer):
        self.driver.execute_script("document.getElementById('form-cfds').setAttribute('style', 'inline-block')")
        self.select_from_dropdown(answer, self._select_cdfs, "xpath")

    def verify_answer_selected_from_cdfs(self, answer):
        result = self.text_of_element(answer, self._select_cdfs + self._visible_answer, "xpath")
        return result

    def select_from_relevant_experience(self, answer):
        self.driver.execute_script("document.getElementById('form-relevant_experience').setAttribute('style', 'inline-block')")

        self.select_from_dropdown(answer, self._select_relevant_experience, "xpath")

    def verify_answer_selected_relevant_experience(self, answer):
        result = self.text_of_element(answer, self._select_relevant_experience + self._visible_answer, "xpath")
        return result

    def select_from_relevant_trading_accounts(self, answer):
        self.driver.execute_script("document.getElementById('form-trading_accounts').setAttribute('style', 'inline-block')")
        self.select_from_dropdown(answer, self._select_trading_accounts, "xpath")

    def verify_answer_selected_trading_accounts(self, answer):
        result = self.text_of_element(answer, self._select_trading_accounts + self._visible_answer, "xpath")
        return result

    def select_currency(self, answer):
        self.driver.execute_script(
            "document.getElementById('form-currency').setAttribute('style', 'inline-block')")
        self.select_from_dropdown(answer, self._select_currency, "xpath")

    def verify_answer_selected_currency(self, answer):
        result = self.text_of_element(answer, self._select_currency + self._visible_answer, "xpath")
        return result

    def select_annual_income(self, answer):
        self.driver.execute_script(
            "document.getElementById('form-approx_annual_income').setAttribute('style', 'inline-block')")
        self.select_from_dropdown(answer, self._select_annual_income, "xpath")

    def verify_answer_selected_annual_income(self, answer):
        result = self.text_of_element(answer, self._select_annual_income + self._visible_answer, "xpath")
        return result

    def select_employment_status(self, answer):
        self.driver.execute_script(
            "document.getElementById('form-employment_status').setAttribute('style', 'inline-block')")
        self.select_from_dropdown(answer, self._select_employment_status, "xpath")

    def verify_answer_selected_employment_status(self, answer):
        result = self.text_of_element(answer, self._select_employment_status + self._visible_answer, "xpath")
        return result

    def select_savings(self, answer):
        self.driver.execute_script(
            "document.getElementById('form-liquid_savings').setAttribute('style', 'inline-block')")
        self.select_from_dropdown(answer, self._select_liquid_savings, "xpath")

    def verify_answer_selected_savings(self, answer):
        result = self.text_of_element(answer, self._select_liquid_savings + self._visible_answer, "xpath")
        return result

    def check_read_terms(self):
        if not self.is_selected_element(self._read_terms):
            self.click_on_element(self._read_terms)

    def verify_portal_page_is_open(self):
        result = self.get_page_url()
        return result