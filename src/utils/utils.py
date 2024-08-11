import json
import os

type User = dict[str, str | int]

class Utils():
    def load_json(self, file: str):
        with open(file, "r") as f:
            return json.load(f)


    def save_json(self, file: str, user: User) -> None:
        with open(file, "w") as f:
            json.dump(user, f, indent=4)
            

    def clear_screen(self) -> None:
        # windows
        if os.name == "nt":
            return os.system("cls")

        return os.system("clear") # mac, linux
