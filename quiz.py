def show_menu():
    print("1. Ask Questions")
    print("2. Add a Question")
    print("3. Exit Game")
    
    option = input("Enter Option: ")
    return option
    
def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You selected 'Ask Questions'")
        elif option == "2":
            print("You selected 'Add a Question'")
        elif option == "3":
            break
        else:
            print("Ivalid Option")
        print("")
        
game_loop()