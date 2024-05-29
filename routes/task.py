from fastapi import APIRouter
from models.task import Task 
from config.db import conn 
from schemas.task import serializeDict, serializeList
from bson import ObjectId
task = APIRouter() 

@task.get('/')
async def find_all_tasks():
    return serializeList(conn.local.task.find())

@task.get('/{id}')
async def find_one_task(id):
    return serializeDict(conn.local.task.find_one({"_id":ObjectId(id)}))

@task.post('/')
async def create_task(task: Task):
    conn.local.task.insert_one(dict(task))
    return serializeList(conn.local.task.find())

@task.put('/{id}')
async def update_task(id,task: Task):
    conn.local.task.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(task)
    })
    return serializeDict(conn.local.task.find_one({"_id":ObjectId(id)}))

@task.delete('/{id}')
async def delete_task(id,task: Task):
    return serializeDict(conn.local.task.find_one_and_delete({"_id":ObjectId(id)}))