from .counter_daemon import CounterDaemon

import rumps

class DisplayApp(rumps.App):
    def __init__(self, counter: CounterDaemon):
        super(DisplayApp, self).__init__(type(self).__name__)
        self.counter = counter

    @rumps.timer(1)
    def show_count(self, _):
        self.title = f"{self.counter.get_count()}"
