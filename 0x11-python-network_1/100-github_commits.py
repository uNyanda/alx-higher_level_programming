#!/usr/bin/python3
"""
This a challange!

The script takes 2 arguments and lists the 10 most recent commits of a GitHub
repository, specified by the repository name and owner name.
"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <repository_name> <owner_name>')
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]

    # GitHub API endpoint for commits
    link = 'https://api.github.com/repos/{owner}/{repository}/commits'
    url = f'{link}'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            commits = response.json()[:10]

            # Print each commit in the specified format
            for commit in commits:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f'{sha}: {author_name}')
        else:
            print(f'Failed to retrieve commits: {response.status_code}')
    except requests.RequestException as e:
        print(f'Request failed: {e}')
        sys.exit(1)
