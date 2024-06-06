## API 設計

### 1.タスクの取得

Path: /api/todo/tasks  
Method: GET  
Responce Body:

 <!-- 11行目からのコード    -->

```{
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
     "status_id":2
   }
 ]
} 　　
```

<!-- コードブロック終了 -->

Response Header:  
'Content-Type:application/json'

### 2.タスク作成

Path:- '/api/todo/tasks'  
Method: POST  
Request Header:
'Content-Type: application/json'  
Request Body:

<!-- 39行目からのコード    -->

```
{
  "tasks": [
    {
      "id": 3,
      "title": "shopping",
      "deadline": "2024-05-17",
      "status_id": 1
    }
  ]
}
```

<!-- コードブロック終了 -->

Responce Body:

<!-- 55行目からのコード  -->

```
{
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
}
```

<!-- コードブロック終了 -->

Response Header:  
'Content-Type:application/json'

### 3.特定のタスク取得

Path:- '/api/todo/tasks/{task_id}'  
Method: GET  
Responce Body:(task_id が 1 のデータを GET する場合)

<!-- 91行目からのコード -->

```
 {
 "tasks": [
   {
     "id": 1,
     "title": "shopping",
     "deadline": "2024-05-15",
     "status_id": 1
   },
 ]
}
```

<!-- コードブロック終了 -->

Response Header:  
'Content-Type:application/json'

### 4.タスク更新:

Path: '/api/todo/tasks/{task_id}'  
Method: PUT  
Request Header:
'Content-Type: application/json'<br>
Request Body:

<!-- 114行目からのコード -->

```
{
  "tasks": [
    {
      "id": 3,
      "title": "buy flower",
      "deadline": "2024-05-17",
      "status_id": 1
    }
  ]
}
```

<!-- コードブロック終了 -->

Responce Body:

<!-- 129行目からのコード -->

```
{
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
}
```

<!-- コードブロック終了 -->

Response Header:  
'Content-Type:application/json'

### 5.タスク削除

Path:- '/api/todo/tasks/{task_id}'  
Method: DELETE<br>
Responce Body:(task_id が 3 のデータを DELETE する場合)

<!-- 165行目からのコード -->

```
 {
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
}
```

<!-- コードブロック終了 -->

Response Header:  
'Content-Type:application/json'
