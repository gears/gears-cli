import os

from gears.assets import build_asset
from gears.environment import Environment
from gears.exceptions import FileNotFound
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
        for path in self.environment.public_assets:
            try:
                asset = build_asset(self.environment, path)
            except FileNotFound:
                continue
            self.environment.save_file(path, str(asset))
            source_path = os.path.relpath(asset.absolute_path)
            output_path = os.path.relpath(os.path.join(self.environment.root, path))
            print('- compiled %s to %s' % (source_path, output_path))
