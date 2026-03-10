from ..agents.planner_agent import PlannerAgent
from ..agents.action_agent import ActionAgent
from ..agents.validation_agent import ValidationAgent

def test_login_agent(driver):

    planner = PlannerAgent()
    action = ActionAgent(driver)
    validator = ValidationAgent()

    plan = planner.create_plan()

    for step in plan:

        if step != "validate_login":
            action.execute(step)

        else:
            validator.verify_login(driver)












