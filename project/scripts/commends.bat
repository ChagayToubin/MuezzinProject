
-----------kafka------
docker run -d -p 9092:9092 --name kafka apache/kafka:latest

--------elastic---------------
docker run -d --name es -p 9200:9200 `
-e "discovery.type=single-node" `
-e "xpack.security.enabled=false" `
-e "ES_JAVA_OPTS=-Xms1g -Xmx1g" `
docker.elastic.co/elasticsearch/elasticsearch:8.15.0

-----------mongo-----------
docker pull mongodb/mongodb-community-server:latest

docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest