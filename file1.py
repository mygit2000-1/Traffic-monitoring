import os
import psycopg2

# ❌ Bad practice (DO NOT DO THIS)
password = "super_secret_password"

# ✅ Recommended practice: use environment variables
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")  # stored securely outside the code
db_host = "localhost"
db_name = "mydatabase"

try:
    conn = psycopg2.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        database=db_name
    )
    print("Connection successful!")
except Exception as e:
    print("Connection failed:", e)
