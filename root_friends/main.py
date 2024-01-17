from .counter_daemon import CounterDaemon
from .display_app import DisplayApp
from .api import CounterAPI

import threading
import uvicorn

counter = CounterDaemon()
server = CounterAPI(counter)

def serve():
    uvicorn.run(server, port=8096)

def start_threads():
    # カウンター
    thread1 = threading.Thread(target=counter.listen)
    # APIサーバー
    thread2 = threading.Thread(target=serve)

    thread1.start()
    thread2.start()

if __name__ == "__main__":
    start_threads()
    app = DisplayApp(counter)
    app.run()
