from tabulate import tabulate

# inside the class, read_data functions is defined to use the try statement to open the text file and read the data
# 5 objects of the class have been created to store the data from the text file so to be able to use them seperately.
class Shoe:
    def __init__(self):
        self.country = []
        self.code = []
        self.product = []
        self.cost = []
        self.quantity = []

    def read_data(self):
        store_inventory = []
        try:
            with open("inventory.txt", "r") as f:
                for lines in f.readlines():
                    line = lines.strip("\n").split(",")
                    if "Country" in line:
                        pass
                    else:
                        store_inventory.append(line)
        except FileNotFoundError as error:
            print(error)
        
        for inventory in store_inventory:
            self.country.append(inventory[0])
            self.code.append(inventory[1])
            self.product.append(inventory[2])
            self.cost.append(inventory[3])
            self.quantity.append(int(inventory[4]))
        
        return store_inventory
    
# A method for to allow the user to search by code has been created  
    def search_by_code(self):
        store_inventory = self.read_data()
        search = input("Please enter the product code you are searching for: ").upper()
        for inventory in store_inventory:
            if search in inventory:
                print(f"{inventory[0]} {inventory[1]} {inventory[2]} {inventory[3]} {inventory[4]}")

# A method to check for the lowest item or ptoduct and ask the user to order more.  
    def lowest(self):
        shoe_inventory = self.read_data()
        quantity = self.quantity
        quantity.sort()
    
        for inventory in shoe_inventory:
            if str(quantity[0]) in inventory:
                print(f"Please order more of {inventory[2]}.")

# A method to check the highest item and as to place the item for sale.
    def highest(self):
        shoe_inventory = self.read_data()
        quantity = self.quantity
        quantity.sort()
        
        for inventory in shoe_inventory:
            if str(quantity[-1]) in inventory:
                print(f"Please put {inventory[2]} up for sale.")

# A method to calculate the calue of each item and print it out
    def value_per_item(self):
        shoes = []
        with open("inventory.txt", "r") as f:
            for lines in f.readlines():
                line = lines.strip("\n").split(",")
                if "Country" in line:
                    pass
                else:
                    shoes.append(line)
        
        for item in shoes:
            value = int(item[3]) * int(item[4])
            item.append(str(value))
            print("Product: " + item[2])
            print("value : " + str(value))
            print("\n")
        
        return shoes

# A method to view all the data in a table format has been created.
    def view_all_products(self):
        new_list = self.value_per_item()
        print(tabulate(new_list, headers = ["Country", "Code", "Product", "Cost", "Quantity", "Value"]))


# A loop of the menu has been created so the user can check the data they wish to check and an exit has been created to end the loop.
while True:
    print("\n")
    menu = input('''Please select from the menu below:
          1 - Search product by code
          2 - Check for lowest product quantity
          3 - Check for highest product quantity
          4 - Calculate each product value
          5 - View all data related to products
          6 - Exit
          : ''')
    
    if menu == "1":
        manager = Shoe()
        manager.search_by_code()
    elif menu == "2":
        manager = Shoe()
        manager.lowest()
    elif menu == "3":
        manager = Shoe()
        manager.highest()
    elif menu == "4":
        manager = Shoe()
        manager.value_per_item()
    elif menu == "5":
        manager = Shoe()
        manager.view_all_products()
    elif menu == "6":
        print("Goodbye!!")
        exit()
    else:
        print("Invalid input")