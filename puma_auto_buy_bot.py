from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium. webdriver. common. keys import Keys
import time

PATH = r'C:\Users\jonas\OneDrive\online_buy_bot\chromedriver.exe'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
wd = webdriver.Chrome(PATH)
website = "https://eu.puma.com/ch/de/pd/puma-smash-v2-l/4059505055387.html"

shopping_cart = "https://eu.puma.com/ch/de/cart"

checkout = "https://eu.puma.com/ch/de/checkout/start?stage=shipping#shipping"

log_in = "https://eu.puma.com/ch/de/account/login"

instock = False

#Personal Data
email_adress = "jonastibisch@gmail.com"
email_password = "password"







wd.get(log_in)

time.sleep(1)

accept_cookies_button = wd.find_element(By.ID, "onetrust-accept-btn-handler")
accept_cookies_button.click()

email_adress_input = wd.find_element(By.ID, "login-form-email")
for letter in email_adress:
    time.sleep(0.2)
    email_adress_input.send_keys(letter)


time.sleep(1)


email_password_input = wd.find_element(By.ID, "login-form-password")
for letter in email_password:
    time.sleep(0.2)
    email_password_input.send_keys(letter)

pop_up_close = wd.find_element(By.XPATH, '//*[@id="wps_popup"]/div/div[1]')
pop_up_close.click()

time.sleep(1)
login_remember = wd.find_element(By.ID, "loginRememberMe")
login_remember.click()

login_button = wd.find_element(By.XPATH, '//*[@id="login"]/form/div[5]/button')
login_button.click()


time.sleep(2)
wd.get(website)


while instock == False:
    try:
        size_button = wd.find_element(By.ID, "swatch-0210")
    except:
        try:
            size_button = wd.find_element(By.ID)
        except:
            wd.refresh()
            time.sleep(5)

        else: 
            instock = True

        

    else:
        instock = True

size_button.click()

time.sleep(2)


add_to_cart = wd.find_element(By.XPATH, '//*[@id="page"]/div[2]/div[3]/div[1]/div[2]/div/div[11]/div/div[2]/button')
add_to_cart.click()

time.sleep(5)


wd.get(checkout)

time.sleep(5)
"""
adress_book = wd.find_element(By.XPATH, '//*[@id="dwfrm_shipping"]/fieldset[1]/div/div/div/div[1]/div[1]/select')
adress_book.click()
adress_selection = wd.find_element(By.XPATH,'//*[@id="dwfrm_shipping"]/fieldset[1]/div/div/div/div[1]/div[1]/select/option[3]')
adress_selection.click()
"""
time.sleep(1)

payment = wd.find_element(By.XPATH, '//*[@id="shipping-address"]/div/div/button')
payment.click()

time.sleep(10)

select_payment_method = wd.find_element(By.ID, "paymentOption-PAYMENTOPERATOR_CREDIT_PAYNOW")
select_payment_method.click()

select_payment_method = wd.find_element(By.XPATH, '/html/body/div[5]/div[4]/div/div[1]/div[5]/div[2]/div[4]/div/form/fieldset[1]/div[3]/div/label/div[1]/input')
select_payment_method.click()

time.sleep(10)








"""
SIZE = 40

instock = False


while not instock:
    
    try:
        size_button = wd.find_element('//*[@id="swatch-0210"]')
        add_to_cart = wd.find_element_by_xpath('//*[@id="page"]/div[2]/div[3]/div[1]/div[2]/div/div[11]/div/div[2]/button')
        
        
    except:
        print("Not in stock yet")
        time.sleep(1)
        wd.refresh()
    else:
        add_to_cart.click()
        time.sleep(1000)
        instock = True
        checkout = wd.find_element_by_xpath('//*[@id="addToBagOverlay"]/div/div/div/div/div[3]/div[2]/a')
        checkout.click()
"""