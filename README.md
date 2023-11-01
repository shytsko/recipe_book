# Запуск локально с базой SQLite

1. В файле `src/src/settings.py` изменить настройки СУБД. Закомментировать параметры для postgresql и раскомметировать
   настройки для SQLite

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT')
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}
```

База уже содержит некоторые данные. Есть пользователи admin:zaqwsx123 и user:1

2. Запустить сервер

```commandline
cd src
python manage.py runserver
```

3. Проверяем работу [http://127.0.0.1:8000](http://127.0.0.1:8000)

# Запуск локально в docker c nginx и базой postgresql

1. Создаем и запускаем стек контейнеров

```commandline
cd src
docker compose -f docker-compose.dev.yml build
docker compose -f docker-compose.dev.yml up
```

Иногда при первом запуске после создания контейнеров, django падает из-за ошибки подключения к базу. Не понятно, с чем
это связано, со второй попытки запускается нормально

2. Заходим в контейнер django и загружаем дамп базы

```commandline
docker exec -it django sh
/app # python -Xutf8 manage.py loaddata db.json
/app # exit
```

База заполниться данными, будут созданы пользователи admin:zaqwsx123 и user:1

Если дамп базы не нужен, то только создаем суперадмина

```commandline
docker exec -it django sh
/app # python manage.py createsuperuser
/app # exit
```

3. Проверяем работу [http://127.0.0.1](http://127.0.0.1)


