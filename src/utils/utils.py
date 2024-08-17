import json
import os


class Utils:
    @staticmethod
    def load_json(file: str):
        with open(file, "r") as f:
            return json.load(f)

    @staticmethod
    def save_json(file: str, data: object) -> None:
        with open(file, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def clear_screen() -> int:
        # windows
        if os.name == "nt":
            return os.system("cls")

        return os.system("clear")  # mac, linux
