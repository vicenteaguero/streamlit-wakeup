# ![Streamlit Wake-Up](https://docs.streamlit.io/logo.svg) Streamlit Wake-Up

A Python script to keep your Streamlit apps awake by periodically visiting their URLs.
This project helps overcome Streamlit Cloud's auto-sleep feature for inactive apps,
ensuring your apps remain active and accessible to users.

**Author:** **[Vicente Aguero](https://github.com/vicenteaguero)**.

Feel free to connect with me on **[LinkedIn](https://www.linkedin.com/in/vicente-aguero/)**!

## Features

- Automates waking up Streamlit apps using Selenium and a headless Chrome browser.
- Cron jobs for scheduling periodic checks.

## Why is this repository important?

Streamlit Cloud offers free hosting for apps but automatically puts them to sleep
when they remain inactive for too long. This project ensures your apps are always running,
improving accessibility and usability for your users.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/vicenteaguero/streamlit-wakeup.git
cd streamlit-wakeup
```

### 2. Update the URLs

Edit the `main.py` file to include the Streamlit URLs you want to wake up:

```python
URLS = [
    'https://your-streamlit-app1.streamlit.app/',
    'https://your-streamlit-app2.streamlit.app/',
]
```

### 3. Set Up ChromeDriver

Download and install [ChromeDriver](https://chromedriver.chromium.org/downloads),
and update the path in the `CHROME_PATH` variable in `main.py` before running the script.

### 4. Create Cron Jobs

Make the script executable and create the cron jobs:

```bash
chmod +x create_cronjobs.sh
./create_cronjobs.sh
```

This will schedule the script to run every 5 hours to wake up your Streamlit apps.

## Disclaimer

This project is provided under the MIT License and is to be used **at your own risk**.
Streamlit may block or restrict access if the script is misused or violates their terms of service.
Please ensure you review and comply with the website's usage policies before deploying this automation.

## How to Contribute

- Fork the repository and star it on [GitHub](https://github.com/vicenteaguero/streamlit-wakeup).
- Submit pull requests for improvements:
  - Support for additional web drivers (e.g., Firefox, Edge).
  - Compatibility with Windows or macOS platforms.
  - Enhanced scheduling or configuration features.
- Suggestions, bug fixes, and feature requests are welcome!

## Future Enhancements

- Expand compatibility with other browsers and drivers.
- Testing and optimization for Windows and macOS platforms.

## License

This project is licensed under the MIT License (2025).

If you have any questions, feel free to reach out to [vicenteaguero@uc.cl](mailto:vicenteaguero@uc.cl).

Contributions and feedback are always welcome!
