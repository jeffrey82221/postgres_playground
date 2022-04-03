# postgres_playground
Try to connect to my mac mini DB and play around with it

# Install 

## Install Postgresql: 

brew install postgres

## Starting (or Stop) Postgres Service: 

brew services start postgresql
(brew services stop postgresql)

## Configure Postgres DB

psql postgres

CREATE ROLE admin WITH LOGIN PASSWORD 'password';
ALTER ROLE admin CREATEDB;

\q
psql postgres -U admin


## Install DB Browser and check the content: 

https://www.pgadmin.org/ 

Enter: 

host – “localhost”
user – “newuser”
password – “password”
maintenance database – “postgres”

## install psycopg2 

$ brew install libpq --build-from-source

$ export LDFLAGS="-L/opt/homebrew/opt/libpq/lib"

$ pip install psycopg2-binary

## Create database.ini: 

```ini
[postgresql]
host=localhost
database=suppliers
user=postgres
password=SecurePas$1
```