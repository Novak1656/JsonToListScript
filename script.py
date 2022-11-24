import json
from sys import argv


class JsonToList:
    def __init__(self, json_path: str):
        self.json_path = json_path
        self.result_list = set()

    def upload_json(self) -> dict:
        try:
            with open(self.json_path, 'r') as json_file:
                if json_file.name.endswith('.json'):
                    return json.load(json_file)
                raise Exception('Укажите путь к json файлу!')
        except Exception as error:
            raise Exception(f'{error}')

    def list_iter(self, lst: list) -> None:
        for elm in lst:
            if isinstance(elm, dict):
                self.dict_iter(elm)
            elif isinstance(elm, list):
                self.list_iter(elm)
            else:
                self.result_list.add(elm)

    def dict_iter(self, data: dict) -> None:
        for key, value in data.items():
            self.result_list.add(key)
            if isinstance(value, dict):
                self.dict_iter(value)
            elif isinstance(value, list):
                self.list_iter(value)
            else:
                self.result_list.add(value)

    def convert_to_list(self) -> list:
        self.dict_iter(data=self.upload_json())
        return list(self.result_list)


if __name__ == '__main__':
    if len(argv) == 1:
        file_path = input('Введите путь к файлу где расположен JSON:\n')
    else:
        file_path = argv[1]
    jtl = JsonToList(json_path=file_path)
    j_list = jtl.convert_to_list()
    print(j_list)
