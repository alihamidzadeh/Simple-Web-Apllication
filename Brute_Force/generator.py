import sqlite3
import hashlib
from tqdm import tqdm 

# === CONFIG ===
TEXT_FILE = "10-million-password-list-top-1000000.txt"
DB_FILE = "rainbow.db"

# === STEP 1: Create SQLite database and table ===
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS rainbow (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password TEXT NOT NULL,
        hash TEXT NOT NULL UNIQUE
    )
''')
conn.commit()

# === STEP 2: Read password file and insert hashes ===
with open(TEXT_FILE, 'r', encoding='utf-8', errors='ignore') as file:
    for line in tqdm(file, desc="Hashing and inserting"):
        password = line.strip()
        if password == '':
            continue
        md5_hash = hashlib.md5(password.encode()).hexdigest()

        try:
            cursor.execute("INSERT INTO rainbow (password, hash) VALUES (?, ?)", (password, md5_hash))
        except sqlite3.IntegrityError:
            # Ignore duplicates
            continue

conn.commit()
conn.close()

print(f"✅ Rainbow table generated and saved to {DB_FILE}")
