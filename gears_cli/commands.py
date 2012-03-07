import os
import time

from gears.assets import build_asset
from gears.environment import Environment
from gears.exceptions import FileNotFound
from gears.finders import FileSystemFinder

from watchdog.observers import Observer
from .events import WatchEventHandler


def get_absolute_path(path):
    return os.path.normpath(os.path.abspath(os.path.join(os.getcwd(), path)))


class BaseCommand(object):

    def __init__(self, args):
        self.args = args
        self.init_environment()

    def init_environment(self):
        self.environment = Environment(get_absolute_path(self.args.output))
        self.environment.finders.register(FileSystemFinder([get_absolute_path(self.args.source)]))
        self.environment.register_defaults()

    def compile(self):
        for path in self.environment.public_assets:
            try:
                asset = build_asset(self.environment, path)
            except FileNotFound:
                continue
            self.environment.save_file(path, str(asset))
            source_path = os.path.relpath(asset.absolute_path)
            output_path = os.path.relpath(os.path.join(self.environment.root, path))
            print('- compiled %s to %s' % (source_path, output_path))


class CompileCommand(BaseCommand):

    def run(self):
        self.compile()


class WatchCommand(BaseCommand):

    def run(self):
        event_handler = WatchEventHandler(self.compile)
        observer = Observer()
        observer.schedule(event_handler, path=self.args.source, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
