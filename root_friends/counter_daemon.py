from pynput.keyboard import Listener

class CounterDaemon:
    def __init__(self):
        self.count = 0

    def listen(self):
        print("start listen")
        with Listener(on_press=self.on_press) as listener:
            # start loop
            listener.join()

    def on_press(self, key):
        self.count += 1

    def get_count(self) -> int:
        return self.count
