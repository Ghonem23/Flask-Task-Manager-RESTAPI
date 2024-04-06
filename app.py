from flask import Flask, request
from appservice import AppService
import json

app = Flask(__name__)

task_list = [{
    "id": 1,
    "Task name": "Coding",
    "Due Date": "05-11-2024"    
}] 

appService = AppService(task_list);

@app.route("/")
def home():
    return "Welcome to REST API"

@app.route("/user_tasks")
def get_user_tasks():
    return appService.get_tasks()

@app.route("/create_task", methods= ['POST'])
def create_task():
    request_data = request.get_json()
    task = request_data ['task']
    return appService.create_task(task)

@app.route("/update_task/<int:id>", methods= ['PUT'])
def update_task(id):
    request_data = request.get_json()
    return appService.update_task(id, request_data['task'])


@app.route("/delete_task/<int:id>", methods=['DELETE'])
def delete_task(id):
    return appService.delete_task(id)

if __name__ == "__main__":
    app.run(debug=True)