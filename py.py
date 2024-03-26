from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mvee86wa@localhost/db_name'
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route('/blog', methods=['POST'])
def create_blog():
    data = request.get_json()
    new_blog = Blog(title=data['title'], content=data['content'])
    db.session.add(new_blog)
    db.session.commit()
    return jsonify({'message': 'New blog created.'}), 201

@app.route('/blog', methods=['GET'])
def get_blogs():
    blogs = Blog.query.all()
    return jsonify([{'id': blog.id, 'title': blog.title, 'content': blog.content} for blog in blogs])

@app.route('/blog/<int:id>', methods=['GET'])
def get_blog(id):
    blog = Blog.query.get(id)
    if blog:
        return jsonify({'id': blog.id, 'title': blog.title, 'content': blog.content})
    else:
        return jsonify({'message': 'Blog not found.'}), 404

@app.route('/blog/<int:id>', methods=['PUT'])
def update_blog(id):
    data = request.get_json()
    blog = Blog.query.get(id)
    if blog:
        blog.title = data['title']
        blog.content = data['content']
        db.session.commit()
        return jsonify({'message': 'Blog updated.'})
    else:
        return jsonify({'message': 'Blog not found.'}), 404

@app.route('/blog/<int:id>', methods=['DELETE'])
def delete_blog(id):
    blog = Blog.query.get(id)
    if blog:
        db.session.delete(blog)
        db.session.commit()
        return jsonify({'message': 'Blog deleted.'})
    else:
        return jsonify({'message': 'Blog not found.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
