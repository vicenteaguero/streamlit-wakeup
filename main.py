"""
# Streamlit Wake-Up

## Author
Vicente Agüero
- GitHub: https://github.com/vicenteaguero
- LinkedIn: https://www.linkedin.com/in/vicente-aguero
- Email: vicenteaguero@uc.cl

## Description
This script automates waking up Streamlit apps by periodically visiting their URLs.
It uses Selenium to perform the automation in a headless Chrome browser.
The use of Cron Jobs is recommended to schedule the script execution.
In the README file, you will find instructions on how to set up the script and the Cron Job.

## Last Updated
January 2025

## Disclaimer
This script is provided under the MIT License and is to be used at your own risk.
Streamlit may block or restrict access if the script is misused or violates their terms of service.
Please review the website's usage policies before deploying this automation.

## License
MIT License (2025)
---
"""

# main.py

import os

from streamlit_wakeup import wakeup_streamlit

if __name__ == '__main__':

    # If you have a different path to your chromedriver, change it here
    # More information on how to install chromedriver: https://chromedriver.chromium.org/downloads
    CHROME_PATH = os.path.join('chromedriver', 'chromedriver')

    ARGUMENTS = ['headless', 'disable-gpu', 'no-sandbox', 'disable-dev-shm-usage']

    # Add the URLs you want to wake up here. Only Streamlit URLs are supported.
    URLS = [
        'https://openun.streamlit.app/',
    ]

    # Set to True to print the logs
    VERBOSE = True

    if len(URLS) == 0:
        raise ValueError('No URLs provided.')

    for URL in URLS:
        wakeup_streamlit(url=URL, arguments=ARGUMENTS, chrome_path=CHROME_PATH, verbose=VERBOSE)
