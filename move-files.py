import os
import shutil
import time

file_source = 'testfolder1/'
file_dest = 'testfolder2/'


class Observer:

    def __init__(self, source, dest):
        self._running = True
        self.source = source
        self.dest = dest

    def check_dir(self):
        files = os.listdir(self.source)
        if files:
            for item in files:
                shutil.move(self.source + item, self.dest)
                print(item + ' was moved.')
        else:
            pass

    def start_watcher(self):
        while self._running:
            self.check_dir()
            time.sleep(1)

    def terminate(self):
        self._running = False


newfolder1 = Observer(file_source, file_dest)

try:
    print('Script is running.')
    newfolder1.start_watcher()

except KeyboardInterrupt:
    print('It is done!')
    newfolder1.terminate()
