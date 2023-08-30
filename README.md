# Webhook Discord Push Action

![Project Logo](https://imgur.com/IOtkCuf.png)

This project facilitates Discord notifications for commits containing the tag `#doc`.

## Setup

1. Generate a Discord webhook URL in your server settings.
2. Replace `credetials.txt` for the `sendDiscord.py` file with your variables.

      ```bash
      url_discord=
      project=
      url_project=
      url_icon=
      title_embed=
      github_repo=
      github_token=
      description=
      ```

3. Install the necessary dependencies from the provided `requirements.txt` file:

      ```bash
      pip install -r requirements.txt
      ```

4. Execute the script manually or use GitHub Actions to automate the process like `actions.yml` file.

## Usage

1. When committing, include the message "#doc" to trigger the Discord notification.
2. The action will automatically execute when a push is made to the main branch.
   Obs: Maybe you want to change the keyword for commits filtering.

## Code Overview

    [] Identifying the credentials.txt file
    [] Define project and webhook information
    [] Make the HTTP request to get the last commit information from the main branch
    [] Extract relevant information from the commit
    [] Check if keywords are present in the commit message
    [] Decode special characters
    [] Create the embed with the commit information
    [] Send message for discord channel

## Exemple:

![Example](https://imgur.com/bQi4dmL)

The script is triggered by a GitHub Action workflow on push events. It fetches commit information from the GitHub API, analyzes commit messages for specific keywords (such as `@doc` or similar), and sends relevant commit details as a Discord notification using a webhook.

To enable the functionality, the script reads configuration from a `credentials.txt` file, including Discord webhook URL, project information, and GitHub repository details.

Please refer to the provided `sendDiscord.py` script and GitHub Actions workflow files for detailed implementation and integration steps.

<img src="https://img.shields.io/badge/NOTE-DC143C?=for-the-badge&logo=&logoColor=white"> This project uses the `python-discord-webhook` library. You can find more information about it [here](https://github.com/lovvskillz/python-discord-webhook).
