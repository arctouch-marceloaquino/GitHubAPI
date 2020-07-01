import unittest
import json
from ...src.views.user import UserRepos
from ...src.views.user import UserRepoDetails
from ...src.model.user import User

class TestViewUser(unittest.TestCase):

  def setUp(self):
    self.user_repos = UserRepos()
    self.user_repo_details = UserRepoDetails()
    self.user = User(17485700,
                    'Marcelo Aquino',
                    'MarceloAquino7',
                    'Senior Software Engineer @ ArcTouch\r\n- Data Scientist\r\n- MCP',
                    5,
                    0,
                    10,
                    '2016-02-26T00:39:47Z')
    self.repo_name = 'BakeryAPI'

  def test_get_repos(self):
    response = self.user_repos.get(username=self.user.login)
    repos_list = json.loads(json.dumps(response))
    self.assertEqual(len(repos_list), self.user.public_repos)

  def test_get_repo_details(self):
    response = self.user_repo_details.get(self.user.login, self.repo_name)
    repo_details = json.loads(json.dumps(response))
    self.assertEqual(repo_details['name'], self.repo_name)
