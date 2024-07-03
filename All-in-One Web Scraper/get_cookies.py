import requests

def get_cookies(self):
    cookies = self.driver.get_cookies()
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    return session
