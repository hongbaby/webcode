from business import logger, get_browser
from pages.Login_Page import LoginPage
from pages.welcome_page import WelcomePage


def verify_login(username, password):
    logger.info("Go to etown login dialog: ")
    login_page = LoginPage(get_browser())
    login_page.element_username.send_keys(username)
    login_page.element_password.send_keys(password)
    login_page.element_login_button.click()

    logger.info("Go to etown welcome dialog: ")
    login_page.verify_current_page_url(WelcomePage(get_browser()).url)
