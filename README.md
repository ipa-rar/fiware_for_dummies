# Fiware: Orion Context Broker

- The Orion Context Broker is a service that based on the OMA NGSI 9/10 standard and can handle sending and receiving contextual information. 
- Primarily, to handle a large number of messages from entities and manage updates, queries, and also handle data subscriptions from the entities. 

- Currently, the Orion Context Broker relies on open source MongoDB technology to keep persistence of the context data it holds. Therefore, the architecture will consist of two elements:

    - The Orion Context Broker server which will receive requests using NGSI
    - The underlying MongoDB database associated to the Orion Context Broker server

Since all interactions between the two elements are initiated by HTTP requests, the entities can be containerized and run from exposed ports. 

![](https://fiware.github.io/tutorials.Getting-Started/img//architecture.png)

## Getting started
````
docker pull mongo:3.6
docker pull fiware/orion
docker network create fiware_default
````

## MongoDB
- mongoDB is the NoSQL database used to store context data
````
docker run -d --name=context-db --network=fiware_default  --expose=27017 mongo:3.6 --bind_ip_all --smallfiles
````
## Orion context broker
- The Orion Context Broker can be started and connected to the network with the following command:
````
docker run -d --name orion  --network=fiware_default -p 1026:1026  fiware/orion -dbhost context-db
````
To check if the Orion context broker is running, make a HTTP request to exposed port `1026`

````
curl -X GET http://localhost:1026/version
````
which returns us 
````
{
"orion" : {
  "version" : "3.0.0-next",
  "uptime" : "0 d, 0 h, 43 m, 35 s",
  "git_hash" : "686c4f10cb647eab70a674cfaa88ca7977b53223",
  "compile_time" : "Wed May 12 13:30:11 UTC 2021",
  "compiled_by" : "root",
  "compiled_in" : "46c2c05dcde4",
  "release_date" : "Wed May 12 13:30:11 UTC 2021",
  "machine" : "x86_64",
  "doc" : "https://fiware-orion.rtfd.io/",
  "libversions": {
     "boost": "1_66",
     "libcurl": "libcurl/7.61.1 OpenSSL/1.1.1g zlib/1.2.11 nghttp2/1.33.0",
     "libmicrohttpd": "0.9.70",
     "openssl": "1.1",
     "rapidjson": "1.1.0",
     "mongoc": "1.17.4",
     "bson": "1.17.4"
  }
}
}
````
- **GET** - Obtaining Version Information
````
curl --location --request GET 'http://localhost:1026/version/'
````
- **GET** - Retrieving context information
````
curl --location --request GET 'http://localhost:1026/v2/entities'
````



