from flask_restx import Namespace, Resource
from ..api import git_api

user_namespace = Namespace('users', 'Users repo information ')

@user_namespace.route("/<string:username>", methods=['GET'])
@user_namespace.param("username", "User name")
class UserRepos(Resource):

    @classmethod
    @user_namespace.doc("get_repos")
    @user_namespace.response(404, "Repo not found")
    def get(cls, username):
        """
        Get all public repos from a specific user
        """
        return git_api.get_user_repos(username).json()


@user_namespace.route("/<string:username>/<string:repo_name>", methods=['GET'])
@user_namespace.param("username", "User name")
@user_namespace.param("repo_name", "Repo name")
class UserRepoDetails(Resource):

    @classmethod
    @user_namespace.doc("get_repo_details")
    @user_namespace.response(404, "Repo not found")
    def get(cls, username, repo_name):
        """
        Get repo details from a specific user
        """
        return git_api.get_repo_details(username, repo_name).json()
