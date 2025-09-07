
-----------kafka------
docker run -d -p 9092:9092 --name kafka apache/kafka:latest

-----------mongo-----------
docker pull mongodb/mongodb-community-server:latest

docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest