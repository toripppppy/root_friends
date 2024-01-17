from root_friends.counter_daemon import CounterDaemon
from root_friends.core import Core

from fastapi import FastAPI

class CounterAPI(FastAPI):
    def __init__(self, counter: CounterDaemon) -> None:
        super().__init__(counter=counter)
        self.counter = counter
        self.core = Core()

        @self.get("/count")
        async def get_count():
            return {"count": self.counter.get_count()}
        
        @self.get("/lv")
        async def get_lv():
            count = self.counter.get_count()
            return self.core.calc_lv(count)