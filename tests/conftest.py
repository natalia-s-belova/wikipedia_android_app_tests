import allure_commons
import pytest
from selene import browser, support
import project
from appium import webdriver
import allure
from wikipedia_android_app_tests.utils import allure_helper


@pytest.fixture(scope='function', autouse=True)
def android_management():
    with allure.step('init app session'):
        options = project.config.to_driver_options()
        browser.config.driver = webdriver.Remote(project.config.remote_url, options=options)

    browser.config.timeout = float(project.config.timeout)

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure_helper.attach_screenshot()

    allure_helper.attach_page_source()

    session_id = browser.driver.session_id
    with allure.step(f'tear down app session: {session_id}'):
        browser.quit()

    if project.config.context == 'bstack':
        allure_helper.attach_bstack_video(session_id)
