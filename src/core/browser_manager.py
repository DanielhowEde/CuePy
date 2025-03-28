from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_browser(browser_name="chrome"):
    browser_name = browser_name.lower()

    if browser_name == "firefox":
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == "edge":
        return webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    else:
        return webdriver.Chrome(executable_path=ChromeDriverManager().install())
