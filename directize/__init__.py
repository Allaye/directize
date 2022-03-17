import argparse
from config import directory, description, version

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="directize", description='CLI for directize package usage')
    parser.add_argument('-d', '--directory', type=str, choices=directory.keys(), help='choose a directory type to create', required=True)
    parser.add_argument('-d', '--directory', help='directory to directize', required=True)
    args = parser.parse_args()
    print(args)
