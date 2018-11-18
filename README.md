# Project Title

This a web application that allows users to create "feature requests".

A "feature request" is a request for a new feature that will be added onto an existing piece of software. Assume that the user is an employee at IWS who would be entering this information after having some correspondence with the client that is requesting the feature

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Server Side Scripting: 3.6+
Server Framework: Flask
ORM: Sql-Alchemy
Depoly Tool: Fabric
```

`pip install requirement.txt`

### Installing

A step by step series of examples that tell you how to get a development env running


```
Set Up a Virtual Environment
```

```
install requirements
```

```
migrate and update the changes to your database with commands below
```

`flask db migrate`
`flask db upgrade`

```
create sample clients from python shell
```

```
then create request for clients from the main interface
```


`main interface` <http://localhost:5000>

```
That is all.
```

```
#wink ;)
```

## Approach to Problem
if a user input a request with a priority aleady on an existing request, i increment every request from that priority number and above so my new request can use the priority of choice. that way we can never have two request with same priority number.

since feature priority is directly proportional to number of requests then if a user types in a priority above the current number of request in the system, the request priority will be the `number of total request + 1`. 

## Running the tests

run tests by using the command at the application root directory

`pytest`



## Deployment

include all neccessary credentials like (database, hosting of static files *optional, etc)

`pip install Fabric3`

`fab update_app`

`fab docker_up`

## Demo
<http://sandbox.quizboot.com:5000/>

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [AWS (Rds, Ec2)](https://s3.console.aws.amazon.com/) - Hosting Platform
* [Gunicorn](https://gunicorn.org/) -  Python WSGI HTTP Server for UNIX
* [Fabric](http://www.fabfile.org/) - Auto Deploy tool
* [Vue.js](https://vuejs.org/) - Javascript framework
* [Jquery](https://jquery.com/) - Javascript framework

