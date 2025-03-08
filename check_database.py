import os

# Path to your SQLite database file
db_path = 'projects.db'

# Check if the file exists
if os.path.exists(db_path):
    print(f"The database file {db_path} exists.")
else:
    print(f"The database file {db_path} does not exist.")
