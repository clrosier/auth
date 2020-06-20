from flask import request
from flask_restplus import Resource

from ..util.dto import BlogDto
from ..service.blog_service import save_new_blog, get_user_blogs

api = BlogDto.api
_blog = BlogDto.blog


@api.route('/<string:user_id>')
class BlogList(Resource):
    @api.doc('list_of_user_blogs')
    @api.marshal_list_with(_blog, envelope='data')
    def get(self, user_id):
        blogs = get_user_blogs(user_id)
        if not blogs:
            api.abort(404)
        else:
            return blogs


@api.route('/')
class Blog(Resource):
    @api.doc('create a new blog')
    @api.response(201, 'Blog successfully created.')
    @api.expect(_blog, validate=True)
    def post(self):
        data = request.json
        return save_new_blog(data=data), {'Access-Control-Allow-Origin': '*'}
