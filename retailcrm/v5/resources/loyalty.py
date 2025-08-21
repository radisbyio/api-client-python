import decimal
from datetime import datetime

from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.entities.loyalty import SerializedCreateLoyaltyAccount, SerializedEditLoyaltyAccount
from retailcrm.v5.schemas.entities.orders import SerializedOrder
from retailcrm.v5.schemas.filters.loyalty import LoyaltyAccountFilterData, LoyaltyAccountBonusOperationsApiFilterType, \
    LoyaltyAccountBonusApiFilterType, LoyaltyBonusOperationsApiFilterType, LoyaltyApiFilterData
from retailcrm.v5.schemas.requests.loyalty import LoyaltyAccountsFilterRequest, LoyaltyAccountCreateRequest, \
    LoyaltyAccountBonusChargeRequest, LoyaltyAccountEditRequest, LoyaltyAccountBonusCreditRequest, \
    LoyaltyAccountBonusOperationsRequest, LoyaltyBonusDetailsRequest, LoyaltyBonusOperationsAllRequest, \
    LoyaltyCalculateRequest, LoyaltiesFilterRequest
from retailcrm.v5.schemas.responses.loyalty import LoyaltyAccountsResponse, LoyaltyAccountCreateResponse, \
    LoyaltyAccountBonusChargeResponse, LoyaltyAccountActivateResponse, LoyaltyAccountEditResponse, \
    LoyaltyAccountGetResponse, LoyaltyAccountBonusCreditResponse, LoyaltyAccountBonusOperationsResponse, \
    LoyaltyBonusDetailsResponse, LoyaltyBonusOperationsResponse, LoyaltyCalculateResponse, LoyaltiesFilterResponse, \
    LoyaltyRetrieveResponse


