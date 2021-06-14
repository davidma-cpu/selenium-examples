from seleniumbase import BaseCase
import time
from datetime import datetime, timedelta


class Login(BaseCase):

    def test_login(self):
        self.open('https://happin.app/')
        self.click("link=Login")
        self.click("//button[3]")
        self.type('[name="email"]', 'test@test.com')
        self.click("//div[2]/button")
        self.type('#password', 'test123')
        self.click("//div[2]/button")

        time.sleep(10)
        #Click top right corner
        self.click("//div[2]/div/img")
        
        ##Click host event
        self.click("//*[@id=\"tippy-2\"]/div[1]/div[1]/div/a[3]/span")
        
        time.sleep(10)
        #Click Create Event
        self.click("//button[2]")

        #Click Hybrid Event
        self.click("//div[2]/p")
        
        #Click Continue
        self.click("//button")
        
        #Input Event Name
        self.type("//span/input", 'Test Name')
        
        #Click line button to fill event description
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(
            self.driver.find_element_by_xpath("//iframe[@class=\"tox-edit-area__iframe\"]"))
        self.type('//p', "test")
        self.driver.switch_to.default_content()

        #Upload Cover Photo
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys("/Users/weibinma/Desktop/bg1.jpeg")
        
        #Click Next
        self.click("/html/body/app-root/nz-layout/nz-layout/app-dashboard/nz-layout/nz-content/app-create-hybrid/div/main/div/div/div[2]/div[3]/button")

        ##Change time to now + (x Minutes)
        now = datetime.now()
        show_time = now + timedelta(minutes=60)
        show_time = show_time.strftime("%Y-%m-%d %H:%M:%S")
        self.click('//nz-date-picker/nz-picker/span/input')
        self.driver.find_element_by_class_name("ant-calendar-input ").clear()
        self.driver.find_element_by_class_name("ant-calendar-input ").send_keys(show_time)
        self.driver.find_element_by_class_name("ant-calendar-ok-btn ").click()

        
