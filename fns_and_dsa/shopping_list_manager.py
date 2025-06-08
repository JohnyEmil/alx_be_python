def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"Added '{item}' to the list.")
    else:
        print("Item name cannot be empty.")  

def remove_item(shopping_list):
    item = input("Enter item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"remove '{item}' from the list.")
    else:
        print(f"'{item}' is not found in the list")
        
def display_list(shopping_list):
    if shopping_list:
        for i,item in enumerate(shopping_list, 1):
            print(f"{i}.{item}")
    else:
        print("\nShopping list is empty")        
    

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item(shopping_list)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            remove_item(shopping_list)
            pass
        elif choice == '3':
            # Display the shopping list
            display_list(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()