import os
import json
import requests

def download_file(url, filename, save_path):
    """
    Скачать файл по указанному URL и сохранить его в указанном пути.
    """
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(save_path, filename), 'wb') as f:
            f.write(response.content)
        print(f"Файл '{filename}' успешно загружен!")
    else:
        print(f"Произошла ошибка при загрузке файла '{filename}'. Код ошибки: {response.status_code}.")

def get_result(hash):
    params = {'hash': hash}
    response = requests.get('https://mvsep.com/api/separation/get', params=params)
    data = json.loads(response.content.decode('utf-8'))

    if data['success']:
        files = data['data']['files']
        save_path = os.path.expanduser('~/Desktop')  # Путь к рабочему столу
        for file_info in files:
            url = file_info['url'].replace('\\/', '/')  # Исправление неверного слэша
            filename = file_info['download']  # Имя файла для сохранения
            download_file(url, filename, save_path)
    else:
        print("Произошла ошибка при получении данных о файлах.")