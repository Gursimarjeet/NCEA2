#Docstring = Gursimrjeet Singh = Graphics Card Information
#imports
import sqlite3
#contants and variables
DATABASE = 'Graphics.db'


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

def print_all_Price():
    '''This function will print all the prices in the database'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM GraphicCardInfo ORDER BY Price DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through results and print them
    print(f"Manufacturer        GPU_Model                Vram_Size    Price(NZD)   Clock_Speed")
    for result in results:
        print(f"{result[1]:<20}{result[2]:<25}{result[3]:<15}{result[4]:<10}{result[5]}")
    #loop finish
    db.close()
def print_all_Clock_Speed():
    '''This function will print all the Clock Speeds in the database'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM GraphicCardInfo ORDER BY Clock_Speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through results and print them
    print(f"Manufacturer        GPU_Model                Vram_Size    Price(NZD)   Clock_Speed")
    for result in results:
        print(f"{result[1]:<20}{result[2]:<25}{result[3]:<15}{result[4]:<10}{result[5]}")
    #loop finish
    db.close()
def print_all_Vram_Size():
    '''This function will print all the VRAM Sizes in the database'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = sql = """
    SELECT * FROM GraphicCardInfo 
    ORDER BY CASE Vram_Size
        WHEN '32GB GDDR7'  THEN 1
        WHEN '16GB GDDR7'  THEN 2
        WHEN '16GB GDDR6'  THEN 3
        WHEN '12GB GDDR6X' THEN 4
        WHEN '12GB GDDR6'  THEN 5
        WHEN '8GB GDDR7'   THEN 6
        WHEN '8GB GDDR6'   THEN 7
        ELSE 8
    END ASC;
    """
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
    User = input("""
What would you like to do?
1. print all manufacturers
2. print all prices (Highest to lowest)
3. print all clock speeds (Highest to lowest)
4. print all VRAM sizes (Highest to lowest)
5. exit
 """)
    if User == '1':
        print_all_Manufacturer()
    if User == '2':
        print_all_Price()
    if User == '3':
        print_all_Clock_Speed()
    if User == '4':
        print_all_Vram_Size()
    if User == '5':
        print("Thank You")
        break
    else:
        print("Invalid input, please try again.")
        break

