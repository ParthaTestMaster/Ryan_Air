import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.utils import Utils
from base.base_driver import BaseDriver


class homepage(BaseDriver):
    log = Utils.cutom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    accept_cookies_button = "button[data-ref='cookie.accept-all']"
    departure_text_box_filed = "//input[@id='input-button__departure']"
    adult_button = "ry-counter[data-ref='passengers-picker__adults']>div[class='counter']>div[data-ref='counter.counter__increment']"
    teen_button = "ry-counter[data-ref='passengers-picker__teens']>div[class='counter']>div[data-ref='counter.counter__increment']"
    children_button = "ry-counter[data-ref='passengers-picker__children']>div[class='counter']>div[data-ref='counter.counter__increment']"
    done = "//button[contains(text(),'Done')]"
    search_button = "//button[@aria-label='Search']"



    def accept_cookies(self):
        accept_button = self.wait_until_element_is_clickable(By.CSS_SELECTOR, self.accept_cookies_button)
        accept_button.click()

    def locator_generoator(self, country_from, city_from, country_to, city_to, departure_date, arrival_date, adults,
                           teens, children):
        ### make all vriable global, so can be used any subsequent fuctions
        global country_from_1, city_from_1, country_to_1, city_to_1, departure_date_1, arrival_date_1, adults_1, teens_1, children_1
        country_from_1 = country_from
        city_from_1 = city_from
        country_to_1 = country_to
        city_to_1 = city_to
        # departure_date_1 = departure_date
        # arrival_date_1 = arrival_date
        adults_1 = adults
        teens_1 = teens
        children_1 = children

        global from_country_loc, from_city_loc, country_to_loc, city_to_loc
        from_country_loc = "//span[normalize-space()='" + country_from + "']"
        from_city_loc = "//span[normalize-space()='" + city_from + "']"
        country_to_loc = "//span[normalize-space()='" + country_to + "']"
        city_to_loc = "//span[normalize-space()='" + city_to + "']"
        global departure_dates_loc, arrival_dates_loc,departure_dates_1, arrival_dates_1
        departure_dates_1 = str(departure_date).strip(" 00:00:00")
        arrival_dates_1 = str(arrival_date).strip(" 00:00:00")
        departure_dates_loc = "div[data-id='" + departure_dates_1 + "']"
        arrival_dates_loc = "div[data-id='" + arrival_dates_1 + "']"

    def click_on_departure_text_box(self):
        self.wait_until_element_is_clickable(By.XPATH, self.departure_text_box_filed).click()

    def from_place(self):
        self.wait_until_element_is_clickable(By.XPATH, from_country_loc).click()
        self.wait_until_element_is_clickable(By.XPATH, from_city_loc).click()
        self.log.info("Departing from %s - %s" % (country_from_1, city_from_1))

    def to_place(self):
        self.wait_until_element_is_clickable(By.XPATH, country_to_loc).click()
        self.wait_until_element_is_clickable(By.XPATH, city_to_loc).click()
        self.log.info("Arriving to %s - %s" % (country_to_1, city_to_1))

    def departure_datz(self):
        self.wait_until_element_is_clickable(By.CSS_SELECTOR, departure_dates_loc).click()
        self.log.info("Departure date %s" % departure_dates_1)


    def arrival_datz(self):
        self.wait_until_element_is_clickable(By.CSS_SELECTOR, departure_dates_loc).click()
        self.log.info("Arrival date %s" % arrival_dates_1)

    def adult_count_change(self):
        for i in range(adults_1-1):
            self.wait_until_element_is_clickable(By.CSS_SELECTOR, self.adult_button).click()

    def teens_count_change(self):
        for i in range(teens_1):
            self.wait_until_element_is_clickable(By.CSS_SELECTOR, self.teen_button).click()

    def children_count_change(self):
        for i in range(children_1):
            self.wait_until_element_is_clickable(By.CSS_SELECTOR, self.children_button).click()

    def add_total_persons(self):
        self.log.info("Adults:%s  , Teens:%s , Children:%s" %(adults_1,teens_1,children_1))
        self.adult_count_change()
        self.teens_count_change()
        self.children_count_change()
        self.wait_until_element_is_clickable(By.XPATH, self.done).click()
        self.log.info("-----------------------*-----------------------------")

    def click_on_search_button(self):
        self.wait_until_element_is_clickable(By.XPATH,self.search_button)
    def country_city_select(self):
        self.accept_cookies()
        self.click_on_departure_text_box()
        self.from_place()
        self.to_place()
        self.departure_datz()
        self.arrival_datz()
        self.add_total_persons()
        self.click_on_search_button()
