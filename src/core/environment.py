from src.core.browser_manager import get_browser
from selenium import webdriver

def before_all(context):
    context.driver = get_browser()
    context.driver.implicitly_wait(10)

def after_all(context):
    context.driver.quit()