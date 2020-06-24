import unittest
from ...src.model.user import User

class TestModelUser(unittest.TestCase):

  def setUp(self):
    self.user = None

  def test_init(self):
    self.user = User(17485700,
                    'Marcelo Aquino',
                    'MarceloAquino7',
                    'Senior Software Engineer @ ArcTouch\r\n- Data Scientist\r\n- MCP',
                    5,
                    0,
                    10,
                    '2016-02-26T00:39:47Z')
    self.assertEqual('Marcelo Aquino', self.user.name)
    self.assertEqual(17485700, self.user.id)
    self.assertEqual('MarceloAquino7', self.user.login)
    self.assertEqual(5, self.user.followers)
