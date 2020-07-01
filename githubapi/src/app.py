from flask import Flask
from flask_restx import Api
from githubapi.src.views.user import user_namespace

app = Flask(__name__)

flask_api = Api(app=app, title="GitHub's API reader",
          description="This API consumes GitHub's API in order to retrieve user's repo informations")

flask_api.add_namespace(user_namespace, path='/users')
