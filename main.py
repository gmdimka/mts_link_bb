import os
import undetected_chromedriver as uc

from dotenv import load_dotenv


from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC

from dom_consts import mute_mic_btn, entry_as_dmitry, enter_with_chrome, warning_first_step, join_btn, mute_cam_btn

load_dotenv()
MTS_LINK = os.getenv("MTS_LINK")

chrome_options = ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Разрешить доступ к микрофону
with uc.Chrome(options=chrome_options) as browser:
    browser.get(MTS_LINK)
    try:
        iframe = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "eventLandingFrame"))
        )
        browser.switch_to.frame(iframe)
        btn_warning_first_step = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, warning_first_step)))
        btn_warning_first_step.click()
    except TimeoutException:
        pass
    try:
        browser.switch_to.default_content()
    except WebDriverException:
        pass
    try:
        btn_entry_as_dmitry = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.XPATH, entry_as_dmitry)))
        btn_entry_as_dmitry.click()
    except TimeoutException:
        pass
    btn_enter_with_chrome = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.XPATH, enter_with_chrome)))
    btn_enter_with_chrome.click()
    btn_mute = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, mute_mic_btn)))
    if btn_mute.get_attribute("aria-label") == "Выключить микрофон":
        btn_mute.click()
    btn_cam = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, mute_cam_btn)))
    if btn_cam.get_attribute("aria-label") == "Выключить камеру":
        btn_cam.click()
    btn_join = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, join_btn)))
    btn_join.click()

    while True:

        for i in range(1, 13):
            xpath_btn_here = f"/html/body/div[{i}]/div/div/div[3]/button"
            xpath_btn_close = f"/html/body/div[{i}]/div/div/div[2]/button"
            try:
                btn_here = WebDriverWait(browser, 3).until(
                    EC.visibility_of_element_located((By.XPATH, xpath_btn_here)))
                btn_here.click()
                btn_close = WebDriverWait(browser, 3).until(
                    EC.visibility_of_element_located((By.XPATH, xpath_btn_close)))
                btn_close.click()

            except TimeoutException:
                pass
