from selenium import webdriver
import geckodriver_binary  # Adds geckodriver binary to path

def test_driver():
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.titl
    driver.quit()
