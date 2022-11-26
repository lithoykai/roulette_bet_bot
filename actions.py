from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import mensagem

def moveClick(a,b):
    pyautogui.moveTo(a, b)
    pyautogui.click()

def sendKeysEnter(elem, string):
    elem.send_keys(string)
    elem.send_keys(Keys.RETURN)

def login(driver):
    elem = driver.find_element(By.NAME, 'Username')
    sendKeysEnter(elem, "#") #Change # to your username
    elem = driver.find_element(By.NAME, 'Password')
    sendKeysEnter(elem, "#") #Change # to your password


def start(driver, LINK_SITE):
        driver.get("https://br.betano.com/") #Conectando ao site da Betano
        driver.find_element(By.XPATH, '//*[@id="landing-page-modal"]/div/div[2]/div[1]/p[2]/a').click()
        time.sleep(5)
        iframe = driver.find_element(By.CSS_SELECTOR, "#iframe-modal > div > iframe") 
        driver.switch_to.frame(iframe) 
        login(driver)
        time.sleep(5)
        driver.get(LINK_SITE)
        driver.implicitly_wait(20)
        change = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/main/div[1]/div/div[1]/div/div[1]/div/iframe')
        driver.switch_to.frame(change)
        driver.implicitly_wait(32)

def apostarInVoisins():
    moveClick(923, 690)
    sleep(0.5)
    moveClick(425, 574)

def apostarInVoisinsGale():
    moveClick(923, 690)
    sleep(0.5)
    moveClick(425, 574)
    moveClick(425, 574)

def inactive(driver, LINK_SITE):
    driver.get(LINK_SITE)
    mensagem.inactive()