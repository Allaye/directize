import argparse
from config import directory, description, version

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="directize", description='CLI for directize package usage')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + version)
    parser.add_argument('-d', '--directory', type=str, choices=directory.keys(), help='choose a directory type to create')
    args = parser.parse_args()
    print(args)
