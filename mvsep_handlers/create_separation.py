import requests
import json

def create_separation(path_to_file, api_token):
    files = {
        'audiofile': open(path_to_file, 'rb'),
        'api_token': (None, api_token),
        'sep_type': (None, '9'),
        'add_opt1': (None, '0'),
        'add_opt2': (None, '1'),
        'output_format': (None, '1'),
        'is_demo': (None, '1'),
    }
    response = requests.post('https://mvsep.com/api/separation/create', files=files)
    response_content = response.content

    # Преобразование байтового массива в строку
    string_response = response_content.decode('utf-8')

    # Парсинг строки в JSON
    parsed_json = json.loads(string_response)

    # Вывод результата
    hash = parsed_json["data"]["hash"]

    return hash, response.status_code
