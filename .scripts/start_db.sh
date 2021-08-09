#!/usr/bin/env bash

docker-compose up -d database

mysql -h 127.0.0.1 -u root -p1234 -P3306 < .sql/nidus_database_core.sql
