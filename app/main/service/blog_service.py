from app.main import db
from app.main.model.blog import Blog

from auth_helper import get_logged_in_user

import datetime

def save_new_blog(data):
    blog = Blog.query.filter_by(title=data['title']).first()
    if not blog:
        new_blog = Blog(
            title = data['title'],
            description = data['description'],
            content = data['content'],
            is_private = data['is_private'],
            created_by = get_logged_in_user(data),
            creation_date = datetime.datetime.utcnow()
        )
        save_changes(new_blog)
        response_object = {
            'status': 'success',
            'message': 'Successfully saved new blog.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Blog with title already exists.'
        }
        return response_object, 409

def get_user_blogs(user_id):
    blogs = Blog.query.filter_by(created_by=user_id).all()


def save_changes(data):
    db.session.add(data)
    db.session.flush()
    db.session.commit()
