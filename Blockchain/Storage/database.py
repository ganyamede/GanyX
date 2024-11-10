from .interfaces import IDataRepository
from pymongo import MongoClient
from pymongo.collection import Collection
from typing import List, Dict, Any
from .config import MONGO_URL
import certifi

class MongoService(IDataRepository):
    def __init__(self, db_name: str, collection_name: str):
        self.client = MongoClient(MONGO_URL, tlsCAFile=certifi.where())  
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert(self, data: Dict[str, Any]) -> str:
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def select(self, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        return list(self.collection.find(query))

    def delete(self, query: Dict[str, Any]) -> int:
        result = self.collection.delete_many(query)
        return result.deleted_count

    def update(self, query: Dict[str, Any], update_data: Dict[str, Any]) -> int:
        result = self.collection.update_many(query, {'$set': update_data})
        return result.modified_count

    def close(self):
        self.client.close()