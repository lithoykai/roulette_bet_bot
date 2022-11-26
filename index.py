import threading
from time import sleep
from typing import final
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import actions
import mensagem
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

#Duzias
dozenOne = list(range(1, 13))
dozenTwo = list(range(13, 25))
dozenThree = list(range(25, 37))
noVoisins = ['9', '31', '14', '20', '1', '33', '16', '24', '5', '10', '23', '8', '30', '11', '36', '13', '27', '6', '34', '17']

# CONST
LINK_SITE = "https://br.betano.com/casino/live/games/quantum-auto-roulette/1389/tables/103087/"
booleanValueCont = False
nervousNumber = 3
nervousNumberVoisins = 6


def numbersToBoolean(valueToCheck, listToCheck, listInBoolean):
    listWithBooleanValue = valueToCheck in listToCheck
    listInBoolean.insert(0, listWithBooleanValue)
 
def verificationCount(count):
    if count == '17':
        return True
    else:
        return False

def greenResult(list, a, b):
    testList = [False, True, True]
    greenList = set(a) <= set(b)
    list.insert(0, greenList)
    if greenList == testList:
        return True

def main():
        # Variaveis globais.
        global noVoisins
        global booleanValueCont
        global nervousNumber
        global nervousNumberVoisins
        ###########
        whatDozen = [46]
        actions.start(driver, LINK_SITE)
        #cache
        calledNumbersInBoolean = [False]
        calledNumbers = [46]
        dozenOneListinBoolean = [False, False]
        dozenTwoListinBoolean = [False, False]
        dozenThreeListinBoolean = [False, False]
        veriList = [False, True, True, True]
        veriListVisions = [False, True, True, True, True, True]
        #########
        while True:
                count = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[5]/div[1]') 
                booleanValueContHist = booleanValueCont
                booleanValueContItem = count.get_attribute('innerText') 
                booleanValueCont = verificationCount(booleanValueContItem)
                
                if booleanValueContHist and (not booleanValueCont):
                    number = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div[2]/div[7]/div/div[2]/div/div[1]/div/div')
                    valueNumber = number.get_attribute('innerText') 
                    valueNumberInInt = int(valueNumber)
                    numbersToBoolean(valueNumber, noVoisins, calledNumbersInBoolean)
                    numbersToBoolean(valueNumberInInt, dozenOne, dozenOneListinBoolean)
                    numbersToBoolean(valueNumberInInt, dozenTwo, dozenTwoListinBoolean)
                    numbersToBoolean(valueNumberInInt, dozenThree, dozenThreeListinBoolean)
                    
                    limitedListOne = dozenOneListinBoolean[:4]
                    limitedListTwo = dozenTwoListinBoolean[:4]
                    limitedListThree = dozenThreeListinBoolean[:4]
                    limitedListVoisinsInBoolean = calledNumbersInBoolean[:6] #Lista em boolean dos voisins


                    limitedListOneBoolean = pd.Series(dozenOneListinBoolean[:5]).all()
                    limitedListTwoBoolean = pd.Series(dozenTwoListinBoolean[:5]).all()
                    limitedListThreeBoolean = pd.Series(dozenThreeListinBoolean[:5]).all()
                   
 
                    limitedListNumbersBoolean = pd.Series(calledNumbersInBoolean[:7]).all()
                    limitedListNumbersBooleanTwo = pd.Series(calledNumbersInBoolean[:8]).all()

                    calledNumbers.insert(0, valueNumberInInt) 
                    whatDozen = calledNumbers[:nervousNumber]

                    #Telegram messagem
                    if set(whatDozen) <= set(dozenOne):
                        mensagem.dezonOne(whatDozen)
                        if limitedListOneBoolean == True:
                            mensagem.gale()

                    elif set(whatDozen) <= set(dozenTwo):
                        mensagem.dezonTwo(whatDozen)
                        if limitedListTwoBoolean == True:
                            mensagem.gale()
                    
                    elif set(whatDozen) <= set(dozenThree):
                        mensagem.dezonThree(whatDozen)
                        if limitedListThreeBoolean == True:
                            mensagem.gale()

                    elif limitedListNumbersBoolean == True: 
                        mensagem.voisins(calledNumbers[:7])  
                        if limitedListNumbersBooleanTwo == True:
                            mensagem.gale()

                    elif valueNumber == '0':
                        mensagem.zero(calledNumbers[:2])


                    elif limitedListOne == veriList:
                        mensagem.green(whatDozen)
                    
                    
                    elif limitedListTwo == veriList:
                        mensagem.green(whatDozen)
                    
                    
                    elif limitedListThree == veriList:
                        mensagem.green(whatDozen)
                    
                    elif limitedListVoisinsInBoolean == veriListVisions:
                        mensagem.green(calledNumbers[:2])



                    
main()
                    