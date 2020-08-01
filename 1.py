from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from configparser import ConfigParser
a_init = time.time()
CONFIG = ConfigParser()
CONFIG.read('config.ini')

driver_path = CONFIG.get('MAIN', 'DRIVER_LOCATION')
email_inp = CONFIG.get('CREDENTIALS', 'USERNAME')
pass_inp = CONFIG.get('CREDENTIALS', 'PASSWORD')
# cvv_inp = CONFIG.get('ORDER', 'CVV')
addr_input = CONFIG.get('ORDER', 'ADDRESS')
PIN_input = CONFIG.get('ORDER', 'PIN')

# pay_opt_input = CONFIG.get('ORDER', 'PAYMENT')
#
# bankname_input = CONFIG.get('EMIOPTIONS', 'BANK')
# tenure_input = CONFIG.get('EMIOPTIONS', 'TENURE')

url = CONFIG.get('ORDER', 'URL')

print('\nLogging in with username:', email_inp)

driver = webdriver.Chrome(driver_path)
driver.set_window_size(800, 600)
driver.get(url)

print('\nConfirmed Details & Press Enter to proceed!')


def login():
    try:
        print("Logging In..")
        try:
            login = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "._34niwY"))
            )
            print('Login Button Clickable')
        except:
            print('Login Button Not Clickable')
        login.click()
        print('Login Button Clicked Successfully')
    except:
        print('login Failed. Retrying.')
        time.sleep(0.5)
        login()


def login_submit():
    try:
        if 'Enter Password' in driver.page_source:
            print('Trying Usual method of Login.')
            email = driver.find_element_by_css_selector(".Km0IJL ._2zrpKA")
            passd = driver.find_element_by_css_selector(".Km0IJL ._3v41xv")
            email.clear()
            passd.clear()
            email.send_keys(email_inp)
            passd.send_keys(pass_inp)
            try:
                form = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, ".Km0IJL ._7UHT_c"))
                )
                print('Submit Button Clickable')
            except:
                print('Submit Button Not Clickable')
            form.click()
        else:
            print('Trying Alternate method of Login.')
            email = driver.find_element_by_css_selector("._2zrpKA")
            email.clear()
            email.send_keys(email_inp)
            loginnext = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "._1LctnI"))
            )
            loginnext.click()
            loginpassword = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".jUwFiZ"))
            )
            loginpassword.click()
            time.sleep(0.5)
            passd = driver.find_elements_by_css_selector("._2zrpKA")[1]
            passd.clear()
            passd.send_keys(pass_inp)
            form = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "._1LctnI"))
            )
            form.click()
        print("Logged In Successfully")
    except:
        if ('Login &amp; Signup' not in driver.page_source and 'Login & Signup' not in driver.page_source):
            print('Logged in Manually.')
        else:
            print('login_submit Failed. Please login manually.')
            time.sleep(1)
            login_submit()


def buy_check():
    try:
        nobuyoption = True
        pin_field = driver.find_element_by_id('pincodeInputId')
        pin_field.clear()
        pin_field.send_keys(PIN_input)
        pin_check_button = driver.find_element_by_css_selector('._2aK_gu')
        pin_check_button.click()
        time.sleep(0.5)
        print("PIN CHECK DONE")
        while nobuyoption:
            try:
                driver.refresh()
                time.sleep(0.2)
                buyprod = driver.find_element_by_css_selector(
                    "._1k1QCg ._7UHT_c")
                print('Buy Button Clickable: ' + time.ctime())
                nobuyoption = False
            except:
                nobuyoption = True
                print('Buy Button Not Clickable: ' + time.ctime())
        buyprod.click()
        print('Buy Button Clicked Successfully: ' + time.ctime())
        buy_recheck()
    except:
        print('buy_check Failed. Retrying: ' + time.ctime())
        time.sleep(0.5)
        buy_check()


def buy_recheck():
    try:
        WebDriverWait(driver, 4).until(
            EC.title_contains("Secure Payment")
        )
        print('Redirected to Payment')
    except:
        print('Error in Redirecting to Payment')
        time.sleep(0.5)
        buy_check()


def deliver_option():
    try:
        addr_input_final = "//label[@for='"+addr_input+"']"
        try:
            sel_addr = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, addr_input_final))
            )
            print('Address Selection Button Clickable')
        except:
            print('Address Selection Button Not Clickable')
        sel_addr.click()
        print('Address Selection Button Clicked Successfully')
    except:
        print('deliver_option Failed. Retrying.')


def deliver_continue():
    try:
        addr_sal_avl = True
        while addr_sal_avl:
            try:
                address_sel = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "._3K1hJZ ._7UHT_c"))
                )
                address_sel.click()
                addr_sal_avl = False
                print('Address Delivery Button Clickable')
            except:
                addr_sal_avl = True
                print('Address Delivery Button Not Clickable')
        print('Address Delivery Button Clicked Successfully')
    except:
        print('deliver_continue Failed. Retrying.')


def order_summary_continue():
    try:
        press_continue = driver.find_element_by_css_selector("._2Q4i61")
        press_continue.click()
        print('Continue Button Clicked Successfully')
    except:
        print('order_summary_continue Failed. Retrying.')
        time.sleep(0.5)
        order_summary_continue()


def select_cod():
    try:
        press_COD = driver.find_element_by_css_selector("._34nCiT")
        press_COD.click()
        print("COD selected successfully")
        """ 
        # capt = driver.find_elements_by_class_name("AVMILy")
        capt = driver.find_element_by_xpath(
            '//div[@class="_3931C8"]/img')
        add = capt.get_attribute('src')
        urllib.request.urlretrieve(add, 'captcha.jpeg')

        img = Image.open('captcha.jpeg')
        img.show() """
        print(time.time()-a_init)
        OTP = input("Enter Captcha:")
        otp_box = driver.find_element_by_css_selector("._16qL6K._366U7Q")
        otp_box.clear()
        otp_box.send_keys(OTP)
        submit_COD = driver.find_element_by_css_selector("._23FrK1")
        submit_COD.click()
    except:
        print('Unable to select COD, retrying!')
        select_cod()


def run_script():
    login()
    login_submit()
    time.sleep(0.5)
    buy_check()
    order_summary_continue()
    select_cod()


if __name__ == "__main__":
    run_script()
