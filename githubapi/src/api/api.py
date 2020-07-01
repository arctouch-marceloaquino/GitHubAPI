import requests

class BaseAPI(object):
  """
    The purpose of this class is to be a base class for all API's based objects
    providing easy access to HTTP verbs implementation like GET, POST, PUT and DELETE
  """
  def __init__(self, url, header=None, timeoutConnection = 4):
      self.base_url = url
      self.header = header
      self.timeout = timeoutConnection

  def get(self, url):
    return requests.get(url, headers=None, timeout=4)

  def post(self, url, data):
    raise NotImplementedError

  def put(self, url, data):
    raise NotImplementedError

  def delete(self, url, id):
    raise NotImplementedError
