import os

from github import Github

# Authentication is defined via github.Auth
from github import Auth

token = os.environ.get("GITHUB_TOKEN")
# using an access token
auth = Auth.Token(token)

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

repo = g.get_repo("mylxsw/aidea")
print(repo.full_name)
print(repo.description)

# To close connections after use
#g.close()
