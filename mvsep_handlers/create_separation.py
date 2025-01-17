import requests
import json

def create_separation(path_to_file, api_token, sep_type, add_opt1, add_opt2):
    files = {
        'audiofile': open(path_to_file, 'rb'),
        'api_token': (None, api_token),
        'sep_type': (None, sep_type),
        'add_opt1': (None, add_opt1),
        'add_opt2': (None, add_opt2),
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
