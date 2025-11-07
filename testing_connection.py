import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from clarifi_agent.core.database import SessionLocal
    from sqlalchemy import text
    
    def test_db_connection():
        try:
            db = SessionLocal()
            # Use text() wrapper for raw SQL
            result = db.execute(text("SELECT version()"))
            version = result.fetchone()
            print(f"Database connection successful!")
            print(f"Database version: {version[0]}")
            db.close()
            return True
        except Exception as e:
            print(f"Database connection failed: {e}")
            return False

    if __name__ == "__main__":
        test_db_connection()

except ImportError as e:
    print(f"Import error: {e}")