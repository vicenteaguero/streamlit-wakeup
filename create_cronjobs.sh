#!/bin/bash

PROJECT_DIR=$(pwd)
VENV_DIR="$PROJECT_DIR/.venv"
PYTHON_BIN="$VENV_DIR/bin/python3"
CRONJOB_FILE="$PROJECT_DIR/cronjob.txt"
SCRIPT_PATH="$PROJECT_DIR/main.py"
LOG_FILE="$PROJECT_DIR/streamlit-wakeup.log"

echo "> Creating Python Virtual Environment..."

$PYTHON_BIN -m venv $VENV_DIR
source $VENV_DIR/bin/activate
pip install --upgrade pip
pip install selenium
deactivate

echo "> Creating Cron Job to run the script every 5 hours..."

echo "0 */5 * * * source $VENV_DIR/bin/activate && $PYTHON_BIN $SCRIPT_PATH >> $LOG_FILE 2>&1" > $CRONJOB_FILE

crontab $CRONJOB_FILE

echo "> Current Cron Jobs:"

crontab -l

echo "> Setup complete. Your Streamlit wake-up script will now run every 5 hours."