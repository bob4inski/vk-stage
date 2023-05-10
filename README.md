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

## запускаем бд, с которой будет общаться бот 

docker run --name postgres_db2022 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 44444:5432 -d postgres

## также нужно при первом запуске postgres создать базу данных

```
create table clients
(
    telegram_id       int,
  	service text,
  	login text,
  	password text
);
```
p.s да хранить пароли в открытом виде нельзя, но это можно исправить

## последний пункт - запуск бота

```
python3 main.py
```

##  переходим в [бота](https://t.me/vk_stage_bot) и сохраняем свои пароли
