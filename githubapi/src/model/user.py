class User(object):

  def __init__(self, id, name, login, bio, followers, following, public_repos, created_at):
    self.id = id
    self.name = name
    self.login = login
    self.bio = bio
    self.followers = followers
    self.following = following
    self.public_repos = public_repos
    self.created_at = created_at
