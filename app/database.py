import os

DATABASE_URL = os.getenv("DATABASE_URL")

def init_db():
    if DATABASE_URL:
        print("Connected to dummy RDS:", DATABASE_URL)
