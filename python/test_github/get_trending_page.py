import os

from github_handler import GithubHandler

token = os.environ.get("GITHUB_TOKEN")

github_handler = GithubHandler(token)

repos = github_handler.get_trendings()
for repo in repos:
    print(repo.description)
    print(repo.full_name)
    print(repo.readme)
    print(repo.star_count)
