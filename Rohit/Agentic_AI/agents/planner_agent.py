class PlannerAgent:

    def create_plan(self):
        steps = [
            "open_login_page",
            "enter_username",
            "enter_password",
            "click_login",
            "validate_login"
        ]
        return steps