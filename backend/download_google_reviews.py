import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,WebDriverException,TimeoutException
from datetime import datetime
from dateutil.relativedelta import relativedelta


class GetGoogleReviews:
    def __init__(self, url:str):

        self.donwload_google_reviews(url)

    def donwload_google_reviews(self, url:str):

        def time_converter(date: str):

            current_time = datetime.now()
            date = date.split(' ')[1:]

            if  'un'  in date or 'una' in  date:
                date[0] = 1
            else:
                date[0]=int(date[0])

            if date[1] == 'día' or date[1] == 'días':
                relative_time = relativedelta(days=date[0])
            if date[1] == 'mes' or date[1] == 'meses':
                relative_time = relativedelta(months=date[0])
            if date[1] == 'semana' or date[1] == 'semanas':
                relative_time = relativedelta(weeks=date[0])
            if date[1] == 'año' or date[1] == 'años':
                relative_time = relativedelta(years=date[0])

            new_time = current_time - relative_time
            formatted_date = new_time.strftime("%Y-%m-%d")

            return formatted_date

        def get_data(driver):

            count=1
            print('getting data... please wait')
            more_elements = driver.find_elements(By.CLASS_NAME, 'w8nwRe.kyuRq')

            for list_more_element in more_elements:
                list_more_element.click()

            elements = driver.find_elements(By.CLASS_NAME,'jftiEf')

            lst_data = [ ]

            for data in elements:

                try:
                    #name = data.find_element(By.CLASS_NAME, 'd4r55 ').text
                    user = f'user_{count}'
                    text = data.find_element(By.CLASS_NAME, 'wiI7pd').text
                    time=data.find_element(By.CLASS_NAME,'rsqaWe').text
                    date = time_converter(time)
                    score = data.find_element(By.CLASS_NAME,'kvMYJc').get_attribute("aria-label")

                except NoSuchElementException:
                    text = "Text Null"

                lst_data.append([user, text, time, date, score]) # name

                #print(len(lst_data),' row is generated')

                count+=1

            return lst_data

        def count_reviews(title):

            result = driver.find_element(By.CLASS_NAME,'jANrlb').text
            rating = result[:3]
            result = result.split('\n')[1].split(' ')
            result =  result[0]

            print(f'{title} has {rating} and {result} reviews')

            if '.' in result:
                result = int(result.replace('.', ''))
                if result >= 2500:
                    print("Too many reviews to scroll... fetched to 200 scroll down") # each scroll down takes 2 sec to wait comments to appear
                    result = 200
                    return result
            return int((result / 10) + 1)

            return int(int(result) / 10) + 1

        def scrolling(counter):

            print('scrolling over the reviews...')
            time.sleep(2)
            scrollable_div = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[11]/div')

            for _i in range(counter):
                #time.sleep(2)
                try:
                    scrolling = driver.execute_script(
                        'document.getElementsByClassName("dS8AEf")[0].scrollTop = document.getElementsByClassName("dS8AEf")[0].scrollHeight',
                        scrollable_div, time.sleep(2))

                except WebDriverException:

                    print('stop scrolling... ')
                    return

            print("scrolling was complete")

            # Scroll up
            driver.execute_script('document.getElementsByClassName("dS8AEf")[0].scrollTop = 0')

        def write_to_csv(data, tittle):

            print('Writing to csv...')
            cols = ['user_id', 'comment', 'time', 'date', 'rating']
            df = pd.DataFrame(data, columns=cols)
            
            df.to_csv('data.csv')

            print("Your csv was successfully created!")

        print('starting...')

        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--headless")  # show browser or not
        chrome_options.add_argument("--lang=en-US")
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)

        driver.get(url)

        try:
            button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div/div/button/span'))
            )
            button.click()

        except TimeoutException:
            print("The button was not found within the expected time.")

        header = driver.find_element(By.CLASS_NAME,'DUwDvf').text

        try:
            reviews_tab = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@role="tab" and .//div[text()="Reseñas"]]'))
            )
            reviews_tab.click()

        except TimeoutException:
            print("No reviews was found")

        counter = count_reviews(header)
        scrolling(5)

        data = get_data(driver)
        driver.close()

        write_to_csv(data, header)


