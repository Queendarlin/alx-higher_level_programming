import argparse

def main():
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('arg1', type=int, help='Description of arg1')
    parser.add_argument('arg2', type=float, help='Description of arg2')
    parser.add_argument('--arg3', type=str, default='default_value', help='Description of arg3 (optional)')

    args = parser.parse_args()

    # Access the values
    print(f'arg1: {args.arg1}')
    print(f'arg2: {args.arg2}')
    print(f'arg3: {args.arg3}')

if __name__ == "__main__":
    main()
