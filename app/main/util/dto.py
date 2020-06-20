from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class BlogDto:
    api = Namespace('blog', description='blog related operations')
    blog = api.model('blog_details', {
        'title': fields.String(required=True, description='title of the blog'),
        'description': fields.String(required=True, description='the description of the blog'),
        'content': fields.String(required=True, description='the content of the blog'),
        'is_private': fields.Boolean(required=False, description='whether the blog is available to the public')
    })