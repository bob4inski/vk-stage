# vk-stage
для запуска нужно скопировать этот репозиторий
```
git clone https://github.com/bob4inski/vk-stage.git
```
Далее создать в загруженной папке файл `.env`
```
BOT_NAME=vk-project # Constant to set the name of the directory in the container
BOT_CONTAINER_NAME=vk # Constant to set the name of the bot container
BOT_IMAGE_NAME=vk-image # Constant to set the name of the bot image

BOT_TOKEN=6153330849:AAFHgaZ6cQQQSuF4Io7u0_3c7HXobSQbFvI # Constant to set the token of the bot from @BotFather
USE_REDIS=TRUE # Constant to set a boolean value to use Redis

DATABASE_NAME=postgres # Constant to set name of the database
DATABASE_USER=postgres # Constant to set name of the database user
DATABASE_PASSWORD=postgres # Constant to set password of the database
DATABASE_PORT=5432 # Constant to set port of the database (docker-compose.yml)
DATABASE_HOST=vk_DB # Set database service name from docker-compose or localhost if you want to start bot locally

```
# Далее 2 варианта 
1. docker-compose 
2. руками поднять 

## Через docker-compose все просто

заходим в папку и пишем ```docker-compose up``` 



## А руками немного сложнее

подгружаем все зависимости

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

##  Переходим в [бота](https://t.me/vk_stage_bot) и сохраняем свои пароли
