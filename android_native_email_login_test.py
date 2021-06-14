from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
from src.testproject.sdk.drivers.actions import Actions
import pytest


"""
    Project: Android Happin
    Package: TestProject.Tests.AndroidHappin
    Test: native email login
    Created by: David Ma (davidm989@gmail.com)
"""


@pytest.fixture()
def driver():
    capabilities = {
        "platformName": "Android",
        "udid": "LMQ630SKFY65VSQWKB",
        "appPackage": "app.happin.production",
        "appActivity": "app.happin.SplashActivity",
    }
    driver = webdriver.Remote(token="D1uRRn1VuaNoGGLrCu8YPWH00YOZaaApL-MJ6TcizbM",
                              project_name="Android Happin",
                              job_name="native email login",
                              desired_capabilities=capabilities)
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Use the native login function to log into registered account."""

    # 1. Reset App
    # Clear application data and restart
    driver.reset()

    # 2. Click 'app.happin.production:id/btn_next1'
    app_happin_production_colon_id_slash_btn_next1 = driver.find_element(By.ID,
                                                                         "app.happin.production:id/btn_next")
    app_happin_production_colon_id_slash_btn_next1.click()

    # 3. Click 'app.happin.production:id/btn_next1'
    app_happin_production_colon_id_slash_btn_next1 = driver.find_element(By.ID,
                                                                         "app.happin.production:id/btn_next")
    app_happin_production_colon_id_slash_btn_next1.click()

    # 4. Click 'app.happin.production:id/btn_next1'
    app_happin_production_colon_id_slash_btn_next1 = driver.find_element(By.ID,
                                                                         "app.happin.production:id/btn_next")
    app_happin_production_colon_id_slash_btn_next1.click()

    # 5. Click 'Start'
    start = driver.find_element(By.XPATH,
                                "//android.widget.TextView[@text = 'Start']")
    start.click()

    # 6. Click 'sign up with email'
    sign_up_with_email = driver.find_element(By.ID,
                                             "app.happin.production:id/sign_up_with_email")
    sign_up_with_email.click()

    # 7. Pause for '2000'ms
    driver.pause(milliseconds=2000)

    # 8. Tap at ('248','2277') with '1' fingers for '100'ms
    # Remove auto suggestion emails pop up
    driver.tap(positions=[(248, 2277)], duration=100)

    # 9. Type 'chumifyqa8@gmail.com' in 'Email address field'
    email_address_field = driver.find_element(By.ID,
                                              "app.happin.production:id/edttxt_email")
    email_address_field.send_keys("test@test.com")

    # 10. Type 'Hello123456' in 'Password field'
    password_field = driver.find_element(By.ID,
                                         "app.happin.production:id/edttxt_password")
    password_field.send_keys("test-pass")

    # 11. Click 'Next Button'
    next_button = driver.find_element(By.ID,
                                      "app.happin.production:id/btn_next")
    next_button.click()

    # 12. Click 'allow access to device's location'
    allow_access_to_device_s_location = driver.find_element(By.ID,
                                                            "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    allow_access_to_device_s_location.click()

    # 13. Click 'allow access to photos, media and files'
    allow_access_to_photos_media_and_files = driver.find_element(By.ID,
                                                                 "com.android.permissioncontroller:id/permission_allow_button")
    allow_access_to_photos_media_and_files.click()

    # 14. Pause for '6000'ms
    driver.pause(milliseconds=6000)

    # 15. Click 'Me Tab'
    me_tab = driver.find_element(By.XPATH,
                                 "//android.widget.TextView[@text = 'Me']")
    me_tab.click()

    # 16. Click 'More Button Profile Page'
    more_button_profile_page = driver.find_element(By.ID,
                                                   "app.happin.production:id/btn_more")
    more_button_profile_page.click()

    # 17. Make a long press gesture on 'VERSION : 1.0.67(2021.04.11.Release.1...'
    # Toggle Dev Mode
    version_colon_1_0_67_2021_04_11_release_1_ = driver.find_element(By.ID,
                                                                     "app.happin.production:id/txt_version")
    TouchAction(driver).long_press(
        el=version_colon_1_0_67_2021_04_11_release_1_, duration=3000).perform()
