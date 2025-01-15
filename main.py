import sys
import argparse
from mvsep_handlers import get_separation_types, create_separation, get_result

def parse_arguments():
    parser = argparse.ArgumentParser(description="Console application for managing MVSEP separations.")
    subparsers = parser.add_subparsers(dest='command')

    # Подкоманда для получения типов разделения
    get_types_parser = subparsers.add_parser('get_types', help="Get available separation types.")
    get_types_parser.set_defaults(func=get_separation_types.get_separation_types)

    # Подкоманда для создания разделения
    create_separation_parser = subparsers.add_parser('create_separation', help="Create a new separation.")
    create_separation_parser.add_argument('path_to_file', type=str, help="Path to the file to be separated.")
    create_separation_parser.add_argument('api_token', type=str, help="API token for authentication.")
    create_separation_parser.set_defaults(func=lambda args: create_separation.create_separation(args.path_to_file, args.api_token))

    # Подкоманда для получения результата разделения
    get_result_parser = subparsers.add_parser('get_result', help="Get the result of a previously created separation.")
    get_result_parser.add_argument('hash', type=str, help="Hash of the separation to retrieve.")
    get_result_parser.set_defaults(func=lambda args: get_result.get_result(args.hash))

    return parser.parse_args()

def manual_selection():
    while True:
        print("Select a function to execute:")
        print("1. Get separation types")
        print("2. Create separation")
        print("3. Get the separation result")
        print("q. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            get_separation_types.get_separation_types()
        elif choice == '2':
            print("Enter some parameters for separation:")
            print("Path to file: ")
            path_to_file = str(input())
            print("API token: ")
            api_token = str(input())
            if path_to_file != '' and api_token != '':
                print(create_separation.create_separation(path_to_file, api_token))
        elif choice == '3':
            print("Enter hash for get separation:")
            print("Hash: ")
            hash = str(input())
            if hash != '':
                print(get_result.get_result(hash))
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    # Сначала проверяем, были ли переданы аргументы командной строки
    if len(sys.argv) > 1:
        args = parse_arguments()
        args.func()
    else:
        manual_selection()

if __name__ == "__main__":
    main()