import sqlalchemy
from sqlalchemy import create_engine, inspect

# 1. Connect to SQLite database using SQLAlchemy
engine = create_engine('sqlite:///Chinook.db')

# 2. Introspect schema (list all tables)
inspector = inspect(engine)
tables = inspector.get_table_names()

print('=== Database Connection Successful ===')
print(f'Total Tables Found: {len(tables)}')
print('Tables in Chinook Database:')
for table in tables:
    print(f' - {table}')

# 3. Inspect columns of a core business table
print('\n=== Columns in Customer Table ===')
columns = inspector.get_columns('Customer')
for col in columns:
    print(f" - {col['name']} ({col['type']})")
