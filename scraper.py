from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
import os

CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')


options = Options()
options.binary_location = GOOGLE_CHROME_BIN
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.headless = True

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH , chrome_options=options)


url = 'https://www.amazon.es/Quimat-Pantalla-Raspberry-Protectiva-Disipadores/dp/B06W55HBTX/ref=pd_rhf_ee_s_pd_crcd_0_3/260-4071437-3846962?_encoding=UTF8&pd_rd_i=B06W55HBTX&pd_rd_r=db785bde-02bd-4dce-8abd-b6b47bd1caaa&pd_rd_w=smLre&pd_rd_wg=CSHiy&pf_rd_p=76e1f2b8-0692-47af-bb36-251bb7a6a038&pf_rd_r=NN3YXYSMHMQ6H415CEAH&psc=1&refRID=NN3YXYSMHMQ6H415CEAH'

driver.get(url)

el = driver.find_element_by_id('priceblock_ourprice')

print(el.text)

