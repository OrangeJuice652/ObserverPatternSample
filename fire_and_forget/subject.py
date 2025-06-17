from fire_and_forget.import_result import ImportResult
from fire_and_forget.observers import IObserver
from typing import List
from queue import Queue
from threading import Thread
import time


class Subject:
    def __init__(self, observers: List[IObserver]=[]):
        self.observers = observers
        self.queue = Queue()
        self.thread = Thread(target=self.worker)
        self.thread.start()

    def attach_observer(self, observer: IObserver):
        self.observers.append(
            observer
        )

    def detach_observer(self, number: int):
        try:
            self.observers.pop(number)
        except IndexError:
            print(f'Cant detach {number}th observer')

    def notify(self, import_result: ImportResult):
        for observer in self.observers:
            self.queue.put((observer, import_result))

    def worker(self):
        while True:
            observer, import_result = self.queue.get()
            time.sleep(1)
            observer.commit(import_result)
            self.queue.task_done()

