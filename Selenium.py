from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import requests
import json

def enterDOB():
    month = driver.find_element_by_name("MM")
    month.send_keys("01","01","1990", Keys.TAB, Keys.ENTER)

def checkAvilablity():
    r = requests.get('https://450northbeerrelease.com/products.json')
    # Load websites product data
    products = json.loads((r.text))['products']
    # Check if those products match users product
    for product in products:
        print(product['title'])
        productname = product['title']
        if user['DrinkNames'][0] in productname:
            return True
    return False

def refresh():
    driver.get("https://450northbeerrelease.com/")
    driver.refresh()

def purchaseBeer():
    drinksToBuy = user['DrinkNames']
    drinkQtys = user['DrinkQuanity']
    #Navigate to all of the user's products
    #Add them to the cart
    for i in range( len (drinksToBuy) ):
        navigateTo(drinksToBuy[i])
        addToCart(drinkQtys[i])        

def navigateTo(drink):
    r = requests.get('https://450northbeerrelease.com/products.json')
    # Loads website's product data
    products = json.loads((r.text))['products']
    
    # Check if website's products matches user's product
    # Then gets the url handle for the product and then navigate to that product
    for product in products:
        productname = product['title']
        if drink in productname:
            handle = product['handle']
            driver.get('https://450northbeerrelease.com/products/'+ handle)

def addToCart(drinkQty):
   qtyField = driver.find_element_by_id("Quantity-product-template")
   qtyField.send_keys(Keys.DELETE, drinkQty, Keys.TAB, Keys.ENTER)
   
def goToCart():
    driver.get("https://450northbeerrelease.com/cart")
    time.sleep(1)

def checkOut():
    pass

#Get user info
with open('./info.json') as jsonFile: user = json.load(jsonFile)
#Start driver
driver = webdriver.Chrome("./chromedriver")
#Start Site
driver.get("https://450northbeerrelease.com/")
time.sleep(1)
# DOB Check
enterDOB()
# Check if product is live
while checkAvilablity() == False:
        refresh()
        checkAvilablity()
# If product is live then add all the user's products to the cart 
# and checkout
purchaseBeer()
goToCart()
#checkOut()