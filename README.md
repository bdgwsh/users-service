# users-service
Microservice for managing users via api 

## Requirements:
* Python 3.6.2 
* Pip 9.0.1 

## How to use
Install dependencies from file requirements.txt:
```pip3 install -r requirements.txt ```
Run the app by typing:
``` python3 run_app.py ```

### Api 
| Method  |        URI               | Description |
| ------- | ----------------- | -----------  |
| GET     |/users/            | Returns list of all users in json |
| POST    |/users/            | Adds a new user to database.    |
| PATCH   |/users/<user_id>   | Updates users's password with id <user_id>|           
| DELETE  |/users/<user_id>   | Deletes user with id <user_id>      |
| POST    |/auth/             | Checks user's login and password. Returns ```Status: 200 OK ``` if user exists and password is correct. In otherwise ```Status : 401 UNAUTHORIZED ```  |


By default it runs on http://127.0.0.1:8000
### Examples  
 
*GET /users/* 
```
    {
    "users": [
        {
            "id": 1,
            "login": "ultralogin"
        },
        {
            "id": 2,
            "login": "Anon"
        },
        {
            "id": 3,
            "login": "SUPER_ANON"
        },
        {
            "id": 4,
            "login": "new_user"
        },
        {
            "id": 5,
            "login": "losds"
        },
        {
            "id": 6,
            "login": "lossds"
        }
    ]
}
```

*POST /users/* sending data in json like 

 ```{ "login" : "new_user" , "password" : "passcode"}  ```
 
 returns  
 ``` 
{
    "id": 7,
    "login": "newsuperuser"
}  
 ```

If user already exists or there is no user with <user_id>
 ```  
{
    "user": null
}
 ```  


    
