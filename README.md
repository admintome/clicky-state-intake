# Clicky Stats Intake

This is a python application that polls [Clicky.com](http://clicky.com) site [statistics API](https://clicky.com/help/api) and pushes those stats in JSON form to a Kafka topic.

It is only meant to be sample code at the moment.  

It is also meant to run in Marathon as a Docker container.

## Building the Dockerfile

In order to build the docker container run these commands:

```
$ git clone git@github.com:admintome/clicky-state-intake.git
$ cd clicky-state-intake/
$ docker build -t site-stats-intake .
```

Then to run:

```
docker run -it --rm --name intake --env SITE_ID="{your clicky site_id" --env SITEKEY="{your clicky sitekey}" --env KAFKA_BROKERS="192.168.1.x:port" site-stats-intake
```

For more infomation checkout my article: 

[Kafka Tutorial for Fast Data Architecture](http://www.admintome.com/blog/kafka-tutorial-for-fast-data-architecture/)
