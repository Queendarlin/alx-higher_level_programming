#!/usr/bin/python3
"""
A script that lists 10 commits (from the most recent to oldest) of a
repository by a specified user using the GitHub API.
"""

import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API endpoint for commits
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    # Send a GET request to the GitHub API
    response = requests.get(url)

    try:
        commits = response.json()[:10]  # Get the 10 most recent commits

        # Print each commit sha and author name
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except IndexError:
        print("Error: Less than 10 commits available")
