from wikipedia_android_app_tests.models.wikipedia_app import Wikipedia


def test_tutorial_shown_and_functional_after_installation():
    application = Wikipedia()
    application.verify_tutorial_presented()
    application.interact_and_complete_tutorial()


def test_skip_tutorial():
    application = Wikipedia()
    application.skip_tutorial()
    application.verify_tutorial_not_presented()


def test_search_article_by_title():
    application = Wikipedia()
    application.skip_tutorial()
    application.search_article('Appium')
    application.verify_article_title_in_list('Appium')


def test_open_found_article():
    application = Wikipedia()
    application.skip_tutorial()
    application.search_article('Python lang')
    application.verify_article_title_in_list('Python (programming language)')
    application.open_article_in_search_results_having_order_n(0)
    application.verify_phrase_exists_in_article('the designer of python, Guido van Rossum')
