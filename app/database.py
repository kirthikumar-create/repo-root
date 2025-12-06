import os

DATABASE_URL = os.getenv("DATABASE_URL")

def init_db():
    if DATABASE_URL:
        print("Connected to RDS Database:", DATABASE_URL)
    else:
        print("DATABASE_URL not found")
