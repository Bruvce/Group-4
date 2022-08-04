import mysql.connector
import sys

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="shop"
    )

    print("Movies Connected to Driver")
    
except:
    print("Failed Connection")
    sys.exit()  

cursor = connection.cursor()

class Movies:

    def ViewAllMovies(self):   
        cursor.execute("SELECT * FROM movies")
        result = cursor.fetchall()
        
        for x in result:
            print("Name:", x[0], "\tDirector:", x[1])
            print("Genre:", x[2], "\tYear:", x[3], "\tMain Character:", x[4])
            print("\n")

    def ViewMoviesbyGenre(self, genre_type):
        cmd = "SELECT * FROM movies WHERE Genre=%s"
        genre = (genre_type,)
        cursor.execute(cmd, genre)
        result=cursor.fetchall()
        
        for x in result:
            print("Name:", x[0], "\tDirector:", x[1])
            print("Genre:", x[2], "\tYear:", x[3], "\tMain Character:", x[4])
            print("\n")

    def getCartMovies(self):
        cmd = ("SELECT Name FROM movies")
        cursor.execute(cmd)
        result = cursor.fetchall()
        return result

    def addMovietoCart(self, name):
        cmd = ("SELECT * FROM movies WHERE Name=%s")
        name1 = (name,)
        cursor.execute(cmd, name1)
        result=cursor.fetchall()

        for x in result:
            print("Name:", x[0], "\tDirector:", x[1])
            print("Genre:", x[2], "\tYear:", x[3], "\tMain Character:", x[4])
            print("\n") 

        yn = input("Add this movie to your cart? y/n:")
        if yn == "y":
            qty = int(input("Quantity to add: "))
            cmd = "INSERT INTO cart(Name, Quantity, Price) VALUES (%s, %s, %s)"
            price = 9.99
            info = (name, qty, price)
            cursor.execute(cmd, info)
            connection.commit()
            print(qty, "items added to cart")
        elif yn == "n":
            return False
