from sqlalchemy import Table, insert, select, update, delete

from magnetar_deer.db.engine import engine, metadata
from magnetar_deer.db.table_builder import table_builder

class Controller:
    
    def create_table(self, name: str, columns: dict) -> Table:
        """
        Create a new database table

        users_table = {
            "name" : "Users",
            "fields": {
                "name": "string",
                "age": "integer",
            }
        }

        Parameters:
            name (str): Name of the table
            columns (dict): A dictionary of column-datatype pairs
        Returns:
            table (Table): SQLAlchemy Table object        
        """
        return table_builder(name, columns)

    def insert(self, table: Table, records: dict | list[dict]) -> None: 
        """
        Insert record into table

        Parameters:
            table (Table): SQLAlchemy Table object
            record (dict | list[dict]): Dictionary or list of dictionaries with column-value pairs

        Returns:
            Success/Fail
        """
        with engine.connect() as connection:
            connection.execute(insert(table), records)
            connection.commit()

    def select(self, table: Table) -> list: # TODO: Come up with a system for this... Param or method based?
        """
        Reads record(s) from table

        Parameters:

        Returns:
            Record(s)
        """
        with engine.connect() as connection:
            result = connection.execute(select(table))
            return result.fetchall() #Selects ALL records

    def update(self, table: Table, id: int, values: dict) -> None:
        """
        Update record

        Parameters:
            table (Table): SQLAlchemy table object
            id (int): ID of record to be updated
            values (dict): Dictionary of column-value pairs to update
        Returns:
            Record
        """
        with engine.connect() as connection:
            connection.execute(update(table).where(table.columns.id == id).values(**values))
            connection.commit()

    def delete(self, table: Table, id: int) -> None:
        """
        Delete specified record

        Parameters:
            table (Table): SQLAlchemy table object
            id (int): ID of record to be deleted
        
        Returns:
            Success/Fail
        """
        with engine.connect() as connection:
            connection.execute(delete(table).where(table.columns.id == id))
            connection.commit()