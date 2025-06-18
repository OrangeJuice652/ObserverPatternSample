from fire_and_forget.import_result import ImportResult
from fire_and_forget.observers import IObserver
from typing import List, Optional
from queue import Queue
from threading import Thread


class Subject:
    def __init__(self, observers: Optional[List[IObserver]] = None):
        self.observers = observers if observers else []
        self.queue = Queue()
        self.thread = Thread(target=self.worker, daemon=True)
        self.thread.start()

    def attach_observer(self, observer: IObserver):
        self.observers.append(observer)

    def detach_observer(self, number: int):
        try:
            self.observers.pop(number)
        except IndexError:
            print(f"Can't detach {number}th observer")

    def notify(self, import_result: ImportResult):
        for observer in self.observers:
            self.queue.put((observer, import_result))

    def worker(self):
        while True:
            observer, import_result = self.queue.get()
            if observer is None and import_result is None:
                self.queue.task_done()
                break
            observer.commit(import_result)
            self.queue.task_done()

    def worker_stop(self):
        self.queue.put((None, None))
        self.thread.join()

