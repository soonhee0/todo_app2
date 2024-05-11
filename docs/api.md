## API設計

### 1.タスクの取得
Path: /api/todo/tasks  
Method: GET  
Request Body:'{}'  
Responce Body:  
    
 ``` {  
  "tasks": [  
    {  
      "id": 1,  
      "title": "shopping",  
      "deadline": "2024-05-15",  
      "status_id": 1  
    },  
    {  
      "id": 2,  
      "title": "Finish project",  
      "deadline": "2024-05-20",  
      "status":2  
    }  
  ]  
} ```

### 2.タスク作成    
Path:- '/api/todo/tasks'    
Method: POST    
Request Body:    
```{  
  "tasks": [  
    {  
      "id": 3,  
      "title": "shopping",  
      "deadline": "2024-05-17",  
      "status_id": 1  
    }  
  ]  
}  ```
Responce Body:  
    
 ``` {  
  "tasks": [  
    {  
      "id": 1,  
      "title": "shopping",  
      "deadline": "2024-05-15",  
      "status_id": 1  
    },  
    {  
      "id": 2,  
      "title": "Finish project",  
      "deadline": "2024-05-20",  
      "status":2  
    },  
    {  
      "id": 3,  
      "title": "shopping",  
      "deadline": "2024-05-17",  
      "status_id": 1  
    }  
  ]  
}```
### 3.特定のタスク取得  
Path:- '/api/todo/tasks/{task_id}'   
Method: GET  
Request Body:'{}'  
Responce Body:(task_idが1のデータをGETする場合)  
 ``` {  
  "tasks": [  
    {  
      "id": 1,  
      "title": "shopping",  
      "deadline": "2024-05-15",  
      "status_id": 1  
    },  
  ]  
} ```
### 4.タスク更新:   
Path: '/api/todo/tasks/{task_id}'  
Method: PUT  
Request Body:  
```{  
  "tasks": [  
    {  
      "id": 3,  
      "title": "buy flower",  
      "deadline": "2024-05-17",  
      "status_id": 1  
    }    
  ]  
} ```
Responce Body:  
    
 ``` {  
  "tasks": [  
    {  
      "id": 1,  
      "title": "shopping",  
      "deadline": "2024-05-15",  
      "status_id": 1  
    },  
    {  
      "id": 2,  
      "title": "Finish project",  
      "deadline": "2024-05-20",  
      "status":2  
    },  
    {  
      "id": 3,  
      "title": "buy flower",  
      "deadline": "2024-05-17",  
      "status_id": 1  
    }  
  ]  
} ```   
### 5.タスク削除  
Path:- '/api/todo/tasks/{task_id}'   
Method: DELETE
Request Body:'{}'
Responce Body:(task_idが3のデータをDELETEする場合)
``` {  
  "tasks": [  
    {  
      "id": 1,  
      "title": "shopping",  
      "deadline": "2024-05-15",  
      "status_id": 1  
    },  
    {  
      "id": 2,  
      "title": "Finish project",  
      "deadline": "2024-05-20",  
      "status":2  
    },  
   
  ]  
}  ```
 
