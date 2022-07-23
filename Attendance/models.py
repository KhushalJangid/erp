from ast import Str
import pymongo
from regex import D

# Create your models here.

_client = pymongo.MongoClient("mongodb://localhost:27017/") # connection node for mongoDB

_db = _client["Attendance"] # The database to use

'''
Schema :
Database(Attendance) => Collection(Class_Section) => Document (Per day attendance)
Database(Attendance) => Collection(Faculty) => Document (Per day attendance)
document = {
    _id: ...,
    date : 01/01/2001,
    attendance :{
            studentA : 1,
            studentB : 1,
            studentC : 0,
            .
            .
            .
        }
'''

class Collection():
    '''
    Table/Collection Class. 
    Used to create Collection Objects; Apply CRUD operations on the Collection.
    Arguments : Collection Name (String)
    '''
    
    def __init__(self,collectionName) -> None:
        self._collectionName = collectionName
        self._collection = _db[self._collectionName]
        
    def insert(self,data):
        try:
            if type(data) is dict:
                if "date" in data.keys() and "attendance" in data.keys():
                    obj = self._collection.insert_one(data)
                    return obj
                else :
                    return ValueError("Invalid data")
            else:
                raise ValueError("Expected a Dictionary object")
        except Exception as e:
            raise RuntimeError(e)
    
    def get(self,date : str) :
        '''Retrieve one day attendance'''
        try:
            if type(date) is str :
                obj = self._collection.find_one({"date":date})
                return obj
            else:
                raise ValueError("Undefined values or fields")
        except Exception as e:
            raise RuntimeError(e)
    
    def filter(self,_from:str,_to:str):
        '''Params = {"from":date(),"to":date(),"student":id}'''
        try:
            chunk = self._collection.find({"date":{"$gte":_from,"$lte":_to}})
            return chunk
        except Exception as e:
            raise RuntimeError(e)
    
    def update(self,date:str,*args):
        try:
            if type(args) is dict:
                obj = self._collection.find_one({"date":date})
                data = obj["attendance"]
                data.update(args)
                obj["attendance"] = data
                return self._collection.insert_one(obj)
            else:
                raise ValueError("Expected a Dictionary object")
        except Exception as e:
            raise RuntimeError(e)
    
    def delete(self):
        pass
