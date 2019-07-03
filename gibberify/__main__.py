"""
Main entry point of gibberify
"""

import os
import sys
import argparse
import json

# local imports
from .config import __real_langs__, __gib_langs__
from .utils import __version__, __data__
from .gibberify import gibberify, parse_message, interactive
from .gui import gui


def main():
    # Parse arguments (also gives you help automatically with -h)
    parser = argparse.ArgumentParser(prog='gibberify',formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description='Gibberify is simple gibberish generator.\n'
                                                 'Run without arguments to use the graphical interface.')
    parser.add_argument('--interactive', '-i', dest='inter', action='store_true',
                        help='run in interactive mode')
    parser.add_argument('--from-lang', '-fl', dest='lang_in', type=str, default='en',
                        help='language to translate from')
    parser.add_argument('--to-lang', '-l', dest='lang_out', type=str, default='orc',
                        help='language to translate into')
    parser.add_argument('--message', '-m', type=parse_message, nargs='*',
                        help='text to translate. If a filename is given, the '
                             'contents of the file will be translated to stdout. '
                             'If `-` is given, input text is take from stdin')
    parser.add_argument('--version', action='store_true',
                        help='display version information and exit')
    args = parser.parse_args()

    if args.version:
        print(f'Gibberify {__version__}')
        exit()

    # if no arguments were given, run gui version
    graphical = False
    if len(sys.argv) == 1:
        graphical = True

    if graphical:
        gui()
    elif args.inter:
        interactive()
    else:
        translator = dicts[args.lang_in][args.lang_out]
        print(gibberify(translator, ' '.join(args.message)))


if __name__ == '__main__':
    main()
