import os
from time import sleep

from utils import Utils

type Data = dict[str, list[dict[str, str | int]]]


def get_unique_name(data: Data) -> str:
    while True:
        name = str(input("name: "))

        if not any(user["name"] == name for user in data["users"]):
            return name

        print("You cant use that name choose another one.")


def is_valid_password(password: str, size: int) -> tuple[str | None, bool | None]:
    if size <= 7:
        return "Password must be more at least 8 characters", None

    return None, True


def get_password() -> str:
    while True:
        password = str(input("password: "))

        msg, is_valid = is_valid_password(password, len(password))

        if is_valid is None:
            print(msg)
            continue

        return password


def signup_menu():
    if os.path.exists("data.json"):
        data: Data = Utils.load_json("data.json")
    else:
        data = {"users": []}

    name = get_unique_name(data)
    password = get_password()

    id = len(data["users"]) + 1

    user = {"name": name, "password": password, "id": id}

    sleep(5)

    data["users"].append(user)

    Utils.save_json("data.json", data)


def main() -> None:
    while True:
        Utils.clear_screen()

        print("[1] - SignIn")
        print("[2] - SignUp\n")

        try:
            option = int(input("> "))
        except ValueError:
            print("You only can use numbers")
            sleep(2)
            main()

        match option:
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
