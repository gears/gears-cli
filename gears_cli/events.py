from clint.textui import puts
from clint.textui import colored

from watchdog.events import FileSystemEventHandler


class WatchEventHandler(FileSystemEventHandler):

    def __init__(self, callback):
        self.callback = callback

    def on_modified(self, event):
        puts()
        puts(colored.yellow('assets modified, recompiling...'))
        self.callback()
