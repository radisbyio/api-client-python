from typing import Literal

from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.base import IdTypesLiteral
from retailcrm.v5.schemas.entities.customer_interaction import SerializedCart, SerializedFavorite
from retailcrm.v5.schemas.requests.customer_interaction import CartClearRequest, CartSetRequest, FavoritesRemoveRequest, \
    FavoritesAddRequest, FavoritesGetRequest
from retailcrm.v5.schemas.responses.customer_interaction import CartClearResponse, CartSetResponse, CartGetResponse, \
    FavoritesRemoveResponse, FavoritesAddResponse, FavoritesGetResponse


class CustomerInteractionApiResource(ApiResource):
    async def cart_clear(
        self, site: str, cart: SerializedCart, site_by: Literal["id", "code"] = "code"
    ) -> CartClearResponse:
        """
        **Очистка текущей корзины клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customer-interaction-site-cart-clear
        :param site: Символьный код или ID магазина.
        :param cart: Объект корзины.
        :param site_by: Указывается, что передается в параметре site: внутренний ID (siteBy=id) или код (siteBy=code) магазина. По умолчанию code.
        :return: CartClearResponse
        """
        request = CartClearRequest(cart=cart)
        params = {"siteBy": site_by}
        response = await self._client.post(
            endpoint=f"/customer-interaction/{site}/cart/clear",
            params=params,
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CartClearResponse)

    async def cart_set(
        self, site: str, cart: SerializedCart, site_by: Literal["id", "code"] = "code"
    ) -> CartSetResponse:
        """
        **Создание или перезапись данных корзины**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customer-interaction-site-cart-set
        :param site: Символьный код или ID магазина.
        :param cart: Объект корзины.
        :param site_by: Указывается, что передается в параметре site: внутренний ID (siteBy=id) или код (siteBy=code) магазина. По умолчанию code.
        :return: CartSetResponse
        """
        request = CartSetRequest(cart=cart)
        params = {"siteBy": site_by}
        response = await self._client.post(
            endpoint=f"/customer-interaction/{site}/cart/set",
            params=params,
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CartSetResponse)

    async def cart_get(
        self, site: str, customer_id: str, by: IdTypesLiteral = "externalId", site_by: Literal["id", "code"] = "code"
    ) -> CartGetResponse:
        """
        **Получение текущей корзины клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customer-interaction-site-cart-customerId
        :param site: Символьный код или ID магазина.
        :param customer_id: ID клиента.
        :param by: Указывается, что передается в параметре customerId: внутренний (by=id) или внешний (by=externalId) ID клиента. По умолчанию externalId.
        :param site_by: Указывается, что передается в параметре site: внутренний ID (siteBy=id) или код (siteBy=code) магазина. По умолчанию code.
        :return: CartGetResponse
        """
        request = CartGetRequest(by=by, siteBy=site_by)
        response = await self._client.get(
            endpoint=f"/customer-interaction/{site}/cart/{customer_id}",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CartGetResponse)

    async def favorites_get(
        self, site: str, customer_id: str, by: IdTypesLiteral = "externalId", site_by: Literal["id", "code"] = "code"
    ) -> FavoritesGetResponse:
        """
        **Получение списка избранного для клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customer-interaction-site-favorites-customerId
        :param site: Символьный код или ID магазина.
        :param customer_id: ID клиента.
        :param by: Указывается, что передается в параметре customerId: внутренний (by=id) или внешний (by=externalId) ID клиента. По умолчанию externalId.
        :param site_by: Указывается, что передается в параметре site: внутренний ID (siteBy=id) или код (siteBy=code) магазина. По умолчанию code.
        :return: FavoritesGetResponse
        """
        request = FavoritesGetRequest(by=by, siteBy=site_by)
        response = await self._client.get(
            endpoint=f"/customer-interaction/{site}/favorites/{customer_id}",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, FavoritesGetResponse)

    async def favorites_add(
        self, site: str, customer_id: str, favorite: SerializedFavorite, by: IdTypesLiteral = "externalId", site_by: Literal["id", "code"] = "code"
    ) -> FavoritesAddResponse:
        """
        **Добавление товарного предложения в список избранного клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customer-interaction-site-favorites-customerId-add
        :param site: Символьный код или ID магазина.
        :param customer_id: ID клиента.
        :param favorite: Объект избранного товара.
        :param by: Указывается, что передается в параметре customerId: внутренний (by=id) или внешний (by=externalId) ID клиента. По умолчанию externalId.
        :param site_by: Указывается, что передается в параметре site: внутренний ID (siteBy=id) или код (siteBy=code) магазина. По умолчанию code.
        :return: FavoritesAddResponse
        """
        request = FavoritesAddRequest(favorite=favorite)
        params = {"by": by, "siteBy": site_by.value}
        response = await self._client.post(
            endpoint=f"/customer-interaction/{site}/favorites/{customer_id}/add",
            params=params,
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, FavoritesAddResponse)

    async def favorites_remove(
        self, site: str, customer_id: str, favorite: SerializedFavorite, by: IdTypesLiteral = "externalId", site_by: Literal["id", "code"] = "code"
    ) -> FavoritesRemoveResponse:
        """
        **Удаление товарного предложения из списка избранного клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customer-interaction-site-favorites-customerId-remove
        :param site: Символьный код или ID магазина.
        :param customer_id: ID клиента.
        :param favorite: Объект избранного товара.
        :param by: Указывается, что передается в параметре customerId: внутренний (by=id) или внешний (by=externalId) ID клиента. По умолчанию externalId.
        :param site_by: Указывается, что передается в параметре site: внутренний ID (siteBy=id) или код (siteBy=code) магазина. По умолчанию code.
        :return: FavoritesRemoveResponse
        """
        request = FavoritesRemoveRequest(favorite=favorite)
        params = {"by": by, "siteBy": site_by}
        response = await self._client.post(
            endpoint=f"/customer-interaction/{site}/favorites/{customer_id}/remove",
            params=params,
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, FavoritesRemoveResponse)