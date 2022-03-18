import argparse
from config import directory, description, version
from standard import standardproject

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="directize", description='CLI for directize package usage')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + version)
    parser.add_argument('-d', '--directorytype', type=str, choices=directory.keys(), help='choose a directory structure to create', required=True)
    parser.add_argument('-p', '--projectname', type=str, help='name of the project been created', required=False)
    args = parser.parse_args()
    print(args.projectname)
    standardproject(args.projectname)
