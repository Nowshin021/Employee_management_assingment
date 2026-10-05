import sqlite3
import csv
import os

# Path to SQLite database file
db_path = "SQLite.db"  
output_dir = "csv_files"

os.makedirs(output_dir, exist_ok=True)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
tables = cursor.fetchall()

print(f"Found {len(tables)} tables. Exporting...")

for (table_name,) in tables:
    cursor.execute(f'SELECT * FROM "{table_name}"')
    rows = cursor.fetchall()
    headers = [col[0] for col in cursor.description]
    
    csv_path = os.path.join(output_dir, f"{table_name}.csv")
    with open(csv_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
        
    print(f" Exported: {table_name}.csv ({len(rows)} rows)")

conn.close()
print("All tables successfully exported with headers!")

