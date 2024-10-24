import os
import undetected_chromedriver as uc

from dotenv import load_dotenv


from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC

from dom_consts import mute_mic_btn, entry_as_dmitry, enter_with_chrome, warning_first_step, join_btn, here_btn, \
    close_btn, here_btn_2, close_btn_2, mute_cam_btn, all_users_btn, num_of_users, rofl_btn, search_btn, leave_btn

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

    actions = ActionChains(browser)
    btn_all_users = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, all_users_btn)))
    btn_rofl = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, rofl_btn)))

    actions.move_to_element(btn_rofl).perform()
    actions.move_to_element(btn_all_users).perform()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, all_users_btn))).click()

    users = 150
    while users > 30:
        try:
            btn_here = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, here_btn)))
            btn_here.click()
            btn_close = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, close_btn)))
            btn_close.click()

        except TimeoutException:
            pass

        try:
            btn_here_2 = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, here_btn_2)))
            btn_here_2.click()
            btn_close_2 = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, close_btn_2)))
            btn_close_2.click()

        except TimeoutException:
            pass

        users = int(WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, num_of_users))).text)

    btn_search = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, search_btn)))
    actions.move_to_element(btn_search).perform()
    actions.move_to_element(btn_rofl).perform()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, leave_btn))).click()
