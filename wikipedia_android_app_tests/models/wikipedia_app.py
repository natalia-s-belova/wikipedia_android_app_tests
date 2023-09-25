from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class Wikipedia:

    def verify_tutorial_presented(self):
        with step('Verify tutorial shown at first run22'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).should(be.absent)
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).should(be.present)

    def interact_and_complete_tutorial(self):
        with step('Verify page 1 title'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                have.text('The Free Encyclopedia'))
        with step('Tap Continue'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        with step('Verify page 2 title'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                have.text('New ways to explore'))
        with step('Tap Continue'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        with step('Verify page 3 title'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                have.text('Reading lists with sync'))
        with step('Tap Continue'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        with step('Verify page 4 title'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                have.text('Send anonymous data'))
        with step('Verify options to Accept or Reject are present'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/rejectButton')).should(be.present)
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')).should(be.present)
        with step('Tap Accept'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')).click()
        with step('Verify Search input is shown'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).should(be.present)

    def skip_tutorial(self):
        with step('Skip tutorial'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    def verify_tutorial_not_presented(self):
        with step('Verify Tutorial is closed'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(be.absent)
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).should(be.present)

    def search_article(self, text):
        with step('Type search'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(text)

    def verify_article_title_in_list(self, text):
        with step('Verify content found'):
            results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
            results.should(have.size_greater_than(0))
            results.first.should(have.text(text))

    def open_article_in_search_results_having_order_n(self, n):
        with step('Tap on first found article in the list'):
            browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))[n].click()

    def verify_phrase_exists_in_article(self, text):
        with step('Tap Find in Article in Bottom menu'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_find_in_article')).click()
        with step('Enter text and verify only 1 match'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(text)
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/find_in_page_match')).should(have.text('1/1'))
