import os

from gears.environment import Environment
from gears.finders import FileSystemFinder


def get_absolute_path(path):
    return os.path.normpath(os.path.abspath(os.path.join(os.getcwd(), path)))


class CompileCommand(object):

    def __init__(self, args):
        self.args = args
        self.init_environment()

    def init_environment(self):
        self.environment = Environment(get_absolute_path(self.args.output))
        self.environment.finders.register(FileSystemFinder([get_absolute_path(self.args.source)]))
        self.environment.register_defaults()

    def run(self):
        self.environment.save()


def compile(parser, args):
    environment = Environment(get_absolute_path(args.output))
    environment.finders.register(FileSystemFinder([get_absolute_path(args.source)]))
    environment.register_defaults()
    environment.save()
