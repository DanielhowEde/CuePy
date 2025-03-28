from src.core.browser_manager import get_browser
from src.utilities.load_vars.dotenv_loader import get_all_env_vars, load_env
from src.utilities.load_vars.config_reader import load_properties
from selenium import webdriver

def before_all(context):
    load_env()
    # Load env vars and store in Behave context
    context.env = get_all_env_vars()
    config = load_properties('config.properties')
    context.config_data = config

    browser = config.get("browser", "chrome")
    context.driver = get_browser(browser)

    # Start browser based on env config (or default to chrome)
    browser = context.env.get("BROWSER", "chrome")
    context.driver = get_browser(browser)
    
    context.driver.implicitly_wait(10)
    context.base_url = config.get("url", "http://localhost:3000")

def after_all(context):
    context.driver.quit()
