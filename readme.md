# System Overview
![alt text](https://raw.githubusercontent.com/Mjavala/muri/master/system.png)

# Todo:
-   Doc - https://docs.google.com/document/d/1CSF3hZtkelVOZ4mjL_WDlLTLz2xcdvG2n6zTeEbTXk4/edit?usp=sharing
-   Historical data ui
-   Security config
-   Replication
-   System log files
-   Raw database instance
-   Data ingestion as a service
-   Testing

# Proposed DB schema

###   2 relational tables - devices, stations - ||  One time-series hypertable -  device_data
```SQL
CREATE TABLE "devices"(
   device_id   VARCHAR (30),
);

CREATE TABLE "stations"(
   station_id   VARCHAR (30),
);

CREATE TABLE "device_data"(
   time            TIMESTAMP WITH TIME ZONE,
   altitude        REAL,
   rssi            SMALLINT,
   temperature     REAL,
   humidity        REAL,
   device_id       VARCHAR (30),
   station_id      VARCHAR (30)
);

```

### Raw DB schemas

```SQL
CREATE TABLE "0xd2a8_raw"(
   station        VARCHAR (20),
   receiver       VARCHAR (10),
   msg_time       DOUBLE PRECISION,
   addr_from      VARCHAR (30),
   altitude       REAL,
   rssi_rx        SMALLINT,
   frame_type     VARCHAR (10),
   frame_cnt      SMALLINT,
   frame          TEXT,
   packet_id      INTEGER,
   packet_num     INTEGER,
   epoch_index    INTEGER,
   gps_lat        REAL,
   gps_lon        REAL,
   gps_alt        REAL,
   gps_tow        INTEGER,
   gps_fix        SMALLINT,
   gps_numsats    SMALLINT,
   batt_mon       SMALLINT,
   gondola_statu  SMALLINT,
   RS41_temp      REAL,
   RS41_hum       REAL,
   RS41_pres      REAL,
   temp_ta1       INTEGER,
   temp_ti1       INTEGER,
   temp_ta2       INTEGER,
   temp_ti2       INTEGER,
   cw_chop_vr1    INTEGER,
   cw_chop_vr2    INTEGER,
   cw_chop_vo1    INTEGER,
   cw_chop_vo2    INTEGER,
   cw_chop_cpot   INTEGER,
   cw_chop_gpot   SMALLINT,
   gps_veln       SMALLINT,
   gps_vele       SMALLINT,
   gps_vel_d      SMALLINT,
   hw_chop_vr1    SMALLINT,
   hw_chop_vr2    SMALLINT,
   hw_chop_vo1    SMALLINT,
   hw_chop_vo2    SMALLINT,
   hw_chop_cpot   SMALLINT,
   hw_chop_gpot   SMALLINT,
   rms_hor_vel    SMALLINT,
   rms_ver_vel    SMALLINT,
   var_35         SMALLINT
);
```

```SQL
CREATE TABLE "0xC109_raw"(
   station        VARCHAR (20),
   receiver       VARCHAR (10),
   msg_time       DOUBLE PRECISION,
   addr_from      VARCHAR (30),
   altitude       REAL,
   rssi_rx        SMALLINT,
   frame_type     VARCHAR (10),
   frame_cnt      SMALLINT,
   frame          TEXT,
   packet_id      INTEGER,
   packet_num     INTEGER,
   epoch_index    INTEGER,
   interval_index SMALLINT,
   gps_lat        REAL,
   gps_lon        REAL,
   gps_alt        REAL,
   gps_tow        INTEGER,
   gps_fix        SMALLINT,
   gps_numsats    SMALLINT,
   cw_sa_0        INTEGER,
   cw_sa_1        INTEGER,
   cw_sa_2        INTEGER,
   cw_sa_3        INTEGER,
   cw_sa_4        INTEGER,
   cw_sa_5        INTEGER,
   cw_sa_6        INTEGER,
   cw_sa_7        INTEGER,
   cw_sa_8        INTEGER,
   hw_sa_0        INTEGER,
   hw_sa_1        INTEGER,
   hw_sa_2        INTEGER,
   hw_sa_3        INTEGER,
   hw_sa_4        INTEGER,
   hw_sa_5        INTEGER,
   hw_sa_6        INTEGER,
   hw_sa_7        INTEGER,
   hw_sa_8        INTEGER,
   cw_meas_vr1    SMALLINT,
   cw_meas_vr2    SMALLINT,
   cw_meas_vo1    SMALLINT,
   cw_meas_vo2    SMALLINT,
   cw_meas_cpot   INTEGER,
   cw_meas_gpot   INTEGER,
   hw_meas_vr1    SMALLINT,
   hw_meas_vr2    SMALLINT,
   hw_meas_vo1    SMALLINT,
   hw_meas_vo2    SMALLINT
);
```

# Frontend
-   Live data feed and visualization: [Streaming UI](https://iriss-2j50vp3tc.now.sh/#/)

## Stack
-   Vue, Vuetify, Plotly, Vue-Leaflet, Vue-Apollo, GraphQL

### Resources

-   [Vue](https://vuejs.org/v2/guide/)
-   [Vuetify](https://vuetifyjs.com/en/getting-started/quick-start/)
-   [Plotly.js](https://plotly.com/javascript/)
-   [Vue-Leaflet](https://vue2-leaflet.netlify.app/)
-   [Vue-Apollo](https://apollo.vuejs.org/)
-   [GraphQL](https://graphql.org/)

Note: If you want to understand graphQL queries the hasura ui (linked below) has a visual playground 
linked to our timescaledb.

# Backend services

## Logging 

-   Logs are stored here -  [logging server](http://159.89.152.16/logs/)
-   Logs are stored on an hourly and daily basis per device.
-   Daily logs rotate every 7 days
-   Hourly logs rotate once a day

## Data ingestion
-   Currently a 1-1 connection between an instance of this service and a single database.

### Resources
-   [Asyncpg](https://github.com/MagicStack/asyncpg)

# Database - DO droplet debian (v10.4)

## Backend UI 
The current set up is for communication with the frontend via the [Hasura GraphQL API](http://64.227.104.52:8080/console).

It is password protected. For now, ask for the password through ryver.

### Docker (v19)
-   Hasura -  docker image: hasura/graphql-engine:v1.0.0-alpha20
-   timescaledb - docker image: timescale/timescaledb:latest-pg12 | postgres (v12.2)
-   Docker compose file example:
```yaml
version: '2'
services:
  timescale:
    image: timescale/timescaledb:latest-pg12
    restart: always
    environment:
      # POSTGRES_PASSWORD: '!--- config ---!'
    ports:
    - "5432:5432"
    volumes:
    - db_data:/var/lib/postgresql/data
  graphql-engine:
    image: hasura/graphql-engine:v1.0.0-alpha20
    ports:
    - "8080:8080"
    depends_on:
    - "timescale"
    restart: always
    environment:
      # HASURA_GRAPHQL_DATABASE_URL: postgres://postgres:!--config--!@timescale:5432/postgres
      # HASURA_GRAPHQL_ACCESS_KEY: '!--- set your access key ---!'
    command:
      - graphql-engine
      - serve
      - --enable-console
volumes:
  db_data:
```

note: database muri must be created in the postgres/timescale image before hasura is able to connect.

### Useful Docker commands
-  docker exec -it [img-id] psql -U postgres (connect to postgres)
-  docker-compose start/stop
-  docker inspect [obj]


### Resources 
-   [timescale](http://64.227.104.52:8080/console)
-   [hasura](https://hasura.io/docs/1.0/graphql/manual/index.html)
