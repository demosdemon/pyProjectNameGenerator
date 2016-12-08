# coding=utf-8

import argparse

from . import generate


def alliterative_type(string):
    if string:
        return string[0]
    return True


def main():
    parser = argparse.ArgumentParser(description="Generates a random Heroku like project name")
    parser.add_argument('-w', '--words', metavar='N', type=int, help="The number of words to generate", default=2)
    parser.add_argument('-n', '--numbers', action='store_true', help="Generate random digits at the end")
    parser.add_argument('-a', '--alliterative', metavar='C', type=alliterative_type, const=True, default=False,
                        nargs='?', help="Generate an alliterative string of words")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--dashed', action='store_true', help='Output only the dashed result')
    group.add_argument('-s', '--spaced', action='store_true', help='Output only the spaced result')
    group.add_argument('-r', '--raw', action='store_true', help='Output the raw results separated by newlines')

    args = parser.parse_args()

    results = generate(args.words, args.numbers, args.alliterative)

    if args.dashed:
        print(results['dashed'])
    elif args.spaced:
        print(results['spaced'])
    elif args.raw:
        print('\n'.join(results['raw']))
    else:
        print('Raw: {}'.format(repr(results['raw'])))
        print('Dashed: {}'.format(results['dashed']))
        print('Spaced: {}'.format(results['spaced']))
