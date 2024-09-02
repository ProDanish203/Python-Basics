from fastapi import APIRouter, HTTPException
from models.todo import Todo, TodoUpdate
from config.db import todos_collection
from schemas.todo import TodosSchema, TodoSchema
from bson import ObjectId, errors as bson_errors
from pymongo import errors as mongo_errors

todo = APIRouter()


@todo.get("")
def get_todos():
    try:
        todos = todos_collection.find()
        return {"message": "List of todos", "data": TodosSchema(todos), "success": True}
    except mongo_errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@todo.post("")
def create_todo(todo: Todo):
    try:
        result = todos_collection.insert_one(dict(todo))
        created_todo = todos_collection.find_one({"_id": result.inserted_id})
        return {
            "message": "Todo created successfully",
            "success": True,
            "data": TodoSchema(created_todo),
        }
    except mongo_errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Failed to create todo: {str(e)}")


@todo.patch("/{todo_id}")
def update_todo(todo_id: str, todo: TodoUpdate):
    try:
        update_data = {k: v for k, v in todo.dict().items() if v is not None}
        if not update_data:
            return {"message": "No valid update data provided", "success": False}

        result = todos_collection.update_one(
            {"_id": ObjectId(todo_id)}, {"$set": update_data}
        )

        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Todo not found")

        if result.modified_count == 0:
            return {"message": "Todo found, but no changes were made", "success": True}

        return {"message": "Todo updated successfully", "success": True}
    except bson_errors.InvalidId:
        raise HTTPException(status_code=400, detail="Invalid todo ID format")
    except mongo_errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Failed to update todo: {str(e)}")


@todo.delete("/{todo_id}")
def delete_todo(todo_id: str):
    try:
        result = todos_collection.delete_one({"_id": ObjectId(todo_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Todo not found")
        return {"message": "Todo deleted successfully", "success": True}
    except bson_errors.InvalidId:
        raise HTTPException(status_code=400, detail="Invalid todo ID format")
    except mongo_errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete todo: {str(e)}")
