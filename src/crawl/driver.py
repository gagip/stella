from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DriverManager():

    def __init__(self, base_url: str, hidden_browser_option: bool = False):
        driver_option = webdriver.ChromeOptions()
        driver_option.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        # 창 숨기는 옵션
        if hidden_browser_option:
            self.options.add_argument("headless")
        self.driver = webdriver.Chrome(options=driver_option)
        self.driver.get(base_url)

    def move_to(self, url: str, wait_time=3):
        self.driver.get(url)
        self.driver.implicitly_wait(wait_time)
        
    def find_element_by_id(self, id: str):
        return self.driver.find_element(By.ID, id)
    
    def get_text_by_id(self, id: str):
        return self.driver.find_element(By.ID, id).text
    
    def find_element_by_class(self, class_name: str):
        return self.driver.find_element(By.CLASS_NAME, class_name)
    
    def find_elements_by_class(self, class_name: str):
        return self.driver.find_elements(By.CLASS_NAME, class_name)
    
    def find_select_element_by_id(self, id: str) -> Select:
        return Select(self.find_element_by_id(id))
    
    def close(self):
        self.driver.close()
    
    @property
    def page_source(self) -> str:
        return self.driver.page_source