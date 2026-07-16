import json
def read_config(path: str):
# Made used build-in library json
# tries to open file prints error message otherwise and program closes
# tries to read json file prints error message otherwise and closes program
    try:
        with open(path) as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                # assert("Invalid JSON foramt!")
                raise ValueError("Invalid JSON foramt! Please try again")
    except FileNotFoundError:
        raise FileNotFoundError("File not found! Please try again")