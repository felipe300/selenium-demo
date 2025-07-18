from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

def test_page_title():
    browser = webdriver.Firefox(service=FirefoxService("/usr/local/bin/geckodriver"))
    # browser = webdriver.Firefox()
    browser.get("https://github.com")

    titleElement = browser.find_element(By.ID, "hero-section-brand-heading")

    assert titleElement.text == "Build and ship software on a single, collaborative platform"

    browser.quit()
