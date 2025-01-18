import sys
import time
import argparse
from typing import Union
from mvsep_handlers import get_separation_types, create_separation, get_result


def parse_args(dict_args: Union[dict, None]) -> argparse.Namespace:
    """
    Parse command-line arguments for configuring the model, dataset, and training parameters.

    Args:
        dict_args: Dict of command-line arguments. If None, arguments will be parsed from sys.argv.

    Returns:
        Namespace object containing parsed arguments and their values.
    """
    parser = argparse.ArgumentParser(description="Console application for managing MVSEP separations.")
    subparsers = parser.add_subparsers(dest='command')

    # Подкоманда для получения типов разделения
    get_types_parser = subparsers.add_parser('get_types', help="Get available separation types.")
    get_types_parser.set_defaults(func=get_separation_types.get_separation_types)

    # Подкоманда для создания разделения
    create_separation_parser = subparsers.add_parser('create_separation', help="Create a new separation.")
    create_separation_parser.add_argument('path_to_file', type=str, help="Path to the file to be separated.")
    create_separation_parser.add_argument('api_token', type=str, help="API token for authentication.")
    create_separation_parser.add_argument('sep_type', type=str, help="Separation type.")
    create_separation_parser.add_argument('add_opt1', type=str, help="Additional option 1.")
    create_separation_parser.add_argument('add_opt2', type=str, help="Additional option 2.")
    create_separation_parser.set_defaults(func=lambda args: create_separation.create_separation(**vars(args)))

    # Подкоманда для получения результата разделения
    get_result_parser = subparsers.add_parser('get_result', help="Get the result of a previously created separation.")
    get_result_parser.add_argument('hash', type=str, help="Hash of the separation to retrieve.")
    get_result_parser.set_defaults(func=lambda args: get_result.get_result(vars(args)['hash']))

    if dict_args is not None:
        args = parser.parse_args([])
        args_dict = vars(args)
        args_dict.update(dict_args)
        args = argparse.Namespace(**args_dict)
    else:
        args = parser.parse_args()

    return args


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
            print("Separation type: ")
            sep_type = str(input())
            print("Additional options. If you don't select anything, the default value is 0")
            print("Additional option 1: ")
            add_opt1 = str(input())
            print("Additional option 2: ")
            add_opt2 = str(input())
            if '' not in [path_to_file, api_token, sep_type]:
                if add_opt1 == '':
                    add_opt1 = '0'
                if add_opt2 == '':
                    add_opt2 = '0'
                hash, response_code = create_separation.create_separation(path_to_file, api_token, sep_type, add_opt1, add_opt2)
                print("Hash of your separation: ", hash)
                print("Wait response from server")
                counter = 0
                while counter < 10:
                    response = get_result.get_result(hash)
                    if response:
                        break
                    else:
                        counter += 1
                        print('...')
                        time.sleep(10)
            else:
                print("Bad request")
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
    try:
        if len(sys.argv) > 1:
            args = parse_args(None)
            arguments = vars(args)
            args_to_func = []
            for value in arguments.values():
                args_to_func.append(value)
            if args_to_func[0] == 'create_separation':
                print(create_separation.create_separation(*args_to_func[1:-1]))
            if args_to_func[0] == 'get_types':
                get_separation_types.get_separation_types()
            if args_to_func[0] == 'get_result':
                get_result.get_result(args_to_func[1])
        else:
            manual_selection()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()