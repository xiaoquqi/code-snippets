import logging

from bs4 import BeautifulSoup
from github import Auth, Github
import requests

BASE_URL = "https://github.com"
TRENDING_URL = "%s/trending" % BASE_URL
REPOS_XPATH = "article.Box-row"
REPO_XPATH = "h2.h3.lh-condensed > a"

# Query Conditions
LANG_CODE_ANY = "any"
LANGUAGE_ANY = "any"
SINCE_TODAY = "today"

# Repo Relates
README_MD = "readme.md"


class GithubHandler(object):

    def __init__(self, token):
        self.token = token

    def get_trendings(self, spoken_language_code=LANG_CODE_ANY,
                      language=LANGUAGE_ANY, since=SINCE_TODAY):
        """Parser github trending page to get repos

        spoken_language_code: Filter spoken language of repo, ex: en, zh
        language: Programming language of repo, ex: python, c, javascript
        since: Query time range, ex: today, weekly, monthly
        """
        query_trending_url = self._build_query_url(
            spoken_language_code, language, since)

        logging.info("Query github trending url: %s" % query_trending_url)

        response = requests.get(query_trending_url)

        soup = BeautifulSoup(response.text, "html.parser")
        repo_items = soup.select(REPOS_XPATH)

        repos = []
        for repo in repo_items:
            repo_xpath = repo.select_one(REPO_XPATH)
            repo_url = self._clean(repo_xpath["href"])

            repo = Repo(self.token, repo_url)
            repos.append(repo)

        return repos

    def _build_query_url(self, spoken_language_code, language, since):
        # Create query url
        query_trending_url = TRENDING_URL

        # Add language
        if not language == LANGUAGE_ANY:
            query_trending_url = "%s/%s" % (query_trending_url, language)

        # Add since
        query_trending_url = "%s?since=%s" % (query_trending_url, since)

        if not spoken_language_code == LANG_CODE_ANY:
            query_trending_url = "%s&spoken_language_code=%s" % (
                query_trending_url, spoken_language_code)

        return query_trending_url

    def _clean(self, text):
        """Remove useless string for html parser"""
        if text[0] == "/":
            return text[1:]


class Repo(object):

    def __init__(self, token, path):
        self.token = token
        self.path = path

        self._github = None
        self._repo = None
        self._readme = None

    @property
    def github(self):
        if not self._github:
            auth = Auth.Token(self.token)
            self._github = Github(auth=auth)

        return self._github

    @property
    def repo(self):
        """This is wrapper of pygithub repo object"""
        if not self._repo:
            self._repo = self.github.get_repo(self.path)

        return self._repo

    @property
    def description(self):
        return self.repo.description

    @property
    def full_name(self):
        return self.repo.full_name

    @property
    def readme(self):
        if not self._readme:
            readme_path = self._get_readme_path()
            content = self.repo.get_contents(readme_path)
            self._readme = content.decoded_content.decode('utf-8')

        return self._readme

    @property
    def star_count(self):
        return self.repo.stargazers_count

    def _get_readme_path(self):
        contents = self.repo.get_contents("")
        logging.debug("Repo files: %s" % contents)

        readme_path = None
        for content in contents:
            if content.path.lower() == README_MD:
                readme_path = content.path
                break

        return readme_path