class LoyaltyApiResource(ApiResource):
    async def accounts_filter(
        self, filter_obj: LoyaltyAccountFilterData | None = None, limit: int = 20, page: int = 1
    ) -> LoyaltyAccountsResponse:
        """Список участий в программе лояльности

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-loyalty-accounts
        :param filter_obj: Фильтр
        :param limit: Количество элементов на странице
        :param page: Номер страницы
        :return: LoyaltyAccountsResponse
        """
        request = LoyaltyAccountsFilterRequest(filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            "/loyalty/accounts",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, LoyaltyAccountsResponse)

    async def account_create(
        self, loyalty_account: SerializedCreateLoyaltyAccount, site: str | None = None
    ) -> LoyaltyAccountCreateResponse:
        """
        **Добавление клиента в программу лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-loyalty-account-create
        :param loyalty_account: Данные для добавления клиента в программу лояльности
        :param site: Символьный код магазина
        :return: LoyaltyAccountCreateResponse
        """
        request = LoyaltyAccountCreateRequest(loyaltyAccount=loyalty_account, site=site)
        response = await self._client.post(
            "/loyalty/account/create",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, LoyaltyAccountCreateResponse)

    async def account_get(self, account_id: int) -> LoyaltyAccountGetResponse:
        """
        **Получение информации об участии в программе лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-loyalty-account-id
        :param account_id: ID участия в программе лояльности
        :return: LoyaltyAccountGetResponse
        """
        response = await self._client.get(f"/loyalty/account/{account_id}")
        return self._process_response(response, LoyaltyAccountGetResponse)

    async def account_edit(
        self, account_id: int, loyalty_account: SerializedEditLoyaltyAccount
    ) -> LoyaltyAccountEditResponse:
        """
        **Редактирование участия в программе лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-loyalty-account-id-edit
        :param account_id: ID участия в программе лояльности
        :param loyalty_account: Данные для редактирования участия
        :return: LoyaltyAccountEditResponse
        """
        request = LoyaltyAccountEditRequest(loyaltyAccount=loyalty_account)
        response = await self._client.post(
            f"/loyalty/account/{account_id}/edit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, LoyaltyAccountEditResponse)

    async def account_activate(self, account_id: int) -> LoyaltyAccountActivateResponse:
        """
        **Активация участия в программе лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-loyalty-account-id-activate
        :param account_id: ID участия в программе лояльности
        :return: LoyaltyAccountActivateResponse
        """
        response = await self._client.post(f"/loyalty/account/{account_id}/activate")
        return self._process_response(response, LoyaltyAccountActivateResponse)

    async def account_bonus_charge(
        self, account_id: int, amount: decimal.Decimal, comment: str
    ) -> LoyaltyAccountBonusChargeResponse:
        """
        **Списание бонусов участию в программе лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-loyalty-account-id-bonus-charge
        :param account_id: ID участия в программе лояльности
        :param amount: Количество бонусов к списанию
        :param comment: Комментарий
        :return: LoyaltyAccountBonusChargeResponse
        """
        request = LoyaltyAccountBonusChargeRequest(amount=amount, comment=comment)
        response = await self._client.post(
            f"/loyalty/account/{account_id}/bonus/charge",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, LoyaltyAccountBonusChargeResponse)

    async def account_bonus_credit(
        self,
        account_id: int,
        amount: decimal.Decimal,
        activation_date: datetime | None = None,
        expire_date: datetime | None = None,
        comment: str | None = None,
    ) -> LoyaltyAccountBonusCreditResponse:
        """
        **Начисление бонусов участию в программе лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-loyalty-account-id-bonus-credit
        :param account_id: ID участия в программе лояльности
        :param amount: Количество бонусов к начислению
        :param activation_date: Дата активации бонусов
        :param expire_date: Дата сгорания бонусов
        :param comment: Комментарий
        :return: LoyaltyAccountBonusCreditResponse
        """
        request = LoyaltyAccountBonusCreditRequest(
            amount=amount,
            activationDate=activation_date,
            expireDate=expire_date,
            comment=comment,
        )
        response = await self._client.post(
            f"/loyalty/account/{account_id}/bonus/credit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, LoyaltyAccountBonusCreditResponse)

    async def account_bonus_operations(
        self,
        account_id: int,
        filter_data: LoyaltyAccountBonusOperationsApiFilterType | None = None,
        limit: int = 20,
        page: int = 1,
    ) -> LoyaltyAccountBonusOperationsResponse:
        """
        **История бонусного счета для конкретного участия**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-loyalty-account-id-bonus-operations
        :param account_id: ID участия в программе лояльности
        :param filter_data: Фильтр
        :param limit: Количество элементов на странице
        :param page: Номер страницы
        :return: LoyaltyAccountBonusOperationsResponse
        """
        request = LoyaltyAccountBonusOperationsRequest(
            filter_obj=filter_data, limit=limit, page=page
        )
        response = await self._client.get(
            f"/loyalty/account/{account_id}/bonus/operations",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, LoyaltyAccountBonusOperationsResponse)

    async def account_bonus_details(
        self,
        account_id: int,
        status: str,
        filter_data: LoyaltyAccountBonusApiFilterType | None = None,
        limit: int = 20,
        page: int = 1,
    ) -> LoyaltyBonusDetailsResponse:
        """
        **Получение детализации по бонусному счету**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-loyalty-account-id-bonus-status-details
        :param account_id: ID участия в программе лояльности
        :param status: Статус бонусов
        :param filter_data: Фильтр
        :param limit: Количество элементов на странице
        :param page: Номер страницы
        :return: LoyaltyBonusDetailsResponse
        """
        request = LoyaltyBonusDetailsRequest(
            filter_obj=filter_data, limit=limit, page=page
        )
        response = await self._client.get(
            f"/loyalty/account/{account_id}/bonus/{status}/details",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, LoyaltyBonusDetailsResponse)

    async def bonus_operations(
        self,
        filter_data: LoyaltyBonusOperationsApiFilterType | None = None,
        limit: int = 20,
        cursor: str | None = None,
    ) -> LoyaltyBonusOperationsResponse:
        """
        **История бонусного счета для всех участий**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-loyalty-bonus-operations
        :param filter_data: Фильтр
        :param limit: Количество элементов на странице
        :param cursor: Курсор
        :return: LoyaltyBonusOperationsResponse
        """
        request = LoyaltyBonusOperationsAllRequest(
            filter_obj=filter_data, limit=limit, cursor=cursor
        )
        response = await self._client.get(
            "/loyalty/bonus/operations",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, LoyaltyBonusOperationsResponse)

    async def calculate(
        self, site: str, order: SerializedOrder, bonuses: decimal.Decimal = decimal.Decimal(0)
    ) -> LoyaltyCalculateResponse:
        """
        **Расчёт максимальной скидки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-loyalty-calculate
        :param site: Символьный код магазина
        :param order: Заказ
        :param bonuses: Количество бонусов
        :return: LoyaltyCalculateResponse
        """
        request = LoyaltyCalculateRequest(site=site, order=order, bonuses=bonuses)
        response = await self._client.post(
            "/loyalty/calculate",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, LoyaltyCalculateResponse)

    async def loyalties_filter(
        self, filter_data: LoyaltyApiFilterData | None = None, limit: int = 20, page: int = 1
    ) -> LoyaltiesFilterResponse:
        """
        **Список программ лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-loyalty-loyalties
        :param filter_data: Фильтр
        :param limit: Количество элементов на странице
        :param page: Номер страницы
        :return: LoyaltiesFilterResponse
        """
        request = LoyaltiesFilterRequest(filter_obj=filter_data, limit=limit, page=page)
        response = await self._client.get(
            "/loyalty/loyalties",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, LoyaltiesFilterResponse)

    async def loyalty_get(self, loyalty_id: int) -> LoyaltyRetrieveResponse:
        """
        **Получение информации о программе лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-loyalty-loyalties-id
        :param loyalty_id: ID программы лояльности
        :return: LoyaltyRetrieveResponse
        """
        response = await self._client.get(f"/loyalty/loyalties/{loyalty_id}")
        return self._process_response(response, LoyaltyRetrieveResponse)