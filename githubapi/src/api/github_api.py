import requests
from .api import BaseAPI

class GitHubApi(BaseAPI):
    """
      The purpose of this class is to be an object to consume the GitHub's API
      in order to retrieve informations about an user and his repos
    """

    def get_user_repos(self, name):
      url = '%s/users/%s/repos' % (self.base_url, name)
      return self.get(url)

    def get_repo_details(self, name, repo_name):
      url = '%s/repos/%s/%s' % (self.base_url, name, repo_name)
      return self.get(url)
