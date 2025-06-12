from fastapi import FastAPI
app = FastAPI()

task =[{"tasks":"Reading","description": "Read the book"},
       {"tasks":"Writing","description": "Writing some thing"},
       {"tasks":"Listening", "description": "Listening some thing"},
       {"tasks":"Speaking","description": "Speaking to someone"}]
@app.get("/task_name")
def task(tasks):
    for task_name in tasks:
        if task_name["tasks"]==tasks:
            return task_name["description"]
  
 

