# Check-list
- [ ] Так помечаем невыполненные задания
- [x] Так помечаем выполненные

### Часть-1
- [x] Сгенерирована заготовка django-проекта
- [x] Добавлено приложение(App)
- [x] По корневому url'у доступна html-страница с приветствием и минимальным оформлением
- [x] В проект добавлен `.gitignore` (venv, настройки IDE и файл БД не под репозиторием)
- [x] Проект загружен на github

### Часть-2
- [x] При отображении всех страниц используются html-шаблоны(templates)
- [x] В корень проекта добавлен файл countries.json со списком всех стран
- [x] По url: `/countries-list/` отображается нумерованный список всех стран (только названия стран)
- [ ] Название каждой страны гиперссылка, которая ведет на персональную страницу данной страны.
- [ ] Реализована персональная страница для каждой страны
- [ ] На главной странице добавлена ссылка “Языки”(url: `/languages/`), на которой отображается список всех языков

### Часть-3
- [ ] Создайте модель-класс Country.
- [ ] Перенесите все страны из исходного json файла в базу данных(БД).
- [ ] Измените работу вашего приложения на работу с БД
- [ ] Выгрузите данные из БД в фикстуру(fixture) countries.json







новое окружение:
python3 -m venv countries_venv
source countries_venv/Scripts/activate

pip install django

pip freeze > requirements.txt

git init

django-admin startproject countries_project .

python manage.py startapp countries



install requirements: 
`pip install -r requirements.txt`

run project:
python manage.py runserver

run django-extensions console: 
`python manage.py shell_plus --ipython`


