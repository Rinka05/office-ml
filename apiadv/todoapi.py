from fastapi import FastAPI
import uvicorn

# Create FastAPI app instance
app = FastAPI(title="simple todo api", version="1.0.0")

todos = []

counter = 1
# GET endpoint to fetch todos
@app.get("/todos")
def get_todos():
    print("making todos")
    return todos
@app.post("/todos", status_code = 201)
def create_todo(title:str , description : str = "", completed : bool =False):
    global counter
    new_todo = {
        "id":counter,
        "title":title,
        "description":description,
        "completed":completed
    }
    todos.append(new_todo)
    counter += 1
    return new_todo


#get specific todo by id
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return None


todos = [
    {"id": 1, "task": "Buy groceries"},
    {"id": 2, "task": "Study FastAPI"},
    {"id": 3, "task": "Go for a walk"},
    {"id": 4, "task": "Read a book"},
]


@app.put("/todos/{todo_id}")
def update_todo(todo_id:int , title:str = None , description : str = None , completed : bool = None):
    for todo in todos:
        if todo["id"] == todo_id:
            if title is not None:
                todo["title"] = title
            if description is not None:
                todo["description"] = description
            if completed is not None:
                todo["completed"] = completed
            return todo
    return None
                





# Run the app when the script is executed directly
if __name__ == "__main__":
    print("making todos")
    uvicorn.run(app, host="127.0.0.1", port=8000)


