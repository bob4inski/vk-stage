# VK-internship
Скопируйте репозиторий с помощью команды
```
git clone https://github.com/bob4inski/vk-stage.git
```
В загруженной папке создайте файл `.env` со следующим содержанием 
```
BOT_NAME=vk-project # Constant to set the name of the directory in the container
BOT_CONTAINER_NAME=vk # Constant to set the name of the bot container
BOT_IMAGE_NAME=vk-image # Constant to set the name of the bot image

BOT_TOKEN=<token> # Constant to set the token of the bot from @BotFather
USE_REDIS=TRUE # Constant to set a boolean value to use Redis

DATABASE_NAME=postgres # Constant to set name of the database
DATABASE_USER=postgres # Constant to set name of the database user
DATABASE_PASSWORD=postgres # Constant to set password of the database

#Запуск вручную
# DATABASE_PORT=44444 # Constant to set port of the database (docker-compose.yml)
# DATABASE_HOST=localhost # Set database service name from docker-compose or localhost if you want to start bot locally

#через docker-compose 
DATABASE_PORT=5432 # Constant to set port of the database (docker-compose.yml)
DATABASE_HOST=vk_DB # ost if you want to start bot locally

```
# Далее 2 варианта 
1. Запуск с помощью docker-compose 
2. Запуск вручную

## Через docker-compose все просто

В загруженной папке пропишите ```docker-compose up``` 



## А руками немного сложнее

## 1. Подгрузить зависимости с помощью команды

```
pip install -r rerequirements.txt
```

## 2. Запустить БД с помощью команды  

```
docker run --name postgres_vk -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 44444:5432 -d postgres
```
такие переменные как name, postgres_user, postgres_password и порт работы бд (в примере это 44444) можно исполтзовать свои, главное не забыть поменять их d `.env`

## 3. При первом запуске postgres создать таблицу, в которой будет хранится информация пользователй 


```
create table users
(
    telegram_id       int,
  	service text,
  	login text,
  	password text
);
```
p.s да хранить пароли в открытом виде нельзя и очень плохо, но это можно исправить

## 4. Запустить бота с помощью команды

```
python3 main.py
```

##  Переходим в [бота](https://t.me/vk_stage_bot) и сохраняем свои пароли
