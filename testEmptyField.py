# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from config import *

def test_EmptyField(setup_driver):

    driver = setup_driver

    textAfterChange = driver.find_element("id", "textToBeChanged")

    buttonChange = driver.find_element("id", "buttonChange")
    buttonChange.click()

    textToBeChanged = driver.find_element("id", "textToBeChanged")

    assert textToBeChanged == textAfterChange

    userInput = driver.find_element("id", "userInput")
    userInput.send_keys(" ")

    buttonChange.click()

    textToBeChanged = driver.find_element("id", "textToBeChanged")

    assert textToBeChanged == textAfterChange





