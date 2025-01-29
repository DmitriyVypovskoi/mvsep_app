# mvsep_app
MVSep application

## Как запустить exe с параметрами из командной строки
```
# Получить типы разделения
main.exe get_types

# Создать раделение с заданными параметрами
main.exe create_separation path/to/file.mp3 your_api_token separation_type add_opt1 add_opt2

# Конкретный пример с параметрами
main.exe create_separation {путь до файла} {ваш токен} 55 1 0

# Получить результат (файлы) разделения на рабочий стол
main.exe get_result hash
```
## Как работать со скриптом через консольное приложение

```
# Так выглядит начальный вывод
Select a function to execute:
1. Get separation types
2. Create separation
3. Get the separation result
q. Quit
Enter your choice:
```

## Соответственно, если вы хотите получить все типы разделений - нажмите -> 1

## Если вы хотите создать разделение - нажмите -> 2
```
Enter some parameters for separation:
Path to file: {путь до файла и нажмите Enter}
...
API token: {ваш API-токен}
...
Separation type: {тип разделения (если не знаете, выполните команду "Get separation types")}
...
Additional options. If you don't select anything, the default value is 0
Additional option 1: {дополнительный параметр 1 (если не знаете, выполните команду "Get separation types")}
...
Additional option 2: {дополнительный параметр 2 (если не знаете, выполните команду "Get separation types")}
...
# После заполнения всех параметров, вы получаете хэш разделения. Ожидайте выполнения программы, если файл не скачался можете выполнить команду ("Get the separation result")
Hash of your separation:  20250129191004-2f7b60bb90-5stafamily.mp3
Wait response from server
...
# После завершения загрузки вы увидите соответствующее сообщение
File '5stafamily_phantom_centre_model_mt_0_similarity.wav' uploaded successfully!
```

## Если у вас есть хэш разделения и вы хотите скачать его - нажмите -> 3
```
Enter hash for get separation:
Hash: {хэш разделения}
```


