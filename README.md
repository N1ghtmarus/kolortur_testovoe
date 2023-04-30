# Описание проекта

Этот проект представляет собой API для управления книгами и их авторами.

## Установка и запуск
1. Клонируйте репозиторий:
```bash
git@github.com:N1ghtmarus/kolortur_testovoe.git
```

2. Перейдите в каталог проекта и установите все необходимые зависимости:
```bash
cd backend
pip install -r requirements.txt
```
3. Создайте файл .env в корне проекта со следующим содержимым (замените значения на свои):
```makefile
DJANGO_SECRET_KEY=<>
```
4.  Выполните миграции:

```bash
python manage.py makemigrations
python manage.py migrate
```
5. Запустите сервер разработки Django:

```bash
python manage.py runserver
```
Сервер будет доступен по адресу http://127.0.0.1:8000/api/

# Модели
## Book

У модели `Book` есть следующие поля:

- `title` (CharField) - название книги.
- `author` (ForeignKey, Author) - автор книги.
- `description` (Textfield) - описание книги.
- `pub_date` (DateField) - дата публикации книги.

## Author

Модель `Author` представляет собой автора книги. У автора есть следующие поля:

- `first_name` (CharField) - имя автора.
- `last_name` (CharField) - фамилия автора.
- `email` (EmailField) - email автора.
- `birh_date` (DateField) - дата рождения.

# Views
## BooksViewSet

ViewSet для управления книгами.

Действия, которые поддерживает этот ViewSet:

- `GET` /api/books/ - список всех книг в базе данных
- `GET` /api/books/<int:pk>/ - детальная информация об одной книге
- `POST` /api/books/ - создание новой книги
- `PUT` /api/books/<int:pk>/ - обновление информации о книге
- `DELETE` /api/books/<int:pk>/ - удаление книги из базы данных