import pyodbc
from dataclasses import dataclass

@dataclass
class Database:
    def __init__(self, database: str, driver: str = "SQL Server", server: str = "SPTWGIS00001") -> pyodbc.Connection:
        conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};CHARSET=UTF8;ansi=True"
        self.cnxn = pyodbc.connect(conn_str)
        self.cursor = self.cnxn.cursor()   
  
