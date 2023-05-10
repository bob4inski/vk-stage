# vk-stage
для запуска нужно скопировать этот репозиторий
```
git clone https://github.com/bob4inski/vk-stage.git
```
Далее создать в загруженной папке файл `.env`
```
DATABASE_NAME=postgres # Constant to set name of the database
DATABASE_USER=postgres # Constant to set name of the database user
DATABASE_PASSWORD=postgres # Constant to set password of the database
DATABASE_PORT=44444 # Constant to set port of the database (docker-compose.yml)
DATABASE_HOST=localhost # Set databse service name from docker-compose or localhost if you want to start bot locally
```

Далее подгружаем все зависимости

```
pip install -r rerequirements.txt
```
docker run --name postgres_db2022 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 44444:5432 -d postgres