from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class Wikipedia:

    def verify_tutorial_presented_at_first_launch(self):
        with step('Verify tutorial shown at first launch'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).should(be.absent)
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).should(be.present)

    def verify_each_page_and_complete_tutorial(self):
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

    def search_for_article(self, text):
        with step('Enter text to the search field'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(text)

    def verify_first_article_title_in_the_list(self, text):
        with step('Verify article is first in the list and title is correct'):
            results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
            results.should(have.size_greater_than(0))
            results.first.should(have.text(text))

    def clear_search_field_and_enter_text(self, text):
        with step('Clear search field'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).clear()
        with step('Enter new text to the search field'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(text)

    def go_to_explore(self):
        with step('Open actions menu'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_toolbar_button_show_overflow_menu')).click()
        with step('Tap Explore'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_explore')).click()

    def open_article_in_search_results_having_order_n(self, n):
        with step(f'Tap on article in the list number <{n + 1}>'):
            browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))[n].click()

    def search_history(self, *text):
        with step('Tap on search field'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        with step('Verify previously entered queries are shown in Search History in ascending order'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/recent_searches_recycler')).all(
                (AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(
                have.texts(*text))

    def verify_phrase_exists_in_article(self, text):
        with step('Tap Find in Article in Bottom menu'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_find_in_article')).click()
        with step('Enter text and verify only 1 match found'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(text)
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/find_in_page_match')).should(have.text('1/1'))

    def verify_article_is_not_found(self):
        with step('Verify "No results" message is shown'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/results_text')).should(have.text('No results'))

    def save_article(self):
        with step('Tap on Save option in bottom menu'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_save')).click()
        with step('Verify message about saving is shown'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/snackbar_text')).should(have.text('Saved'))

    def verify_article_added_to_saved(self, text):
        with step('Go to Saved page'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/nav_tab_reading_lists')).click()
        with step('View Saved list details'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/recycler_view')).click()
        with step('Close hint and verify article title'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/buttonView')).click()
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).should(have.text(text))

    def verify_hiding_featured_article(self):
        with step('Verify Featured article is shown at the top of Home Page'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_card_header_title')).should(
                have.text('Featured article'))
        with step('Hide Featured article'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_list_card_header_menu')).click()
            browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/content'))[0].click()
        with step('Verify message about hidden card is shown'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/snackbar_text')).should(
                have.text('Card hidden.'))
        with step('Verify Top read article is shown first on Home Page'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_card_header_title')).should(
                have.text('Top read'))

    def verify_un_hiding_featured_article(self):
        with step('Tap Undo'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/snackbar_action')).click()
        with step('Verify Featured article is shown at the top of Home Page'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_card_header_title')).should(
                have.text('Featured article'))
