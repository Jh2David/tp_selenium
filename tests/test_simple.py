import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Initialisation du navigateur
    driver = webdriver.Chrome()
    yield driver
    # Fermeture du navigateur après le test
    driver.quit()

def test_open_google(driver):
    # Ouvrir la page Google
    driver.get("https://www.google.com")
    
    # Vérifier que le titre de la page est "Google"
    assert driver.title == "Google"
