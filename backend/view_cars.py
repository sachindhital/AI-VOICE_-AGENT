import sqlite3

def show_all_cars(db_path="auto_db.sqlite"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("🚫 No cars found in the database.")
    else:
        print("🚗 Cars in database:")
        for vin, make, model, year in rows:
            print(f"- VIN: {vin}, Make: {make}, Model: {model}, Year: {year}")

if __name__ == "__main__":
    show_all_cars()
