from time import sleep
from selenium import webdriver
from instapy import InstaPy
import tweepy


def test_login_page(browser):
    browser.get("https://www.instagram.com/accounts/login/")
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    username_input.send_keys("<your username>")
    password_input.send_keys("<your password>")
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    errors = browser.find_elements_by_css_selector("#error_message")
    assert len(errors) == 0


class SimpleTwitterBot(object):
    """Perform user engagement of existing users and post engagement."""

    def __init__(self):
        # Authenticate to Twitter
        auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
        auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

        # Create API object
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")

    def get_bme_users(self):
        pass

    def run_post_engagement(self, post):
        pass

    def perform_user_engagement(self):
        # Create a tweet
        api.update_status("Hello Tweepy")


def run_bot(headless_browser=False):
    """

    See: https://github.com/timgrossmann/InstaPy/issues/5035

    Parameters
    ----------
    headless_browser :

    Returns
    -------

    """
    session = InstaPy(
        username=USERNAME, password=PASSWORD, headless_browser=headless_browser
    )
    session.login()

    # fail-safe to not engage
    session.set_dont_like(["naked", "nsfw"])
    # session.set_use_clarifai(enabled=True, api_key=AAPI_ORG_API_KEY)
    # session.clarifai_check_img_for(['nsfw'])

    # set relationship bounds on too many followers
    session.set_relationship_bounds(enabled=True, max_followers=8500)

    # set session quota
    session.set_quota_supervisor(
        enabled=True,
        peak_comments_daily=240,
        peak_comments_hourly=21,
        peak_server_calls_hourly=100,
        peak_server_calls_daily=500,
    )

    # run user interactions
    session.like_by_tags(
        [
            "apiyouth",
            "sfusd",
            "aapi",
            # "aapiinaction",
            # "chinatownsf",
            # "aamplify"
        ],
        amount=5,
    )
    session.set_do_follow(True, percentage=50)
    # session.set_comments()


if __name__ == "__main__":
    run_bot()
