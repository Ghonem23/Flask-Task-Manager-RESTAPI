import json

class AppService:
    def __init__(self, task_list):
        self.task_list = task_list

    def get_tasks(self):
        return self.task_list
    
    def create_task(self,task):
        self.task_list.append(task)
        return self.task_list
    
    def update_task(self, id, request_task):
        for task in self.task_list:
            if task["id"] == id: 
                task.update(request_task)
                return self.task_list
        return {'message': 'task id not found'}
 
    def delete_task(self, request_task_id):
        for task in self.task_list:
            if task["id"] == request_task_id:
                self.task_list.remove(task)
                return self.task_list
        return ({'message': 'task id not found'});