from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from configparser import ConfigParser

CONFIG = ConfigParser()
CONFIG.read('config.ini')

driver_path = CONFIG.get('MAIN', 'DRIVER_LOCATION')
email_inp = CONFIG.get('CREDENTIALS', 'USERNAME')
pass_inp = CONFIG.get('CREDENTIALS', 'PASSWORD')
url = CONFIG.get('ORDER', 'URL')

print('\nLogging in with username:', email_inp)

driver = webdriver.Chrome(driver_path)
driver.minimize_window()
driver.get(url)

print('\nConfirmed Details!')


def login():
    try:
        print("Logging In..")
        try:
            login = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "._34niwY"))
            )
            print('Login Button Found')
        except:
            print('Login Button Not Found')
        login.click()
        print('Login Button Clicked Successfully')
    except:
        print('Unable to login. Retrying.')
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
                print('Submit Button Found')
            except:
                print('Submit Button Not Found')
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
        while nobuyoption:
            try:
                driver.refresh()
                time.sleep(0.2)
                buyprod = driver.find_element_by_css_selector(
                    "._1k1QCg ._7UHT_c")
                print('Buy Button Found: ' + time.ctime())
                nobuyoption = False
            except:
                nobuyoption = True
                print('Buy Button Not Found: ' + time.ctime())
        buyprod.click()
        print('Buy Button Clicked Successfully: ' + time.ctime())
        buy_recheck()
    except:
        print('Buy button Failed. Retrying: ' + time.ctime())
        time.sleep(0.5)
        buy_check()


def buy_recheck():
    try:
        WebDriverWait(driver, 4).until(
            EC.title_contains("Secure Payment")
        )
        print('Redirected to Payment portal')
    except:
        print('Error in Redirecting to Payment page')
        time.sleep(0.5)
        buy_check()

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
        Captcha = input("Enter Captcha:")
        Captcha_box = driver.find_element_by_css_selector("._16qL6K._366U7Q")
        Captcha_box.clear()
        Captcha_box.send_keys(Captcha)
        submit_COD = driver.find_element_by_css_selector("._23FrK1")
        submit_COD.click()
    except:
        print('Unable to select COD, retrying!')
        select_cod()


def run_script():
    start = time.time()
    print("Start time: {0}".format(start))
    login()
    login_submit()
    buy_check()
    order_summary_continue()
    print("Choosing COD option for payment.")
    select_cod()
    end = time.time()
    total = end - start
    print("Total time taken: {0}".format(total))


if __name__ == "__main__":
    run_script()
