import mysql.connector
from mysql.connector import Error
import pandas as pd

connection = None
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="user",
        passwd="abababa"
    )
    print("MySQL Database connection successful")
except Error as err:
    print(f"Error: '{err}'")
