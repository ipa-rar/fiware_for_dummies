# FIWARE
- FIWARE is an open source initiative defining a universal set of standards for context data management which facilitate the development of Smart Solutions for different domains such as Smart Cities, Smart Industry, Smart Agrifood, and Smart Energy.
-  In any smart solution there is a need to gather and manage context information, processing that information and informing external actors, enabling them to actuate and therefore alter or enrich the current context.
- The FIWARE Context Broker component is the core component of any “Powered by FIWARE” platform. It enables the system to perform updates and access to the current state of context

<p align="center">
  <img  src="https://www.fiware.org/wp-content/uploads/2019/09/Screen-Shot-2019-09-25-at-15.30.33.png">
</p>

# Orion Context Broker
- Orion is a C++ implementation of the NGSIv2 REST API binding developed as a part of the FIWARE platform.
- The Orion Context Broker is an implementation of the Publish/Subscribe Context Broker, providing an NGSI interface. Using this interface, clients can do several operations:
  - Query context information. The Orion Context Broker stores context information updated from applications, so queries are resolved based on that information. Context information consists on entities (e.g. a car) and their attributes (e.g. the speed or location of the car).
  - Update context information, e.g. send updates of temperature
  - Get notified when changes on context information take place (e.g. the temperature has changed) 
  - Register context provider applications, e.g. the provider for the temperature sensor within a room


- Currently, the Orion Context Broker relies on open source MongoDB technology to keep persistence of the context data it holds. Therefore, the architecture will consist of two elements:

    - The Orion Context Broker server which will receive requests using NGSI v2
    - The underlying MongoDB database associated to the Orion Context Broker server

Since all interactions between the two elements are initiated by HTTP requests, the entities can be containerized and run from exposed ports. 

<p align="center">
  <img width="660" src="https://fiware.github.io/tutorials.Getting-Started/img//architecture.png">
</p>

# FIROS

<p align="center">
  <img src="https://raw.githubusercontent.com/iml130/firos/master/doc/media/firos.png">
</p>

## config.json
This contains all basic FIROS-Configuration-Parameters which can be manipulated by the user. 
````
{
    "environment": "test",

    "test": {
        "context_type": "MyRobotContextType",
        "server": {
            "port": 10100
        },
        "contextbroker": {
            "address": "192.168.0.97",
            "port": 1026,
            "subscription": {
                "throttling": "0",
                "subscription_length": 300,
                "subscription_refresh_delay": 0.9
            }
        },
        "endpoint": {
            "address": "10.16.55.3",
            "port": 1234
        },
        "log_level": "INFO"
    }
}
````
## robots.json
This json in particular listens to the rostopic ``/turtle1/pose `` with the message type ``"turtlesim/Pose"``  and sends all retreived data to the specified server in the Non-ROS-World. It publishes data into ``/turtle1/cmd_vel`` after receiving a notifcation of the server from the Non-ROS-World from type ``geometry_msgs/Twist``.
````
{
    "/turtle1/cmd_vel": ["geometry_msgs/Twist", "publisher"],
    "/turtle1/pose": ["turtlesim/Pose", "subscriber"]
}
````
### The publish-subscribe-terminology is at the Non-ROS-World 

<p align="center">
  <img width="460" src="https://firos.readthedocs.io/en/latest/media/pubsub-Illustration.png">
</p>

The green arrows are specified by the config.json (and whitelist.json). The corresponding black arrows are derived from the green arrows, which happens automatically.

## whitelist.json
As the name suggests, the whitelist.json functions as a whitelist to let FIROS know which messages it should keep track of. 
````
{
    "publisher": [".*/pose"],
    "subscriber": [".*/cmd_vel"]
}
````
<p align="center">
  <img width="550" src="images/architecture.PNG">
</p>


# Getting started 
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

# References
- [Swagger - FIWARE-NGSI v2 Specification](https://swagger.lab.fiware.org/#/)
- [NGSI-V2 step by step ](https://fiware-tutorials.readthedocs.io/en/latest/getting-started/index.html)
- [FIROS readthedocs](https://firos.readthedocs.io/en/latest/install/install.html)
- [Python request module - RealPython](https://realpython.com/python-requests/)
- [Intercommunication between ROS2 and FIWARE ](https://github.com/eProsima/FIROS2)
- [RMAP_EU - Robot agent node](https://github.com/ramp-eu/Robot_Agent_Node/tree/13f24632699c5ca9ede904a065326eacefabed6e)
- [RAMP](https://github.com/ramp-eu/RAMP/tree/master/logistics)

