from github import Github

# Authentication is defined via github.Auth
from github import Auth

token = "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"
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
