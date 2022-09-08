# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from config import *
import pytest

text = "123"

def test_OpenNewActivity(setup_driver):
    driver = setup_driver

    userInput = driver.find_element("id","userInput")
    userInput.send_keys(text)

    buttonActivity = driver.find_element("id","buttonActivity")
    buttonActivity.click()

    driver.wait_activity("ShowTextActivity", 10)

    result = driver.find_element("id", "text").text

    assert result == text






