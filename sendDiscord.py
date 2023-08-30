import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import os

def get_commit_info(repo, token):
    commit_url = f"https://api.github.com/repos/{repo}/commits/main"
    headers = {"Authorization": f"token {token}"}
    
    try:
        response = requests.get(commit_url, headers=headers)
        response.raise_for_status()
        commit_info = response.json()
        return commit_info
    except requests.exceptions.RequestException as e:
        print(f"Error making HTTP request: {e}")
        return None

def main():
    # Identifying the credentials.txt file
    credentials_file = "credentials.txt"
    if not os.path.exists(credentials_file):
        print(f"Credentials file '{credentials_file}' not found.")
        return

    with open(credentials_file) as f:
        credentials = dict(line.strip().split("=") for line in f)

    # Define project and webhook information
    url_discord = credentials.get("url_discord")
    project = credentials.get("project")
    url_project = credentials.get("url_project")
    url_icon = credentials.get("url_icon")
    title_embed = credentials.get("title_embed")
    description = credentials.get("description")

    # Make the HTTP request to get the last commit information from the main branch
    github_repo = credentials.get("github_repo")
    github_token = credentials.get("github_token")

    commit_info = get_commit_info(github_repo, github_token)
    if not commit_info:
        return

    # Extract relevant information from the commit
    commit_message = commit_info["commit"]["message"]
    commit_author = commit_info["commit"]["author"]["name"]
    commit_date = commit_info["commit"]["author"]["date"]

    # Check if keywords are present in the commit message
    keywords = ["@doc", "@documentação", "@documentation"]
    if not any(keyword in commit_message.lower() for keyword in keywords):
        return

    # Decode special characters
    title_embed = title_embed.encode("latin-1").decode("utf-8")
    commit_message = commit_message.encode("latin-1").decode("utf-8")
    commit_author = commit_author.encode("latin-1").decode("utf-8")

    # Create the embed with the commit information
    webhook = DiscordWebhook(url=url_discord, username="Commit Documentation")
    embed = DiscordEmbed(
        title=title_embed, description=description, color="00ACAC"
    )
    embed.set_author(
        name=project,
        url=url_project,
        icon_url=url_icon,
    )
    embed.add_embed_field(name="Autor do Commit", value=commit_author, inline=False)
    embed.add_embed_field(name="Mensagem do Commit", value=commit_message, inline=False)
    embed.add_embed_field(name="Data do Commit", value=commit_date, inline=False)

    webhook.add_embed(embed)
    response = webhook.execute()

if __name__ == "__main__":
    main()
