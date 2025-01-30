commands

# build react

docker build -t automation-app .

# run react

docker run -p 3000:3000 automation-app

# build db

docker build -t automation-db .

# run db

docker run --name postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -p 5432:5432 -v postgres-data:/var/lib/postgresql/data automation-db

# pgcli to db

pgcli --host=127.0.0.1 --port=5432 --username=postgres --dbname=db
