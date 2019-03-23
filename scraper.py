from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options


options = Options()
options.headless = True

driver = webdriver.Chrome(chrome_options=options)


url = 'https://www.amazon.es/Quimat-Pantalla-Raspberry-Protectiva-Disipadores/dp/B06W55HBTX/ref=pd_rhf_ee_s_pd_crcd_0_3/260-4071437-3846962?_encoding=UTF8&pd_rd_i=B06W55HBTX&pd_rd_r=db785bde-02bd-4dce-8abd-b6b47bd1caaa&pd_rd_w=smLre&pd_rd_wg=CSHiy&pf_rd_p=76e1f2b8-0692-47af-bb36-251bb7a6a038&pf_rd_r=NN3YXYSMHMQ6H415CEAH&psc=1&refRID=NN3YXYSMHMQ6H415CEAH'

driver.get(url)

el = driver.find_element_by_id('priceblock_ourprice')

print(el.text)

