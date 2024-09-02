def TodoSchema(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "title": item["title"],
        "description": item["description"],
        "completed": item["completed"],
    }


def TodosSchema(items) -> list:
    return [TodoSchema(item) for item in items]
