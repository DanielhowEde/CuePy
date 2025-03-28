from behave import given, when, then
from src.pages.loginPOM import LoginPage

@given('the user navigates to the login page')
def step_navigate(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.go_to_login()

@when('the user enters username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.login_page.login(username, password)

@then('the user should see the dashboard')
def step_dashboard(context):
    assert context.login_page.is_dashboard_visible()