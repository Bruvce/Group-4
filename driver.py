import mysql.connector
import sys
from Movies import Movies
from Games import Games

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

def menu():
    print("====Welcome to the E-Commerce Storefront====")
    print("0. Exit")
    print("1. Login")
    
def menu1():
    print("=====Menu=====")
    print("1. Browse Inventory")
    print("2. View Cart")
    print("3. Logout")
    
def Inv_menu():
    print("====Inventory====")
    print("1. View All")
    print("2. View by Genre")
    print("3. View All Movies")
    print("4. View All Games")
    print("5. Back")

games_db = Games()
movies_db = Movies()
menu()   
option = int(input("Enter the desired option: "))

while option != 0:
    if option == 1: 
        #leads into login menu
        print("Option 1 chosen", "\n")
        
       # while option1 == 1: #building login menu1
        menu1()
        choice = int(input("Which would you like to do? "))
        
        # all this errors and idk how to fix it. :.(    
        
        while choice != 4:
            if choice == 1:
                #not sure how to open inventory
                tf = False
                while tf == False:
                    print("\n")
                    Inv_menu()
                    opt1 = int(input("Enter the desired option: "))
                
                    if opt1 == 1:
                        print("\n")
                        games_db.ViewAllGames()
                        movies_db.ViewAllMovies()
                        
                    elif opt1 == 2:
                        print("\n")
                        print("1. Games or 2. Movies")
                        num1 = int(input("Your choice: "))
                        print("\n")
                        list = ("Fighting", "Action", "Adventure", "Platform")
                        if num1 == 1:
                            print("1. Fighting  2. Action\n3. Adventure  4. Platform")
                            num2 = int(input("Your choice: "))
                            print("\n")
                            genre = list[num2-1]
                            games_db.ViewGamesbyGenre(genre)
                        elif num1 == 2:
                            print("1. Fighting   2. Action   3. Adventure")
                            num2 = int(input("Your choice: "))
                            print("\n")
                            genre = list[num2-1]
                            movies_db.ViewMoviesbyGenre(genre)
                    
                    elif opt1 == 3:
                        print("\n")
                        movies_db.ViewAllMovies()
                    
                    elif opt1 == 4:
                        print("\n")
                        games_db.ViewAllGames()

                    elif opt1 == 5:
                        tf == True
                        break
                        
                    else: print("input proper number")
                break

                    


            elif choice == 2:
                #not sure what function to call for info
                print("\n")
                print("Viewing My Info")
                print("\n")
                break
                   
            elif choice == 3: 
                #Not sure what function to call to view Cart
                print("\n")
                print("Viewing Cart")
                print("\n")
                break
                
            elif choice == 4: 
                menu()
            
    elif option == 2: #still main menu
        #creates an account 
        print("Option 2 chosen")
        break
    else: #still min menu
        print("\n", "Invalid option.", "\n")
        menu()
        option = int(input("Enter the desired option: "))
