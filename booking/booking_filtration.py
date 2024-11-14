#This file will include a class with instance methods
#That will be responsible to interact with our website
#After we have some results , to apply to filtration
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, star_value):
        # Wait for the star filtration box to be visible before interacting with it
        try:
            star_filtration_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.ffb9c3d6a3:nth-child(3)"))
            )

            # Find all child elements (stars) within the star_filtration_box
            star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')
            print(len(star_child_elements))
            for star_element in star_child_elements:
                try:
                    # Wait until the element is clickable before clicking it
                    WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable(star_element)
                    )

                    # Check if the innerHTML matches the desired star value and click if so
                    if str(star_element.get_attribute('innerHTML')).strip() == f"{star_value} stars":
                        star_element.click()
                        break  # Exit the loop after applying the filter
                except StaleElementReferenceException:
                    # If the element becomes stale, retry by re-fetching the element
                    star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')
                    continue

        except Exception as e:
            print(f"Error occurred while applying star rating filter: {e}")
