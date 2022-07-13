from ast import Str
import pymongo

# Create your models here.

_client = pymongo.MongoClient("mongodb://localhost:27017/") # connection node for mongoDB

_db = _client["Attendance"] # The database to use

'''
Schema :
Database(Attendance) => Collection(Faculty_id) => Document (Per day attendance)
document = {
    _id: ...,
    date : 01/01/2001,
    data : [
        {section : A,
        year : 1st
        branch : all,
        attendance : {
            studentA : 1,
            studentB : 1,
            studentC : 0,
            .
            .
            .
        }},
        {section : B,
        year : 1st,
        branch : all,
        attendance : {
            .
            .
            .
        } 
        },
        {section : A,
        year : 2,
        branch : EE,
        attendance : {
            studentA : 1,
            studentB : 1,
            studentC : 0,
            .
            .
            .
        }},
    ]
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
        if data is dict:
            obj = self._collection.insert_one(data)
            return obj
        else:
            raise ValueError("Expected a Dictionary object")
    
    def get(self,params):
        '''Retrieve one day attendance'''
        if params is dict and "date" in params.keys :
            obj = self._collection.find_one(params)
            return obj
        else:
            raise ValueError("Undefined values or fields")
    
    def filter(self,params):
        '''Params = {"from":date(),"to":date(),"student":id}'''
        chunk = self._collection.find(params)
        pass
    
    def delete(self):
        pass

    def update(self):
        pass