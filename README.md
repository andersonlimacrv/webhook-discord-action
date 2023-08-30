# Webhook Discord Push Action

This is a project that sends Discord notifications for commits containing `#doc`.

## Setup

1. Create a Discord webhook in your server settings.
2. Replace `URL_DO_WEBHOOK` in the `sendDiscord.py` file with your actual webhook URL.
3. Install required dependencies using the provided `requirements.txt` file:
   
    ```
    pip install -r requirements.txt
    ```
5. Run the script manually or use GitHub Actions to automate the process.

## Usage

1. When making a commit, include the message "#doc" to trigger the Discord notification.
2. The action will run automatically when a push is made to the main branch.

<img src="https://img.shields.io/badge/NOTE-DC143C?=for-the-badge&logo=&logoColor=white"> * This project uses the `python-discord-webhook` library. You can find more information about it [here](https://github.com/lovvskillz/python-discord-webhook).
