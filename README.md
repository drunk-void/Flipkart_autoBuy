# Flipkart_autobuy

### An interactive web-crawler for the website of Flipkart to automate the process of buying any products with multiple payment options. Specially for the products listed on flash-sale getting "Sold Out" in fraction of seconds.

Steps to run this script:
1. Clone or download this repository `git clone https://github.com/mchandolia/Flipkart_autoBuy.git`
2. Run `cd Flipkart_autoBuy`
3. Run `python3 -m venv Scripvenv`
`source Scripvenv/bin/activate`
4. Run `pip install -r requirements.txt`
    *for installing the required libraries in your python environment*
5. Download the correct [chromedriver](http://chromedriver.chromium.org/downloads) for your operating system (Linux/OSX/Windows), put the chromedriver in this project directory.
6. Set path of chromedriver in config.ini file. *Default: `./chromedriver` if driver is in project directory*
7. Enter your email and password in config.ini file.
8. Enter flipkart product URL in config.ini file.
9. Enter your saved card CVV in config.ini file. *Required only if you want to choose card payment*
7. Run `python script.py`

Note:
Make sure you have only one address in your flipkart account and only one card saved. Remove all extra credit and debit cards from Flipkart and PhonePe account.