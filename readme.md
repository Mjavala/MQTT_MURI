## Backend

### - DO droplet debian (v10.4)
### - Docker (v19)
    - Hasura -  docker image: hasura/graphql-engine:v1.0.0-alpha20
    - timescaledb - docker image: timescale/timescaledb:latest-pg12
        - postgres (v12.2)
- docker compose file. **TODO: Security config**


### Database architecture

-   timescaledb hypertable
-   schema

| time | id | altitude | rssi | temperature | Humidity |
|------|----|----------|------|-------------|----------|

-   resources: [timescale docs](http://64.227.104.52:8080/console)


## Hasura API UI
The current set up is for communication with the frontend via the **Hasura GraphQL** interface
located here - [API user interface](http://64.227.104.52:8080/console).

It is password protected. For now, ask for the password through ryver. **TODO: Security config**