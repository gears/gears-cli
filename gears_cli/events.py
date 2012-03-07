from watchdog.events import FileSystemEventHandler


class WatchEventHandler(FileSystemEventHandler):

    def __init__(self, callback):
        self.callback = callback

    def on_modified(self, event):
        print('')
        print('assets modified, recompiling...')
        self.callback()
