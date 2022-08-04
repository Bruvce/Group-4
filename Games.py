import mysql.connector
import sys

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="shop"
    )

    print("Games Connected to Driver")
    
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

    def getCartGames(self):
        cmd = ("SELECT Name FROM games")
        cursor.execute(cmd)
        result = cursor.fetchall()
        return result

    def addGametoCart(self, name):
        cmd = ("SELECT * FROM games WHERE Name=%s")
        name1 = (name,)
        cursor.execute(cmd, name1)
        result=cursor.fetchall()

        for x in result:
            print("Name:", x[0], "\tPublisher:", x[1])
            print("Genre:", x[2], "\tYear:", x[3], "\tMain Character:", x[4])
            print("\n") 

        yn = input("Add this game to your cart? y/n:")
        if yn == "y":
            qty = int(input("Quantity to add: "))
            cmd = "INSERT INTO cart(Name, Quantity, Price) VALUES (%s, %s, %s)"
            price = 9.99
            info = (name, qty, price)
            cursor.execute(cmd, info)
            connection.commit()
            print(cursor.rowcount, "item added to cart")
        elif yn == "n":
            return False



        
