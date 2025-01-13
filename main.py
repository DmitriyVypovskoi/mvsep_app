import sys
from mvsep_handlers import get_separation_types, create_separation, get_result

def main():
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

if __name__ == "__main__":
    main()