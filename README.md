#### schedule backend

# ЗАПУСК ДЛЯ РАЗРАБОТКИ

1. Внутри директории `db` скопируйте файл `.env.example` и переименуйте его в `.env`
2. Запустите проект командой `docker compose up`
3. **Для первого запуска:** Находясь в корневой директории проекта выполните команду `docker compose exec web python3 manage.py migrate` для применения миграций
4. **Для первого запуска:** Находясь в корневой директории проекта выполните команду `docker compose exec web python3 manage.py createsuperuser --noinput` для создания Django администратора с логином `admin`, почтой `admin@ad.min` и паролем `Qwerty123`

## ДОКУМЕНТАЦИЯ ПО API
localhost:8000/api/swagger
