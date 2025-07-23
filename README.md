# RetailCRM API Client

Python >3.11

## Состояние разработки API:
- [x] Верификация
- [x] Веб-аналитика
- [x] Статистика
- [ ] Пользовательские поля
- [ ] Клиенты
- [ ] Лояльность
- [ ] Платежи
- [ ] Оповещения
- [ ] Задачи
- [ ] Склад
- [ ] Корпоративные клиенты
- [ ] Действия клиента на сайте магазина
- [ ] Доставки
- [ ] Файлы
- [ ] Интеграция
- [ ] Заказы
- [ ] Комплектация заказов
- [ ] Рекомендации
- [ ] Справочники
- [ ] Сегменты
- [ ] Настройки
- [ ] Телефония
- [ ] Транспорты
- [ ] Пользователи

## Как использовать

```python
from retailcrm import RetailCrmApiClientV5, RetailCrmApiError
from retailcrm.v5.schemas import OrderFilterData

crm_url = "https://example.retailcrm.ru"
api_key = "example_api_key"

api_cient = RetailCrmApiClientV5(crm_url, api_key)

order_to_get = "12345"

order_filter = OrderFilterData(email="email@example.com")
try:
    response = await api_cient.orders.get(order_filter)
except RetailCrmApiError as exc:
    print({exc.error_msg})
```


## Правила 

- Именование схем данных ответа должны иметь следующий формат: `<Entity><Action>Response`, например OrderRetrieveResponse.
- 
