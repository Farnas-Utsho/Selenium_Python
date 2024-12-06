
from selenium import webdriver
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from booking.booking_filtration import  BookingFiltration


import booking.constants as const

class Booking(webdriver.Firefox):
    def __init__(self, driver_path=r"D:\Selenium\geckodriver.exe", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['Path'] += os.pathsep + self.driver_path
        super(Booking, self).__init__()

        # Set implicit wait and maximize window
        self.implicitly_wait(30)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()  # Quit the browser session

    def land_first_page(self):
        self.get(const.Base_URL)  # Ensure Base_URL is correctly set in booking.constants

    def close_pop(self):
        try:
            # Wait for the button or a higher-level clickable element, not the SVG path svg.Bz112c:nth-child(2)
            popup = WebDriverWait(self, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.f4552b6561'))
            )
            popup.click()
            print("Intro pop up closed")
        except Exception as e:
            print(f"Error closing the popup: {e}")\


    #Closing google pop up for sign in
    def close_google_signup_popup(self):
        try:
            # Step 1: Wait for the iframe to be available and switch to it
            iframe = WebDriverWait(self, 10).until(
                EC.frame_to_be_available_and_switch_to_it(
                    (By.XPATH, "//iframe[contains(@src, 'https://accounts.google.com/')]"))
            )

            # Step 2: Locate the close button inside the iframe using CSS selector
            close_button = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "svg.Bz112c:nth-child(2)"))
            )

            # Step 3: Click the close button
            close_button.click()
            print("Google sign-up popup closed.")

            # Step 4: Switch back to the main content
            self.switch_to.default_content()

        except Exception as e:
            print(f"Error closing Google sign-up popup: {e}")
            # Ensure we return to the main content in case of an exception
            self.switch_to.default_content()

    #Click Currency
    def choose_currency(self):
        currency_select=self.find_element(By.XPATH,
                                         '/html/body/div[2]'
                                         '/div/div/header/div/'
                                         'nav[1]/div[2]/span[1]/'
                                         'button/span' )
        # currency_select=self.find_element(By.CSS_SELECTOR,
        #                                   'button[data-bui-theme="traveller_ex-light"]')
        currency_select.click()
        print("Currency button clicked")
        currency_dollar = self.find_element(By.CSS_SELECTOR,
                                            '.f7c2c6294c > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > button:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
        currency_dollar.click()
        print(" Dollar selected ")

    def select_place_to_go(self,place_to_go):
        search_field=self.find_element(By.ID,':rh:')
        search_field.clear()
        search_field.send_keys(place_to_go)
        print(f'{place_to_go}')
        first_place = WebDriverWait(self, 30).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'li[id="autocomplete-result-0"]'), place_to_go)
        )
        # Find and click the first result element
        first_result_element = self.find_element(By.CSS_SELECTOR, 'li[id="autocomplete-result-0"]')
        first_result_element.click()
        print(f"Selected: {place_to_go}")

    # def select_dates(self , check_in_date,check_out_date):
    #
    #     xpath = "//span[@data-date]"
    #     in_date=WebDriverWait( self,20).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
    #     # Extract the dates from each <span> element's data-date attribute
    #     for element in in_date:
    #         date_value = element.get_attribute("data-date")
    #
    #         # Print the collected date
    #         print("Collected Date:", date_value)
    #
    #         # Check if the current date matches the desired check-in date
    #         if date_value == check_in_date:
    #             # Click the element with the matching date
    #             element.click()
    #             print(f"Clicked on date: {check_in_date}")
    #             break
    #         else:
    #           print(f"Date {check_in_date} not found.")
    #         #Check out Date selection
    #         check_out_found =False
    #         while not check_out_found :
    #             xpath = "//span[@data-date]"
    #             out_date = WebDriverWait(self, 20).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
    #             for element in out_date:
    #                 out_dates = element.get_attribute("data-date")
    #                 if out_dates == check_out_date :
    #                     element.click()
    #                     print(" Check out date found ")
    #                     check_out_found=True
    #                     break
    #                 else :
    #                     next_page=self.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/form/div'
    #                                                                '/div[2]/div/div[2]/div/nav/div[2]/div/div[1]'
    #                                                                '/button/span/span/svg/path')
    #                     next_page.click()

    def select_dates(self, check_in_date, check_out_date):
        # Wait for all available dates to load
        xpath = "//span[@data-date]"
        next="/html/body/div[3]/div[2]/div/form/div/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/button[2]/span/span/svg"

        # Wait for check-in date to be present and select it
        in_date = WebDriverWait(self, 20).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        check_in_found = False

        # Loop to find the check-in date
        for element in in_date:
            date_value = element.get_attribute("data-date")
           # print("Collected Date:", date_value)

            if date_value == check_in_date:
                element.click()
                print(f"Clicked on check-in date: {check_in_date}")
                check_in_found = True
                break

        if not check_in_found:
            print(f"Check-in date {check_in_date} not found.")
            return  # Exit the function if the check-in date isn't found

        # Wait for check-out date to be present and select it
        check_out_found = False

        while not check_out_found:
            out_date = WebDriverWait(self, 20).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

            # Loop to find the check-out date
            for element in out_date:
                out_dates = element.get_attribute("data-date")

                if out_dates == check_out_date:
                    element.click()
                    print(f"Clicked on check-out date: {check_out_date}")
                    check_out_found = True
                    break

            if not check_out_found:
                print(f"Check-out date {check_out_date} not found. Trying to go to the next page.")

                # Find the "next page" button and click it
                # XPath you provided to locate the "next page" button
                next_page_css_selector= '#calendar-searchboxdatepicker > div > div.a10b0e2d13.c807ff2d48 > button > span > span > svg'
                print(" Element Found ")

                # Wait for the "next page" button to be clickable and click it
                next_page = WebDriverWait(self, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, next_page_css_selector))  # The correct way to pass the locator
                )
                next_page.click()

                # Optionally, you can add a delay here to allow the page to load new dates, if necessary
                WebDriverWait(self, 5).until(
                    EC.presence_of_all_elements_located((By.XPATH, xpath))  # Wait for new dates to load
                )



    def number_persons_room(self,adults):


        try:
            adder=WebDriverWait(self,20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'.c7ce171153'))
            )
            adder.click()
            print(" Adder Found ")

            adult_decrease=WebDriverWait(self,20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,"div.a7a72174b8:nth-child(1) > div:nth-child(3) > button:nth-child(1)"))
            )
            for _ in range(1):
                adult_decrease.click()
                print("Adult decreased")




            adder = WebDriverWait(self, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.c7ce171153'))
            )
            adder.click()
            print(" Adder Found ")
            adult_increase=WebDriverWait(self,10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,"div.a7a72174b8:nth-child(1) > div:nth-child(3) > button:nth-child(3)"))
            )
            print("Adult  element Found ")
            for _ in range(adults-1) :
                adult_increase.click()

            # Use JavaScript to ensure any aria-hidden or clickability issues are bypassed


            print("Adult added")

        except Exception as e:
            print("An error occurred:", e)

    def search_item(self):
        try:
         search_it=WebDriverWait(self,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'button.a4c1805887'))
            )
         search_it.click()
        except Exception as e:
            print(" An error occurred : " , e )



    def apply_filtrations(self):

       filtration= BookingFiltration(driver=self)
       # filtration.apply_star_rating(star_value = 5)
       filtration.match_filtration()























