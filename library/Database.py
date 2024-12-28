import mysql.connector
from Variables import Variables
import pandas as pd

class Database:
    def __init__(self,database):
        
        try:
            self.conn = mysql.connector.connect(
                host = Variables("host").get_variable(),
                port =  Variables("port").get_variable(),
                user =  Variables("user").get_variable(),
                password =  Variables("password").get_variable(),
                database = database
            )
            if self.conn.is_connected():
                print("Successfully connected to MySQL!")
        
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")
        
    def execute_query(self,query):
        df = pd.read_sql(query,self.conn)
        return df

    def disconnect(self):
        self.conn.close()

    def fetch(self):
        pass


db = Database("bct2077")
df = db.execute_query("SELECT * FROM teacher")
df.to_csv("output.csv")
db.disconnect()