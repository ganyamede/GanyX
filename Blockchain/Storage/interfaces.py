from abc import ABC, abstractmethod
from typing import List, Dict, Any

class IDataRepository(ABC):
    @abstractmethod
    def insert(self, data: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    def select(self, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def delete(self, query: Dict[str, Any]) -> int:
        pass

    @abstractmethod
    def update(self, query: Dict[str, Any], update_data: Dict[str, Any]) -> int:
        pass