# Backend services

## Logging 

-   logs are stored here -  [logging server](http://159.89.152.16/logs/)

## Data ingestion

### Resource
[Asyncpg](https://github.com/MagicStack/asyncpg)


# Database - DO droplet debian (v10.4)

## Backend UI 
The current set up is for communication with the frontend via the **Hasura GraphQL** interface.
located here - [API user interface](http://64.227.104.52:8080/console).

It is password protected. For now, ask for the password through ryver.

### TODO 
-   security config
-   replication
-   global log files
-   raw database instance

### Docker (v19)
-   Hasura -  docker image: hasura/graphql-engine:v1.0.0-alpha20
-   timescaledb - docker image: timescale/timescaledb:latest-pg12 | postgres (v12.2)

### Database architecture

-   timescaledb hypertable
-   schema

| time | id | altitude | rssi | temperature | Humidity |
|------|----|----------|------|-------------|----------|

-   indexed on ``(time DESC, id)``


### Resources 
-   [timescale docs](http://64.227.104.52:8080/console)
-   [hasura docs](https://hasura.io/docs/1.0/graphql/manual/index.html)
