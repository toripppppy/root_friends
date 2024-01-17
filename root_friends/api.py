from fastapi import FastAPI
from .counter_daemon import CounterDaemon

class CounterAPI(FastAPI):
    def __init__(self, counter: CounterDaemon) -> None:
        super().__init__(counter=counter)
        self.counter = counter

        @self.get('/count')
        async def get_count():
            return {"count": self.counter.get_count()}