""" duplicates.py removes duplicates from a list """

import argparse
import sys


def parse_duplicates_arguments(args):
    """ Parses the arguments provided on the command-line """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        "--verbose", help="Verbose mode", action="store_true")

    parser.add_argument('--listone', nargs='+', type=str)
    parser.add_argument('--listtwo', nargs='+', type=str)

    arguments = parser.parse_args(args)
    return arguments, parser


def display_welcome_message():
    """ Display a welcome message """
    print("Duplicates removes duplicates from lists")
    print()


def remove_duplicates(list_one, list_two):
    """ Assumes that list_one and list_two are lists.
        Removes any element from list_one that also occurs in list_two """
    for element_one in list_one:
        if element_one in list_two:
            list_one.remove(element_one)


if __name__ == '__main__':
    display_welcome_message()
    # parse the arguments
    arguments, parser = parse_duplicates_arguments(sys.argv[1:])
    if arguments.verbose:
        print(arguments)
    if arguments.listone is not None and arguments.listtwo is not None:
        remove_duplicates(arguments.listone, arguments.listtwo)
        print("Removing the duplicates:")
        print()
        print("List one:", arguments.listone)
        print("List two:", arguments.listtwo)
        print()
