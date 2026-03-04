from sqlalchemy import Table, Column, Integer, insert, select

from magnetar_deer.db.engine import engine, metadata
from magnetar_deer.db.utils import map_type

# fields = {"name": "string", "age": "integer", "salary: "float"}

def table_builder(name: str, fields: dict):
    '''
    Create a new table dynamically

    Parameters:
        name (str): Name of the table
        fields (dict): Dictionary of table columns and their respective data types 
        
    Returns:
        Table: SQLAlchemy object
    '''
    columns = [Column("id", Integer, primary_key=True)]

    for field_name, field_type in fields.items():
        columns.append(Column(field_name, map_type(field_type)))

    table = Table(name, metadata, *columns)
    metadata.create_all(engine)
    return table

