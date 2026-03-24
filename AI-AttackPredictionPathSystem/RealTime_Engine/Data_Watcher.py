import time
from pathlib import Path


class DataWatcher:
    def __init__(self, watch_path: Path, interval=3):
        self.watch_path = watch_path
        self.interval = interval
        self.last_state = self._snapshot()

    def _snapshot(self):
        return {
            f: f.stat().st_mtime
            for f in self.watch_path.glob("*")
            if f.is_file()
        }

    def has_changed(self):
        current_state = self._snapshot()
        if current_state != self.last_state:
            self.last_state = current_state
            return True
        return False
        
    def watch(self):
        try:
            while True:
                if self.has_changed():
                    yield True
                time.sleep(self.interval)
        except KeyboardInterrupt:
            return

