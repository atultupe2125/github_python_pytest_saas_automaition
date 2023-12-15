import pytest
from selenium import webdriver
from python_pytest.Config.config import TestData

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass