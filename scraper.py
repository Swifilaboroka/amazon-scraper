from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import smtplib

chrome_options = Options()
chrome_options.add_argument("--headless")


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chrome_options)
url = 'https://www.amazon.de/Crucial-MX500-CT500MX500SSD1-Internes-NAND/dp/B0784SLQM6/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ssd+500gb&qid=1597833560&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFYOUVGUTYyTTJEQkEmZW5jcnlwdGVkSWQ9QTAxMzM2OTYyUlk4UE9YWjhKT1daJmVuY3J5cHRlZEFkSWQ9QTA1Mjk1MzczUTJPNDdIWlZWS1ZIJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
driver.get(url)


def check_price():
    price = driver.find_element_by_id("priceblock_ourprice").text

    converted_price = float(price[0:2])
    
    if(converted_price < 50):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('testpy3299@gmail.com', 'Testtest123!')

    subject = 'Preis ist gefallen!'
    body = url

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'testpy3299@gmail.com',
        'herwigbuche@gmail.com',
        msg
    )
    print('E-mail wurde gesendet.')
    server.quit()



while(True):
    check_price()
    time.sleep(86400)