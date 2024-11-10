from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Service(ABC):
    @abstractmethod
    def validate(self, data: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    def send(self, query: Dict[str, Any]) -> int:
        pass