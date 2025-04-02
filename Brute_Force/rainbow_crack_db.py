import sqlite3

# === FILE PATHS ===
BLOG_DB = "blog.db"     
RAINBOW_DB = "rainbow.db"          

# === STEP 1: Connect to both DBs ===
blog_conn = sqlite3.connect(BLOG_DB)
rainbow_conn = sqlite3.connect(RAINBOW_DB)

blog_cursor = blog_conn.cursor()
rainbow_cursor = rainbow_conn.cursor()

# === STEP 2: Fetch users and their hashes ===
blog_cursor.execute("SELECT username, password FROM user")
users = blog_cursor.fetchall()

print("🕵️‍♂️ Cracking passwords from blog.db using rainbow.db...")

# === STEP 3: Try to match hashes to rainbow passwords ===
cracked = []

for username, md5_hash in users:
    rainbow_cursor.execute("SELECT password FROM rainbow WHERE hash = ?", (md5_hash,))
    result = rainbow_cursor.fetchone()

    if result:
        cracked.append((username, result[0]))
        print(f"✅ {username}: {result[0]}")
    else:
        print(f"❌ User: {username} with Pass hash: {md5_hash} ==> Not found in rainbow table")

# === STEP 4: Cleanup ===
blog_conn.close()
rainbow_conn.close()

print("🎉 Done. Cracked", len(cracked), "passwords.")
