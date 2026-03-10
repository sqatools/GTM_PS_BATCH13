class ValidationAgent:

    def verify_login(self, driver):

        assert "logged-in-successfully" in driver.current_url