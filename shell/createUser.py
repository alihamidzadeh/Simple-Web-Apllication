# #Create App Context & DB
from app import create_app, db

app = create_app()
app.app_context().push()

db.create_all()

#Create Admin User
from app.models import User 
admin = User(username='admin', password='admin123', role='admin')
db.session.add(admin)
db.session.commit()
