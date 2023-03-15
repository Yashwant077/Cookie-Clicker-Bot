from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "YOUR CHROME DRIVER PATH Here"
driver = webdriver.Chrome(service=Service(chrome_driver_path), chrome_options=chrome_options)

CookieURL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(CookieURL)

cookie = driver.find_element(By.ID, "cookie")

right_panel = driver.find_element(By.ID, "rightPanel").text.split('\n')
for i in range(0, len(right_panel), 2):
    print(right_panel[i].split('-')[1])


def buy_something():
    # How much money do I have?
    money = driver.find_element(By.ID, "money")
    money = int(money.text.replace(',', ""))

    # How much does each bit cost?
    Cursor = driver.find_element(By.ID, "buyCursor")
    Cursor_price = int(Cursor.text.split('\n')[0].split('-')[1].replace(',', ""))
    Grandma = driver.find_element(By.ID, "buyGrandma")
    Grandma_price = int(Grandma.text.split('\n')[0].split('-')[1].replace(',', ""))
    Factory = driver.find_element(By.ID, "buyFactory")
    Factory_price = int(Factory.text.split('\n')[0].split('-')[1].replace(',', ""))
    Mine = driver.find_element(By.ID, "buyMine")
    Mine_price = int(Mine.text.split('\n')[0].split('-')[1].replace(',', ""))
    Shipment = driver.find_element(By.ID, "buyShipment")
    Shipment_price = int(Shipment.text.split('\n')[0].split('-')[1].replace(',', ""))
    AlchemyLab = driver.find_element(By.ID, "buyAlchemy lab")
    AlchemyLab_price = int(AlchemyLab.text.split('\n')[0].split('-')[1].replace(',', ""))
    Portal = driver.find_element(By.ID, "buyPortal")
    Portal_price = int(Portal.text.split('\n')[0].split('-')[1].replace(',', ""))
    TimeMachine = driver.find_element(By.ID, "buyTime machine")
    TimeMachine_price = int(TimeMachine.text.split('\n')[0].split('-')[1].replace(',', ""))

    if money > TimeMachine_price:
        TimeMachine.click()
    elif money > Portal_price:
        Portal.click()
    elif money > AlchemyLab_price:
        AlchemyLab.click()
    elif money > Shipment_price:
        Shipment.click()
    elif money > Mine_price:
        Mine.click()
    elif money > Factory_price:
        Factory.click()
    elif money > Grandma_price:
        Grandma.click()
    elif money > Cursor_price:
        Cursor.click()
    else:
        print("not enough money to buy anything")  # Technically don't need this, can skip


timeout = time.time() + 60 * 5  # 5 minutes from now

while time.time() < timeout:
    five_sec = time.time() + 5  # 5 seconds from now
    while time.time() < five_sec:
        cookie.click()
        buy_something()

    cps = driver.find_element(By.ID, "cps")
    print(cps.text)

driver.quit()  # closes the browser session - inc. all tabs
