#Docstring = Gursimrjeet Singh = Graphics Card Information
#imports
import sqlite3
#contants and variables
DATABASE = 'Graphics'


#functions
def print_all_Manufacturer():
    '''This function will print all the manufacturers in the database'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM GraphicCardInfo;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through results and print them
    print(f"Manufacturer        GPU_Model                Vram_Size    Price(NZD)   Clock_Speed")
    for result in results:
        print(f"{result[1]:<20}{result[2]:<25}{result[3]:<15}{result[4]:<10}{result[5]}")
    #loop finish
    db.close()

#main code
while True:
    User = input("\nWhat would you like to do? \n1. print all manufacturers \n2. exit")
    if User == '1':
        print_all_Manufacturer()
    if User == '2':
        print("Thank You")
        break
    else:
        print("Invalid input, please try again.")
        break

