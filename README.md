## Описание
Тестовое задание skillbox

## Стек технологий
1. Python (Django)
2. Postgresql - БД

## Запуск 
Для запуска web приложения необходимо запустить Docker контейнер
```
docker-compose up или docker-compose up --build
```
При этом будет автоматически создан новый пользователь.

*admin* - логин,
*admin* - пароль

## Использование
Запуск автотестов:
> python manage.py test

Импорт данных:
> http://localhost:8080/admin/product/goods/

Экспорт данных:
> http://localhost:8080/admin/product/shop/

Список всех товаров:
> GET
>
> http://localhost:8000/api/v1/instance/

Выполнить покупку:
> POST
> 
> http://localhost:8000/api/v1/buy/
> 
> BODY
> 
> {
	"basket_id": <USERBASKET id>
}


## Authors and acknowledgment
*Alexander Sokolov*

## License
For open source projects, say how it is licensed.
