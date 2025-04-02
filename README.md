# 📝 Flask Blog Web Application

A simple Flask-based blog platform built for educational purposes, showcasing user authentication, role-based access, post management, salted password hashing, and intentional security flaws for demo/lab use.

---

## 🚀 Features

### ✅ Core Functionalities
- User Registration & Login
- Password hashing with **MD5 + salt**
- Roles: `admin`, `author`, `normal`
- Authors can create/edit their own posts
- Admin can edit/delete any post or user
- Comments + Like/Dislike system
- Flash messages for feedback
- Directory exposure vulnerability demo (`/instance`)

---

## 🔐 Security Lab Features

This project demonstrates:
- Insecure password storage (MD5 without salt)
- Rainbow table attacks on SQLite DB
- How salting with user-specific data mitigates those attacks
- Exposed file system path (`/instance`) to simulate server misconfig

---

## 📁 Project Structure

```
flask_blog/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── auth.py
│   ├── static/
│   └── templates/
├── instance/
│   └── blog.db
├── shell/
│   └── createUser.py
├── run.py
├── config.py
└── README.md
```

---

## 🧪 User Roles

| Role    | Permissions |
|---------|-------------|
| `admin` | Manage users, posts, and can access security-sensitive features |
| `author` | Create and edit their own posts |
| `normal` | Can read, comment, like/dislike posts |

---

## 🛡 Password Hashing Logic

```python
hashlib.md5((raw_password + f"{user.id}Ferdowsi").encode()).hexdigest()
```

- Uses MD5 + static salt pattern `"Ferdowsi"`
- Based on `user.id`, making hashes unique per user

---

## 🧰 Setup Instructions

### 1. 📦 Install dependencies
```bash
pip install flask flask_sqlalchemy flask_wtf
```

### 2. 🛠 Initialize the database
```bash
python
>>> from app import create_app, db
>>> app = create_app()
>>> app.app_context().push()
>>> db.create_all()
```

### 3. 👤 Create an admin user
```python
from app.models import User
admin = User(username='admin', password='temp', role='admin')
db.session.add(admin)
db.session.commit()
admin.password = admin.hash_password_with_salt('admin123')
db.session.commit()
```

### 4. ▶️ Run the app
```bash
python run.py
```

---

## 🌐 URLs

| Route | Purpose |
|-------|---------|
| `/` | Homepage with posts |
| `/login` | Login page |
| `/logout` | Logout |
| `/create` | New post (author/admin) |
| `/admin/users` | Manage users (admin only) |
| `/instance` | Intentionally exposed directory |

---

## 🧪 Brute Force & Rainbow Table Demo

### Create Rainbow Table
```bash
python generate_rainbow_table.py
```

### Offline Attack on `blog.db`
```bash
python rainbow_crack_db.py
```

---

## ⚠️ Disclaimer

> This application is intentionally vulnerable and should **never be used in production**. It is designed purely for educational purposes in a controlled environment to demonstrate security risks and best practices.

---

## 📄 License

MIT License. Feel free to modify for educational use.

---

## 🙌 Credits

Made with ❤️ for Flask Security Labs & Network Security Demos  
Salt inspiration: **Ferdowsi** 🏛️
