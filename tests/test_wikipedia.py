from wikipedia_android_app_tests.models.wikipedia_app import Wikipedia
import allure
from allure_commons.types import Severity

pytestmark = [
    allure.label('layer', 'UI test'),
    allure.label('owner', 'nsbelova'),
    allure.epic('Wikipedia android app'),
    allure.tag('android')
]


@allure.title('Verify tutorial is shown at the first launch')
@allure.feature('Tutorial')
@allure.severity(Severity.NORMAL)
def test_tutorial_shown_and_functional_after_installation():
    application = Wikipedia()
    application.verify_tutorial_presented_at_first_launch()
    application.verify_each_page_and_complete_tutorial()


@allure.title('Verify tutorial can be skipped')
@allure.feature('Tutorial')
@allure.severity(Severity.NORMAL)
def test_tutorial_can_be_skipped():
    application = Wikipedia()
    application.skip_tutorial()
    application.verify_tutorial_not_presented()


@allure.title('Verify requested article is shown in the list')
@allure.feature('Article search')
@allure.severity(Severity.BLOCKER)
def test_search_for_existing_article():
    application = Wikipedia()
    application.skip_tutorial()
    application.search_for_article('Appium')
    application.verify_first_article_title_in_the_list('Appium')


@allure.title('Verify message for search of non-existing article')
@allure.feature('Article search')
@allure.severity(Severity.CRITICAL)
def test_search_for_non_existing_article():
    application = Wikipedia()
    application.skip_tutorial()
    application.search_for_article('thisacticletitledoesnotexistandcannotbefound')
    application.verify_article_is_not_found()


@allure.title('Verify search list result is updated when search query is changed')
@allure.feature('Article search')
@allure.severity(Severity.BLOCKER)
def test_change_search_query():
    application = Wikipedia()
    application.skip_tutorial()
    application.search_for_article('Java lang')
    application.verify_first_article_title_in_the_list('Java (programming language)')
    application.clear_search_field_and_enter_text('Python lang')
    application.verify_first_article_title_in_the_list('Python (programming language)')


@allure.title('Verify search history')
@allure.feature('Article search')
@allure.severity(Severity.CRITICAL)
def test_verify_search_history():
    application = Wikipedia()
    application.skip_tutorial()
    application.search_for_article('Java lang')
    application.open_article_in_search_results_having_order_n(0)
    application.go_to_explore()
    application.search_for_article('Python lang')
    application.open_article_in_search_results_having_order_n(0)
    application.go_to_explore()
    application.search_for_article('c sharp lang')
    application.open_article_in_search_results_having_order_n(0)
    application.go_to_explore()
    application.search_history('c sharp', 'Python lang', 'Java lang')


@allure.title('Verify text search in the article')
@allure.feature('Article interaction')
@allure.severity(Severity.BLOCKER)
def test_find_text_in_article():
    application = Wikipedia()
    application.skip_tutorial()
    application.search_for_article('Python lang')
    application.open_article_in_search_results_having_order_n(0)
    application.verify_phrase_exists_in_article('the designer of python, Guido van Rossum')


@allure.title('Verify article saving')
@allure.feature('Article interaction')
@allure.severity(Severity.CRITICAL)
def test_save_article():
    application = Wikipedia()
    application.skip_tutorial()
    application.search_for_article('Python lang')
    application.verify_first_article_title_in_the_list('Python (programming language)')
    application.open_article_in_search_results_having_order_n(0)
    application.save_article()
    application.go_to_explore()
    application.verify_article_added_to_saved('Python (programming language)')


@allure.title('Verify ability to hide article')
@allure.feature('Home page')
@allure.severity(Severity.CRITICAL)
def test_hide_featured_card_on_homepage():
    application = Wikipedia()
    application.skip_tutorial()
    application.verify_hiding_featured_article()


@allure.title('Verify ability to un-hide article')
@allure.feature('Home page')
@allure.severity(Severity.CRITICAL)
def test_un_hide_featured_card_on_homepage():
    application = Wikipedia()
    application.skip_tutorial()
    application.verify_hiding_featured_article()
    application.verify_un_hiding_featured_article()
