import os
import json
import requests

def download_file(url, filename, save_path):
    """
    Download the file from the specified URL and save it in the specified path.
    """
    response = requests.get(url)

    if response.status_code == 200:
        with open(os.path.join(save_path, filename), 'wb') as f:
            f.write(response.content)
        print(f"File '{filename}' uploaded successfully!")
    else:
        print(f"There was an error loading the file '{filename}'. Status code: {response.status_code}.")

def get_result(hash):
    params = {'hash': hash}
    response = requests.get('https://mvsep.com/api/separation/get', params=params)
    data = json.loads(response.content.decode('utf-8'))

    if data['success']:
        try:
            files = data['data']['files']
        except:
            print("The separation is not ready yet")
            return None
        save_path = os.path.expanduser('~/Desktop')  # Путь к рабочему столу
        for file_info in files:
            url = file_info['url'].replace('\\/', '/')  # Исправление неверного слэша
            filename = file_info['download']  # Имя файла для сохранения
            download_file(url, filename, save_path)
    else:
        print("An error occurred while retrieving file data.")