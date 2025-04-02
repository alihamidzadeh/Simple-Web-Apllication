#Create App Context & DB
from app import create_app, db

app = create_app()
app.app_context().push()
db.create_all()
print("DB created!")

#Create Admin User
from app.models import User
import hashlib

raw_password = 'admin123'
hashed_password = hashlib.md5(raw_password.encode()).hexdigest()

admin = User(username='admin', password=hashed_password, role='admin')
db.session.add(admin)
db.session.commit()
admin.password = admin.hash_password_with_salt('admin123')
db.session.commit()
print("Admin user created!")
print(f"Users: {User.query.all()}")
