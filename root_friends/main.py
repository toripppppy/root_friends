from root_friends.counter_daemon import CounterDaemon
from root_friends.display_app import DisplayApp
from root_friends.api import CounterAPI

import threading
import uvicorn

# キータイプ数カウンター
counter = CounterDaemon()
# APIサーバー
server = CounterAPI(counter)
# メニューバー表示アプリ
app = DisplayApp(counter)

def serve():
    uvicorn.run(server, port=8096)

def start_threads():
    thread1 = threading.Thread(target=counter.listen)
    thread2 = threading.Thread(target=serve)
    thread1.start()
    thread2.start()

if __name__ == "__main__":
    start_threads()
    app.run()
