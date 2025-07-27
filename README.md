# RetailCRM API Client

Python >=3.11

## Состояние разработки API:
- [x] Задачи
- [x] Телефония
- [x] Транспорты
- [x] Пользователи
- [x] Верификация
- [x] Веб-аналитика
- [x] Статистика
- [ ] Пользовательские поля
- [ ] Клиенты
- [ ] Лояльность
- [ ] Платежи
- [ ] Оповещения
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

## Интерфейсы для интеграций

```python
from retailcrm.v5.actions.transports import MGTransportActions
from retailcrm.v5.schemas.requests.transports import MGTransportOnlineRequest, MGTransportVisitsRequest
from retailcrm.v5.schemas.responses.transports import MGTransportOnlineResponse, MGTransportVisitsResponse
from retailcrm.v5.schemas.entities.transports import ChatLastVisit
from datetime import datetime
from dataclasses import dataclass


@dataclass(slots=True)
class TransportConfig:
    client_id: str

class MockTransportActionsService(MGTransportActions):
    def __init__(self, transport_config: TransportConfig):
        self._transport_config = transport_config
    
    async def online(self, request: MGTransportOnlineRequest) -> MGTransportOnlineResponse:
        print(f"MockTransportIntegration: Simulating online status for {self._transport_config.client_id}")
        return MGTransportOnlineResponse(lastOnline=datetime.now())

    async def visits(self, request: MGTransportVisitsRequest) -> MGTransportVisitsResponse:
        print(f"MockTransportIntegration: Simulating visits for {self._transport_config.client_id}")
        return MGTransportVisitsResponse(
            lastVisit=ChatLastVisit(
                source="test_source",
                createdAt=datetime.now(),
                duration=100,
            ),
            countVisits=44,
        )
```


## Правила 

- Именование схем данных ответа должны иметь следующий формат: `<Entity><Action>Response`, например OrderRetrieveResponse.
- 
