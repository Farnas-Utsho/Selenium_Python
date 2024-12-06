#This file will include a class with instance methods
#That will be responsible to interact with our website
#After we have some results , to apply to filtration
from dask.multiprocessing import exceptions
from lxml.etree import XPath
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # def apply_star_rating(self, star_value):
    #     # Wait for the star filtration box to be visible before interacting with it
    #     try:
    #         star_filtration_box = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-testid='filters-group']"))
    #         )
    #         print(len(star_filtration_box))
    #         print("Target element found")
    #         elements_count = len(self.driver.find_elements(By.CSS_SELECTOR, "div[data-testid='filters-group']"))
    #         for i in range(elements_count):
    #
    #                 element = self.driver.find_elements(By.CSS_SELECTOR, "div[data-testid='filters-group']")[i]
    #                 div_id = element.get_attribute("id")
    #                 print(f"Div ID: {div_id}")
    #
    #     except Exception as e:
    #         print(f"Error occurred: {e}")

    def match_filtration(self):
        print("Property Ratings Execution Started")
        try:
            # Wait for the elements to be present
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-testid='filters-group']"))
            )
            print("Target elements found")


            targets = self.driver.find_elements(By.CSS_SELECTOR, "div[data-testid='filters-group']")

            for target in targets :
                try:
                    legend = target.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div[1]/div[3]/div[9]/fieldset/div[3]/legend')

                    title = legend.get_attribute('innerText')
                    print(f"Title: {title}")
                    


                except Exception as e:
                    print(f"Error occurred: {e}")






        except Exception as e:
            print(f"Error occurred: {e}")
















