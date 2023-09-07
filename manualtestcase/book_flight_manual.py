import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# from webdriver_manager.chrome import ChromeDriverManager

##deah less run
vid_1 = "body > ytd-app:nth-child(16) > div:nth-child(7) > ytd-page-manager:nth-child(4) > ytd-browse:nth-child(3) > ytd-two-column-browse-results-renderer:nth-child(9) > div:nth-child(1) > ytd-section-list-renderer:nth-child(1) > div:nth-child(2) > ytd-item-section-renderer:nth-child(2) > div:nth-child(3) > ytd-shelf-renderer:nth-child(1) > div:nth-child(1) > div:nth-child(2) > yt-horizontal-list-renderer:nth-child(1) > div:nth-child(2) > div:nth-child(1) > ytd-grid-video-renderer:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(2)"
options = Options()
options.headless = False

##inialize webdriver
# driver = webdriver.Edge()
driver = webdriver.Chrome(options=options)
## driver.get() to get in to mentioned urll
driver.get("https://www.youtube.com/@tseries")
driver.maximize_window()


##wait
wait = WebDriverWait(driver, 20)
driver.execute_script("window.scrollTo(0, 300)")


wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[1]/div/div/button/span"))).click()
driver.execute_script("window.scrollTo(0, 400)")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,vid_1))).click()
time.sleep(1000)
driver.close()

# ##accept cookies
# accept_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[data-ref='cookie.accept-all']")))
# accept_button.click()
# ## departure_place
# departure_from = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='input-button__departure']")))
# departure_from.click()
# departure_country = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Ireland']")))
# departure_country.click()
# departure_airport = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Shannon')]")))
# departure_airport.click()
#
#
# ##desitination place
# arrival_country = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='United Kingdom']")))
# arrival_country.click()
# arrival_airport = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Manchester')]")))
# arrival_airport.click()
#
# ## departure date
#
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR,"div[data-id='2023-07-23']").click()
# #departure_date = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".calendar-body__cell[tabindex='0'][data-id='2023-07-31']")))
# #departure_date.click()
# ## arival date
# arrival_date = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[data-id='2023-08-01']")))
# arrival_date.click()
#
# ##select number of passengers
# passrenger_count = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label='Done']")))
# passrenger_count.click()
#
# ##click search
# wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label='Search']"))).click()
# time.sleep(10)
#
# ##scroll to contact us
# elem = driver.find_element(By.CSS_SELECTOR,"a[href='https://www.ryanair.com/ie/en/r/help/contact-us']")
# driver.execute_script("arguments[0].scrollIntoView();", elem)
# time.sleep(4)
# ##click on contact us
# elem.click()
#
# ## page details
# # time.sleep(10)
# # print(driver.find_element(By.CSS_SELECTOR,"h1[class='h2 mt-6 mb-5']").text)
# ##contact = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a[href='/hc/en-ie']")))
# ##print(contact.text)
#
