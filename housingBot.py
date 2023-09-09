#!/usr/bin/env python 3.6.8 Anaconda 64-bit
# -*- coding: utf-8 -*-
#Created on Fri Aug  4 16:07:51 2023
#@author: frankgrijalva
#This is a script to make a housing site response bot

#Duty-free imports
import time
import requests
import schedule
import pyautogui
from pyautogui import press
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#Func-y town
##Notification generating func
def ElementFinder (driver, Xpath):
     foundeded = driver.find_element(By.XPATH, Xpath)
     return foundeded

def WaitForLoad (driver, timeOut, Xpath):
     thingToWaitFor = WebDriverWait(driver, timeOut).until(EC.presence_of_element_located((By.XPATH, Xpath)))
     return thingToWaitFor

def Notifee (msg):
     requests.post('https://api.mynotifier.app', {"apiKey": 'c7975dab-b5e8-409e-8686-2d8f91d7613b',
                                                  "message": msg,
                                                  "description": "Housing Alert!",
                                                  "type": "warning",
                                                  "body": "Testy test test",
                                                  "project": "279794"})




#Consts
pyautogui.FAILSAFE = False

##housing site URLs
paraURL = "https://www.pararius.com/login?_target_path=/english"
paraPricedURL = "https://www.pararius.com/apartments/utrecht/0-800"
kamerURL = "https://kamernet.nl/en"
kamerPricedURL = "https://kamernet.nl/en/for-rent/rooms-utrecht?radius=3&minSize=1&maxRent=8&listingTypes=2&listingTypes=4&listingTypes=8"
haURL = "https://housinganywhere.com/"
haPricedURL = "https://housinganywhere.com/s/Utrecht--Netherlands?priceMax=80000"
huurwURL = "https://www.huurwoningen.nl/in/utrecht/?price=0-800"
huurzURL = "https://www.huurzone.nl/account"
huurzPricedURL = "https://www.huurzone.nl/huurwoningen/utrecht?page=1&sort_by=price_asc&price_to=800"
huurpURL = "https://huurportaal.nl/en"
huurpPricedURL = "https://huurportaal.nl/en/for-rent?location=utrecht&rent=0-800"
fundaURL = "https://www.funda.nl"
fundaPricedURL = "https://www.funda.nl/zoeken/huur/?selected_area=%5B%22utrecht,5km%22%5D&price=%22-800%22"
mpURL = "https://www.marktplaats.nl"

##Credentials
paraUser = "frank.g65.tg@gmail.com"
paraPass = "Fkjks%LK.W72-_3"

haUser = "franktreygrijalva@gmail.com"
haPass = "yseBAgXw@3y2G.7"

huurzUsr = 'franktreygrijalva@gmail.com'
huurzPass = "WCeRZz2Tyh8HF5M"

##Scams and goners to skip
paraScamsNum = 3
kamerGons = 4
huurwGons = 2
huurzGons = 10
huurpGons = 8




