from root_friends.counter_daemon import CounterDaemon
from root_friends.core import Core

import rumps

class DisplayApp(rumps.App):
    def __init__(self, counter: CounterDaemon):
        super(DisplayApp, self).__init__(type(self).__name__)
        self.counter = counter
        self.core = Core()

    @rumps.timer(1)
    def show_count(self, _):
        count = self.counter.get_count()
        lv = self.core.calc_lv(count)
        self.title = f"lv: {lv} [{count}]"
