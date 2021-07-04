1- Correr el docker-compose.yml de afuera (crea el contenedor de rabbitmq)
2- Entrar en micro-drf/admin 
  2.1- ejecutar docker-compose up backend
  2.2- ejecutar docker-compose exec backend sh
  2.3- ejecutar python manage.py makemigrations
  2.4- ejecutar python manage.py migrate
  2.5- Esto crear las tablas en la base de datos del microservicio de django
3- Entrar en micro-flasl/main
  3.1- ejecutar docker-compose up backend
  3.2- ejecutar docker-compose exec backend sh
  3.3- ejecutar python manager.py db init
  2.4- ejecutar python manager.py db migrate
  2.5- Esto crear las tablas en la base de datos del microservicio de flask
4- Probar los endpoints en Postman:
  - GET, POST           http://localhost:8000/api/products
  - DELETE, PUT, GET    http://localhost:8000/api/products/<id>
  - GET                 http://localhost:8000/api/user
  - GET                 http://localhost:8001/api/products
  - POST                http://localhost:8001/api/products/<id>/like