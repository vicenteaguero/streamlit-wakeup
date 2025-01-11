# streamlit-wakeup.py

from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

def create_browser(arguments: list, chrome_path: str) -> wb.Chrome:
    """Create a Chrome browser instance."""
    options = wb.chrome.options.Options()
    for arg in arguments:
        options.add_argument(f'--{arg}')
    return wb.Chrome(service=wb.chrome.service.Service(chrome_path), options=options)

def wakeup_streamlit(url: str, arguments: list, chrome_path: str, verbose: bool = False) -> None:
    """Wakeup a Streamlit Cloud URL by clicking the wakeup button."""
    if not url.endswith('.streamlit.app/'):
        raise ValueError('URL must be a Streamlit Cloud URL.')
    browser = create_browser(arguments, chrome_path)
    try:
        if verbose:
            print(f'Getting {url}...')
        browser.get(url)
        time.sleep(10)
        try:
            button = WebDriverWait(browser, 5).until(
                ec.presence_of_element_located((
                    By.CSS_SELECTOR, '[data-testid="wakeup-button-viewer"]'
                ))
            )
            if verbose:
                print('Found the button!')
            button.click()
        except Exception:
            if verbose:
                print('Could not find the button.')
    except Exception as e:
        if verbose:
            print(f'An error occurred: {e}')
    finally:
        browser.quit()
        if verbose:
            print('Browser closed.')
