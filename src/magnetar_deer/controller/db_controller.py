'''
Docstring for magnetar_deer.controller.db_controller

Goal: Add CRUD (Create, Read, Update, Delete) commands to controller to interface between the DB and terminal

# Controller Methods 
Controller.create_table(...)

Controller.insert(...)

Controller.select(...)

Controller.update(...)

Controller.delete(...)
'''

class Table:
    pass # This is a type placeholder for SQLalchemy Table

class Controller:
    
    def create_table(self, name: str, columns: dict) -> Table:
        pass

    def insert(self, table: Table, record: dict) -> None: 
        pass # Enable multi insertion of records?

    def select(self, table: Table) -> list: 
        pass # How do we want to query? add .where, .order_by or keep general

    def update(self, table: Table, id: int) -> None:
        pass

    def delete(self, table: Table, id: int) -> None:
        pass