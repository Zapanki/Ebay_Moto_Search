import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.mark.parametrize(("make", "model", "zipcode"),
                         [
                             ("BMW", "125i", "00501"),
                             ("Tesla", "X", "99950")
                         ])


@pytest.mark.ebay_motors
def test_wait_for_the_dropdown(browser_chrome, make, model, zipcode):
    browser_chrome.get('http://www.ebay.com/')
    select = Select(browser_chrome.find_element(By.ID, "gh-cat"))
    select.select_by_visible_text("eBay Motors")
    browser_chrome.find_element(By.ID, "gh-btn").click()
    browser_chrome.implicitly_wait(5)
    select = Select(browser_chrome.find_element(By.NAME, "Make"))
    select.select_by_visible_text(make)
    browser_chrome.implicitly_wait(5)
    select = Select(browser_chrome.find_element(By.NAME, "Model"))
    select.select_by_visible_text(model)
    browser_chrome.find_element(By.CLASS_NAME, "textbox__control").send_keys(zipcode)
    browser_chrome.find_element(By.CLASS_NAME, "motors-finder__find-btn").click()