# Webhook Discord Push Action

<div align=center>
<img src="https://imgur.com/IOtkCuf.png" width="250" height="150" alt="Imagem.">
</div>

This project facilitates Discord notifications for commits containing the special tags like `@documentation` or `@doc` like in my case.

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
5. # Configure your github_token:
      1. **Log in to Your GitHub Account:**
         Go to GitHub and log in to your account.

      2. **Access Token Settings:**
         In the top-right corner of the page, click on your profile picture and select `Settings`.

      3. **Go to Access Token Section:**
         In the left sidebar, scroll down to the `Developer settings` section and click on `Personal access tokens`.

      4. **Generate a New Token:**
         Click on the `Generate new token` button.

      5. **Configure Token Options:**

            - Give the token a descriptive name so you can identify its purpose.
            - Select the necessary permissions. For your case, you'll likely need read permissions related to repositories.
            - Once you've selected the permissions, scroll to the bottom and click `Generate token`.

      6. **Copy the Token:**
         GitHub will generate the token. Make sure to copy the generated token immediately as it will be displayed only once. If you lose the token, you'll need to create a new one.

      7. **Paste the Token in Your Project:**
         In the file where you're using the token (probably the `sendDiscord.py` file in this case), replace the value of `github_token` with the token you just generated.
      Remember that personal access tokens are sensitive and should be handled carefully. Do not share your tokens publicly or store them in insecure locations.

## Usage

1. When committing, include the message `@doc` to trigger the Discord notification.
2. The action will automatically execute when a push is made to the main branch.
   Obs: Maybe you want to change the keyword for commits filtering.

## Code Overview

- [x] Identifying the `credentials.txt` file
- [x] Define project and webhook information
- [x] Make the HTTP request to get the last commit information from the main branch
- [x] Extract relevant information from the commit
- [x] Check if keywords are present in the commit message
- [x] Decode special characters
- [x] Create the embed with the commit information
- [x] Send message for Discord channel

## Example:

<div align=center>
<img src="https://imgur.com/bQi4dmL.png" alt="IMG">
</div>

The script is triggered by a GitHub Action workflow on push events. It fetches commit information from the GitHub API, analyzes commit messages for specific keywords (such as `@doc` or similar), and sends relevant commit details as a Discord notification using a webhook.

To enable the functionality, the script reads configuration from a `credentials.txt` file, including Discord webhook URL, project information, and GitHub repository details.

Please refer to the provided `sendDiscord.py` script and GitHub Actions workflow files for detailed implementation and integration steps.

<img src="https://img.shields.io/badge/NOTE-DC143C?=for-the-badge&logo=&logoColor=white"> This project uses the `python-discord-webhook` library. You can find more information about it [here](https://github.com/lovvskillz/python-discord-webhook).
