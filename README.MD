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
- [x] Название каждой страны гиперссылка, которая ведет на персональную страницу данной страны.
- [x] Реализована персональная страница для каждой страны
- [x] На главной странице добавлена ссылка “Языки”(url: `/languages/`), на которой отображается список всех языков

- [x] Отправьте ссылку на ваш репозиторий преподавателю на почту: _________@gmail.com :-)

### Часть-3
- [x] Создайте модель-класс Country.
- [x] Перенесите все страны из исходного json файла в базу данных(БД).
- [X] Измените работу вашего приложения на работу с БД
- [X] Выгрузите данные из БД в фикстуру(fixture) countries.json

### Часть-4
- [x] Используя информацию с занятия, измените структуру БД, реализовав связь “многие-ко-многом” для стран и языков.
        Не забудьте: выгрузить обновленные данные из БД fixture: countries.json
- [x] Добавьте в проект файл README.md, добавив в него:
          Информацию о запуске проекта после клонирования
          Список всех заданий, пометив выполненные

### Часть-5
- [x] Добавьте в проект файл requirements.txt
- [ ] На странице “Языки”, все языки в списке сделайте гиперссылками, каждая ведет на отдельную страницу, 
      на которой отображаются страны, которые говорят на выбранном языке.
- [x] Все ваши шаблоны(templates) используют наследование от базового шаблона.
- [x] Все используемые url’ы являются именованными.

### Часть-7 (финальные задания)
- [x] Наверху страницы со списком стран добавьте алфавит, каждая буква которого является гиперссылкой. 
      Каждая гиперссылка(на букве) ведет на страницу на которой отображаются только страны на выбранную букву. См. аналогию тут.
- [x] Внизу страницы со списком стран реализуйте пагинацию. На каждой странице отобразите 10 стран.




### новое окружение:
python3 -m venv countries_venv
source countries_venv/Scripts/activate

pip install django

pip freeze > requirements.txt

git init

django-admin startproject countries_project .

python manage.py startapp countries



### install requirements: 
pip install -r requirements.txt

### run project:
source countries_venv/Scripts/activate
python manage.py runserver

### models
python manage.py makemigrations countries
python manage.py migrate


pip install django-extensions
pip install ipython

### run django-extensions console:
python manage.py shell_plus --ipython
    
### fixtures создания 
python manage.py dumpdata countries.Country --indent 2 > countries/fixtures/countries.json
### fixtures Загрузка
python manage.py loaddata countries/fixtures/countries.json
### Удаление данных из всех таблиц приложения:
python manage.py flush


