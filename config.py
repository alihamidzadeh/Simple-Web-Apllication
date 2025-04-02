class Config:
    SECRET_KEY = 'dev'  # Use a stronger key in production
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/blog.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
