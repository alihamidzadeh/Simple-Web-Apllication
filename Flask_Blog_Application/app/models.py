from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  
    role = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def is_admin(self):
        return self.role == 'admin'

    def is_author(self):
        return self.role == 'author'
    
    @staticmethod
    def hash_password(password):
        return hashlib.md5(password.encode()).hexdigest()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    author = db.relationship('User', backref='posts')
    likes = db.relationship('PostLike', backref='post', cascade='all, delete-orphan')
    comments = db.relationship('Comment', backref='post', cascade='all, delete-orphan')



class PostLike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    value = db.Column(db.String(10))  # 'like' or 'dislike'

    user = db.relationship('User', backref='likes')


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref='comments')
