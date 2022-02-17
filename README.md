# Тестовое задание genzis

Разработать одностраничник на Flask. На странице будут две формы и список. Первая, форма добавление записи в список, вторая, форма поиска\фильтрации списка, по названию, атрибуту и т.д.

Сервис доступен по ссылке: https://genzis-test-task.herokuapp.com/

### Стек

* Python 3.8
* Flask
* Flask-RESTful для REST
* Postgres

### Запуск приложения локально

- скачать репозиторий: `git clone https://github.com/Spartan327/genzis-test-task`  
- установить Poetry https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions  
- запуск проекта: `poetry install, poetry shell, ./run.sh`  
- переменные окружения экспортируются в файле: `run.sh`  

### Технические требования к заданию

* :heavy_check_mark: **Использовать REST**  
* :heavy_check_mark: **Использовать Postgresql или MySql**  
* :question: **Сделать валидацию по типу данных.** поскольку использовал одну модель, проверяется валидация ввода 
* :heavy_check_mark: **CI/CD** автоматический деплой на сервер при каждом коммите в master  
* :heavy_check_mark: **Использовать GitHub**  

### Структура и функционал приложения

API сервиса доступно по url: https://genzis-test-task.herokuapp.com/api/v1/items  

Реализован CRUD функцилнал.  

`/api/v1/items`  
GET выводит список элементов  
POST ожидает на вход  
```
{
    "count": int, 0-1
    "name": str,  1
    "type": str   0-1
}
```  
`/api/v1/items/<int:id>`  
GET выводит элемент  
PUT ожидает на вход  
```
{
    "count": int, 0-1
    "name": str,  1
    "type": str   0-1
}
```
DELETE удаляет элемент