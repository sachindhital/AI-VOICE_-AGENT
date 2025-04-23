import sqlite3

def clear_cars_table(db_path="auto_db.sqlite"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cars")
    conn.commit()
    conn.close()
    print("🧹 All car records have been deleted.")

if __name__ == "__main__":
    clear_cars_table()