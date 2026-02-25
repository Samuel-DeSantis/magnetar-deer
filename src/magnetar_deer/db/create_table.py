from sqlalchemy import Table, Column, Integer, insert, select

from magnetar_deer.db.engine import engine, metadata
from magnetar_deer.db.utils import map_type

# fields = {"name": "string", "age": "integer", "salary: "float"}

def create_table(name: str, fields: dict):
    columns = [Column("id", Integer, primary_key=True)]

    for field_name, field_type in fields.items():
        columns.append(Column(field_name, map_type(field_type)))

    table = Table(name, metadata, *columns)
    metadata.create_all(engine)
    return table

users_table = {
    "name" : "Users",
    "fields": {
        "name": "string",
        "age": "integer",
    }
}

users = create_table(users_table["name"], users_table["fields"])

def add_test_users(table):
    with engine.connect() as conn:
        conn.execute(insert(table), [
            {"name": "John", "age": 30},
            {"name": "Jane", "age": 24}
        ])
        conn.commit()

def read_all_users(table):
    with engine.connect() as conn:
        result = conn.execute(select(table))
        rows = result.fetchall()

        print("\nUsers:")
        for row in rows:
            print(dict(row._mapping))

# add_test_users(users)
read_all_users(users)