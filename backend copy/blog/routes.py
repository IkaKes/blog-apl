from flask import Blueprint, jsonify, request
from blog.models import db, Post

blog_blueprint = Blueprint('blog', __name__)

@blog_blueprint.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': post.id, 'title': post.title, 'content': post.content} for post in posts])

@blog_blueprint.route('/api/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    post = Post(title=data['title'], content=data['content'])
    db.session.add(post)
    db.session.commit()
    return jsonify({'id': post.id, 'title': post.title, 'content': post.content}), 201

@blog_blueprint.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    post = Post.query.get_or_404(post_id)
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    db.session.commit()
    return jsonify({'id': post.id, 'title': post.title, 'content': post.content})

@blog_blueprint.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return '', 204