#making the actual script into a massive func for scheduling
def Scraper ():

     #Pressing space to keep pc awake 0
     press("shift")

     ##sanity check to make sure notifications are coming through
     #testMsg = "TEST " + time.ctime()
     #Notifee(testMsg)


     # %% Pararius protocol

     ##launching the browser for Para searching
     driver = webdriver.Chrome()
     driver.get(paraURL)


     # ##fucking cookies pop-up
     # time.sleep(2)
     # cookiesPopUpLoaded = WaitForLoad(driver, 120, ".//html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/button[1]")
     # cookiesPopUpLoaded.click()


     ##finding, waiting for the username & password boxes to load, and populate them appropriately
     elParaUsernameTB = WaitForLoad(driver, 120, ".//html/body/div[3]/div/div/form/div[2]/div/div/input")
     elParaUsernameTB.send_keys(paraUser)

     elParaPasswordTB = WaitForLoad(driver, 120, ".//html/body/div[3]/div/div/form/div[3]/div/div[1]/input")
     elParaPasswordTB.send_keys(paraPass)
     elParaPasswordTB.send_keys(Keys.RETURN)


     #open the correct price and area search after the homepage loads
     paraHomeLoaded = WaitForLoad(driver, 120, ".//html/body/div[3]/div[1]/div/div/form/div/wc-autocomplete/div/div")
     driver.get(paraPricedURL)

     ##finding the number of results
     numOfParaOpt = driver.find_element(By.XPATH, ".//html/body/div[3]/div[3]/div[2]/div/div/div[1]/span")

     ##Printing the results and debug output
     print("\nPararius house ops:", numOfParaOpt.text)

     ##Phone notification stuff

     ##Pull in the global var with the number of scams or goner postings
     global paraScamsNum

     ##actual alert and goner posting num update logic
     if int(numOfParaOpt.text) > paraScamsNum:
         ##Crafting a good message
         goodGud = str(int(numOfParaOpt.text) - paraScamsNum) + " New houses on Pararius"

         ##sending the msg
         Notifee (goodGud)

         ##outputting the msg set
         print("\nPhone notif", goodGud)

         #updating new amount of options
         paraScamsNum = int(numOfParaOpt.text)


     #!!!next steps should probably involve sharing the Pararius links in the notification's body
     #!!!....even tho they don't seem to be clickable

     ##Killing the Para window
     driver.quit()




     # %% Housing Anywhere protocol

     driver = webdriver.Chrome()
     driver.get(haURL)

     ##login button
     logButt = WaitForLoad(driver, 120, ".//html/body/div[1]/div/div/header/div/div/div[3]/div/div[1]/div/div/form[1]/button")
     logButt.send_keys(Keys.RETURN)

     ##Actually logging in
     haUsernameBox = WaitForLoad(driver, 120, ".//html/body/main/div/section[5]/form/fieldset[1]/div/input")
     haUsernameBox.send_keys(haUser)

     haPassBox = WaitForLoad(driver, 120, ".//html/body/main/div/section[5]/form/fieldset[2]/div/input")
     haPassBox.send_keys(haPass)
     haPassBox.send_keys(Keys.RETURN)

     ##waiting for the page to load and then going to the correct URL to scrape
     haLandingPg = WaitForLoad(driver, 120,
                               ".//html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div/form/div/div[2]/div/div/div/div[1]/div/input")
     driver.get(haPricedURL)

     #!!!from here I gotta count the elements matching a real list item and compare to send a notification.........
     #!!!Problem is, there are no matching properties, so idk what a matching web element is like to trigger my own notification

     ##Killing the HA window
     driver.quit()




     # %% Pressing space to keep pc awake 1
     pyautogui.press("shift")




     # %% Kamernet protocol

     driver = webdriver.Chrome()
     driver.get(kamerPricedURL)

     ##fucking cookies
     cookiePopUpLoaded = WaitForLoad(driver, 120, ".//html/body/div[2]/div/div[2]/div[2]/a")
     cookiePopUpLoaded.send_keys(Keys.RETURN)

     cookiePolicyPageLoaded = WaitForLoad(driver, 120, ".//html/body/div[1]/div/main/section/div/form/button")
     cookiePolicyPageLoaded.send_keys(Keys.RETURN)

     ##waiting for the landing page before reopening the og page
     landingLoaded = WaitForLoad(driver, 120, ".//html/body/div[1]/div/main/section[2]/div/div[2]/form/div[4]")

     ###Actual housing page
     driver.get(kamerPricedURL)
     houseCountElementLoaded = WaitForLoad(driver, 120, ".//html/body/main/div[1]/div[8]/div[2]/div[2]/div/div[1]/div/div/div[2]/label/h2")

     ##reporting the number of houses
     numOfHousesTextBox = driver.find_element(By.XPATH, ".//html/body/main/div[1]/div[8]/div[2]/div[2]/div/div[1]/div/div/div[2]/label/h2")
     numOfHousesText = numOfHousesTextBox.text
     actualNumOfHousesMsg = ("\nKamernet ops: " + numOfHousesText[0])
     print(actualNumOfHousesMsg)

     ##Phone notif about the ops
     global kamerGons

     if int(numOfHousesText[0:2]) > kamerGons:
          Notifee(actualNumOfHousesMsg)
          kamerGons = int(numOfHousesText[0])

          #outputting to console knowledge of the notification
          print("\nPhone notified of", actualNumOfHousesMsg)

     ##Killing it softly with his song
     driver.quit()




     # %% Pressing space to keep pc awake 2
     pyautogui.press("shift")




     # %% Huurwoningen protocol

     driver = webdriver.Chrome()
     driver.get(huurwURL)

     ##cookies are the real monster
     # kookjesPopUpLoaded = WaitForLoad(driver, 120, ".//html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/button[2]")
     # kookjesPopUpLoaded.send_keys(Keys.RETURN)

     # kookjesSelectorWindowLoaded = WaitForLoad(driver, 120, "/html/body/div[6]/div[3]/div/div[3]/div[1]/button")
     # kookjesSelectorWindowLoaded.send_keys(Keys.RETURN)

     ##reporting the number of options
     huurwops = WebDriverWait(driver, 120).until(
          EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div/div[1]/span"))
          )

     ##outputting and phone notifying
     huurwMsg = "\nHuurwoningen ops: " + str(huurwops.text)[0]
     print(huurwMsg)

     ##notifying only if it's greater than it was
     global huurwGons
     if int(str(huurwops.text)[0:2]) > huurwGons:
          Notifee(huurwMsg)
          huurwGons = int(str(huurwops.text)[0])

          #console log of alert
          print("\nPhone notified of", huurwMsg)

     ##the killing floor
     driver.quit()




     # %% Pressing space to keep pc awake 3
     pyautogui.press("shift")




     # %% Huurzone protocol

     driver = webdriver.Chrome()
     driver.get(huurzURL)

     #alertsPopUp
     alertsPopUpNo = WaitForLoad(driver, 120, "/html/body/div[4]/div/div/div[2]/button[2]")
     alertsPopUpNo.send_keys(Keys.RETURN)

     #cookies selection (I'm full, no thanks)
     waitForCookiesToBake = WaitForLoad(driver, 120, './/html/body/div[1]/div/div[3]/div[1]/div[2]/div[1]/div/div/div/div/form/fieldset/div/div[*]/div/input')

     for i in range(2,5,1):
          killCookies = ElementFinder(driver, "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[1]/div/div/div/div/form/fieldset/div/div["+str(i)+"]/div/input")
          killCookies.click()
          time.sleep(1.2 + i*0.01)

     closePopUp = ElementFinder(driver, "/html/body/div[1]/div/div[4]/div[1]/div[2]/button[1]")
     closePopUp.click()

     #Kenny Logs-in time
     emailBox = ElementFinder(driver, "/html/body/div[2]/div/main/div/div[1]/form/div[1]/div/input")
     emailBox.click()
     emailBox.send_keys(huurzUsr)

     passBox = ElementFinder(driver, "/html/body/div[2]/div/main/div/div[1]/form/div[2]/div[2]/input")
     passBox.send_keys(huurzPass)

     clickyBoi = ElementFinder(driver, "/html/body/div[2]/div/main/div/div[1]/form/div[3]/button")
     clickyBoi.click()

     #go to the search page
     driver.get(huurzPricedURL)

     #report
     listOfHousingEl = driver.find_elements(By.XPATH, "/html/body/div[1]/div/form/main/div[3]/div/div[2]/div[2]/div[2]/a[*]")
     numOfHuurzOps = len(listOfHousingEl)
     huurzMsg = "\nHuurzone ops: " + str(numOfHuurzOps)
     print(huurzMsg)


     global huurzGons
     if numOfHuurzOps > huurzGons:
          huurzGons = numOfHuurzOps
          Notifee(huurzMsg)

          #logging alert
          print("\nPhone notif", huurzMsg)


     #getting rid of the evidence
     driver.quit()




     # %% Pressing space to keep pc awake 4
     pyautogui.press("shift")




     # %% Huurportal protocol

     driver = webdriver.Chrome()
     driver.get(huurpURL)

     ##dealing with cookies
     facknCookies = WaitForLoad(driver, 120, "/html/body/div[1]/div/div[1]/div[1]/div[2]/button[1]")
     facknCookies.click()

     saveNoCookies = WaitForLoad(driver, 120, "/html/body/div[1]/div/div[1]/div[2]/div[3]/button[2]")
     saveNoCookies.click()

     ##waiting for the landing to load and then jumping to the correct page
     loadedLanding = WaitForLoad(driver, 120, "/html/body/header")
     driver.get(huurpPricedURL)

     ##reporting
     opsTextEl = WaitForLoad(driver, 120, "/html/body/div[3]/div[5]/div[3]/div[1]/h1")
     opsText = opsTextEl.text[0:2]
     huurpMsg = "\nHuurportal ops: " + opsText
     print(huurpMsg)


     global huurpGons
     if int(opsText) > huurpGons:
           Notifee(huurpMsg)
           huurpGons = int(opsText)

           #log output
           print("\nPhone notified", huurpMsg)

     ##exiting
     driver.quit()




     # %% Pressing space to keep pc awake 5
     pyautogui.press("shift")




     # %% funda protocol

     ##########################################
     #They have bot protection
     ##########################################


     # driver = webdriver.Chrome()
     # driver.get(fundaURL)

     # ##fucking crumbs everywhere
     # crumbs = WaitForLoad(driver, 120, "/html/body/div[10]/div[2]/div/div/div[2]/div/button")
     # crumbs.click()

     # noCrumbsPls = WaitForLoad(driver, 120, "/html/body/div[10]/div[3]/div/div[3]/div[1]/button")
     # crumbs.click()

     # ##Search page loaded
     # srchPgLoaded = WaitForLoad(driver, 120, "/html/body/main/div[1]/div[3]")

     # ##proceed to the correct rental options page
     # driver.get(fundaPricedURL)

     # ##reporting
     # fundaOpsTxtEl = WaitForLoad(driver, 120, "/html/body/div[2]/div/div/div/section/main/div/div[1]/div[2]/div[1]/div[2]/h1/div[1]/font/font")
     # fundaOpsTxt = fundaOpsTxtEl.text[0:2]
     # print(fundaOpsTxt)


     # %% MP protocol

# %% scheduling

#Pressing space to keep pc awake
press("shift")

#Scheduling
schedule.every(150).seconds.do(Scraper)

while True:
     schedule.run_pending()
