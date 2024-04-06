# Flask Task Manager API

## Description

This project is a simple REST API built with Flask for managing tasks. It allows users to create, retrieve, update, and delete tasks stored in an in-memory list.

## Features

- CRUD operations for task management
- In-memory data storage

## Technologies

- Python
- Flask

## Setup

To run this project, install it locally using pip:

$ pip install -r requirements.txt
$ python app.py


## API Endpoints

- `GET /user_tasks` - Retrieves all tasks
- `POST /create_task` - Creates a new task
- `PUT /update_task/<int:id>` - Updates an existing task
- `DELETE /delete_task/<int:id>` - Deletes a task

## How to Use

To use this API, send HTTP requests to the endpoints listed above. The request and response format is JSON.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.