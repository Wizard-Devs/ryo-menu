from time import sleep
import os

from utils import Utils

utils = Utils()


def signup_menu():
    if os.path.exists("data.json"):
        users = utils.load_json("data.json")
    else:
        users = {
            "users": []
        } 

    name = str(input("name: "))
    password = str(input("password: "))

    user = {
        "name": name,
        "password": password,
        "id": len(users["users"]) + 1
    }
    
    users["users"].append(user)
    
    utils.save_json("data.json", users) 


def main() -> None:
    while True:
        utils.clear_screen()

        print("[1] - SignIn")
        print("[2] - SignUp\n")
        
        try:
            option = int(input("> "))
        except ValueError:
            print("You only can use numbers")
            sleep(2) 
            main()
            
        match(option):
            case 1:
                # signin_menu()
                ...
            case 2:
                signup_menu()
            case _:
                print("Option not available")
                sleep(2)
                main()


        
if __name__ == "__main__":
    main()



