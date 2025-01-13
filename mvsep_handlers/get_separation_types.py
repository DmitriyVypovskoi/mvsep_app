import requests
import ast
import json


def get_separation_types():
    # URL для запроса
    api_url = 'https://mvsep.com/api/app/algorithms'

    # Делаем GET-запрос
    response = requests.get(api_url)

    # Проверяем статус-код ответа
    if response.status_code == 200:
        # Парсим ответ в JSON
        data = response.json()
        
        # Теперь можем работать с данными
        for algorithm in data:
            render_id = algorithm['render_id']
            name = algorithm['name']
            algorithm_group_id = algorithm['algorithm_group_id']
            
            # Дополнительные поля
            algorithm_fields = algorithm['algorithm_fields']
            for field in algorithm_fields:
                field_name = field['name']
                field_text = field['text']
                field_options = field['options']
                
            # Описания алгоритма
            algorithm_descriptions = algorithm['algorithm_descriptions']
            for description in algorithm_descriptions:
                short_desc = description['short_description']
                # long_desc = description['long_description']
                lang = description['lang']
            
            # Печать данных для примера
            print(f"{render_id}: {name}, Group ID: {algorithm_group_id}")
            print(f"\tField Name: {field_name}, Field Text: {field_text}, Options: {field_options}")
            # print(f"\tShort Description: {short_desc}, Long Description: {long_desc}, Language: {lang}\n")
    else:
        print(f"Request failed with status code: {response.status_code}")