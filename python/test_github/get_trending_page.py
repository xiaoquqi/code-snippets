from github_handler import GithubHandler

token = "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"

github_handler = GithubHandler(token)

repos = github_handler.get_trendings()
for repo in repos:
    print(repo.description)
    print(repo.full_name)
    print(repo.readme)
    print(repo.star_count)
