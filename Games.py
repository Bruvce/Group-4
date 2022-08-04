import mysql.connector
import sys

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="shop"
    )

    print("success")
    
except:
    print("Failed Connection")
    sys.exit()  

cursor = connection.cursor()

class Games:

    def ViewAllGames(self):
        cursor.execute("SELECT * FROM games")
        result = cursor.fetchall()
        
        for x in result:
            print("Name:", x[0], "\tPublisher:", x[1])
            print("Genre:", x[2], "\tYear:", x[3], "\tMain Character:", x[4])
            print("\n")    

    def ViewGamesbyGenre(self, genre_type):
        cmd = "SELECT * FROM games WHERE Genre=%s"
        genre = (genre_type,)
        cursor.execute(cmd, genre)
        result=cursor.fetchall()
        
        for x in result:
            print("Name:", x[0], "\tPublisher:", x[1])
            print("Genre:", x[2], "\tYear:", x[3], "\tMain Character:", x[4])
            print("\n") 
        
