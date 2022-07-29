import json
import pathlib
from datetime import datetime

json_data = list()

class Logger:

    def write_to_json(self, data):
        file_name = 'temp_weather.json'
        path = pathlib.Path(file_name)
        json_data.append(data)
        with open(file_name, 'w+') as file:
                json.dump(json_data, file)
        print(f"Data write to file with name - {file_name}")

    def write_to_console(self, id, message):
        print(f"To id {id} send message - {message}")

    def write_register_id(self, id):
        print(f"ID {id} register in chat on {datetime.now().strftime('%H:%M:%S')}")
