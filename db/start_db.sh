docker run --rm --name mariadb_dev -e MARIADB_ROOT_PASSWORD=mysql -d -p 3808:3808 -v $(pwd)/db/data:/var/lib/mysql:rw --user $(id -u):$(id -g) mariadb:latest --port 3808
