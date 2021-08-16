# ProjectS
## Introduction

This is a demo repository to test how to authentication using JWT in microservices. 

## Requirements
* Python3.6+
* Django>=2

## Run security service
1. Clone the project to your machine ```[git clone https://github.com/ranvijay-sachan/ProjectS.git]```
2. Navigate into the diretory ```[cd ProjectS]```
3. Install the dependencies ```[pip install -r requirements.txt]```
4. ```[cd security]```
5. ```[python manage.py migrate]```
6. Start the security server ```[python manage.py runserver 0.0.0.0:8000]```
7. Visit the application on the browser - [http:localhost:8000](http:localhost:8000)
8. Create superuser and users from Admin Pannel and create your custom permissions and assign to users
9. ```[curl -X POST -H "Content-Type: application/json" -d '{"username": "user", "password": "yourpass"}' http://127.0.0.1:8000/api/mytoken/]```
10. get Access token and validate in ```[https://jwt.io/]```
11. now we can use acess token in inventories api's Authorization header

## Run inventory service
1. Navigate into the diretory ```[cd ProjectS]```
2. ```[cd inventory]```
3. ```[python manage.py migrate]```
4. Start the security server ```[python manage.py runserver 0.0.0.0:8001]```
5. Visit the application on the browser - [http:localhost:8000](http:localhost:8001)
6. Create superuser if you want to access admin pannel otherwise not required
7. ```[curl -H GET -H "Content-Type: application/json" -H "Authorization: Bearer xxxxxxxxxxxxxx" http://127.0.0.1:8001/inventory/]```

