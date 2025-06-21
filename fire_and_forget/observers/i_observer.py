from abc import ABC, abstractmethod
from fire_and_forget.import_result import ImportResult


class IObserver(ABC):
    @abstractmethod
    def commit(self, import_result: ImportResult):
        pass

