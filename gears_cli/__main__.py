import argparse
import sys
from .commands import CompileCommand


def get_command(args):
    parser = argparse.ArgumentParser(description='CLI for Gears.')
    subparsers = parser.add_subparsers(help='commands')

    compile_parser = subparsers.add_parser('compile')
    compile_parser.add_argument('source')
    compile_parser.add_argument('output')
    compile_parser.set_defaults(_command_class=CompileCommand, _parser=compile_parser)

    args = parser.parse_args(args)
    return args._command_class(args)


def run(args=sys.argv[1:]):
    get_command(args).run()


if __name__ == '__main__':
    run()
