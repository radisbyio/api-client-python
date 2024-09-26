from datetime import datetime

from retailcrm.exceptions import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.schemas.loyalty import (
    LoyaltyAccountBonusApiFilterType,
    LoyaltyAccountBonusOperationsApiFilterType,
    LoyaltyAccountFilterData,
    LoyaltyApiFilterData,
    LoyaltyBonusOperationsApiFilterType,
    ResponseActivateLoyaltyAccount,
    ResponseChargeLoyaltyAccountBonus,
    ResponseCreateLoyaltyAccount,
    ResponseCreditLoyaltyAccountBonus,
    ResponseEditLoyaltyAccount,
    ResponseLoyaltiesFilter,
    ResponseLoyaltyAccountBonusOperations,
    ResponseLoyaltyAccounts,
    ResponseLoyaltyBonusDetails,
    ResponseLoyaltyBonusOperations,
    ResponseLoyaltyCalculate,
    ResponseLoyaltyRetrieve,
    SerializedCreateLoyaltyAccount,
    SerializedEditLoyaltyAccount,
)
from retailcrm.v5.schemas.orders import SerializedOrder
from retailcrm.v5.utils import pydantic_to_nested_dict


class LoyaltyController:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def accounts(
        self, filter_data: LoyaltyAccountFilterData, limit: int = 20, page: int = 1
    ) -> ResponseLoyaltyAccounts:
        """Список участий в программе лояльности

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-loyalty-accounts
        :param filter_data: Фильтр
        :param limit: Количество элементов на странице
        :param page: Номер страницы
        :return: LoyaltyAccountsResponse
        """
        response = await self._client.get(
            "/loyalty/accounts",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )

        response_obj = ResponseLoyaltyAccounts.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def account_create(
        self, loyalty_account: SerializedCreateLoyaltyAccount, site: str
    ) -> ResponseCreateLoyaltyAccount:
        """
        **Добавление клиента в программу лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-loyalty-account-create
        :param loyalty_account: Данные для добавления клиента в программу лояльности
        :param site: Символьный код магазина
        :return: ResponseCreateLoyaltyAccount
        """
        response = await self._client.post(
            "/loyalty/account/create",
            params={"site": site},
            data={
                "loyaltyAccount": loyalty_account.model_dump_json(
                    exclude_unset=True, by_alias=True
                )
            },
        )

        response_obj = ResponseCreateLoyaltyAccount.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def account_get(self, account_id: int) -> ResponseCreateLoyaltyAccount:
        """
        **Получение информации об участии в программе лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-loyalty-account-id
        :param account_id: ID участия в программе лояльности
        """
        response = await self._client.get(f"/loyalty/account/{account_id}")

        response_obj = ResponseCreateLoyaltyAccount.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def account_edit(
        self, account_id: int, loyalty_account: SerializedEditLoyaltyAccount
    ) -> ResponseEditLoyaltyAccount:
        """
        **Редактирование участия в программе лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-loyalty-account-id-edit
        :param account_id: ID участия в программе лояльности
        :param loyalty_account: Данные для редактирования участия
        :return: EditLoyaltyAccountResponse
        """
        response = await self._client.post(
            f"/loyalty/account/{account_id}/edit",
            data={
                "loyaltyAccount": loyalty_account.model_dump_json(
                    exclude_unset=True, by_alias=True
                )
            },
        )

        response_obj = ResponseEditLoyaltyAccount.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def account_activate(self, account_id: int) -> ResponseActivateLoyaltyAccount:
        """
        **Активация участия в программе лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-loyalty-account-id-activate
        :param account_id: ID участия в программе лояльности
        """
        response = await self._client.post(f"/loyalty/account/{account_id}/activate")

        response_obj = ResponseActivateLoyaltyAccount.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def account_bonus_charge(
        self, account_id: int, amount: float, comment: str
    ) -> ResponseChargeLoyaltyAccountBonus:
        """
        **Списание бонусов участию в программе лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-loyalty-account-id-bonus-charge
        :param account_id: ID участия в программе лояльности
        :param amount: Количество бонусов к списанию
        :param comment: Комментарий
        """
        response = await self._client.post(
            f"/loyalty/account/{account_id}/bonus/charge",
            data={"amount": amount, "comment": comment},
        )

        response_obj = ResponseChargeLoyaltyAccountBonus.model_validate_json(
            response.body
        )

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def account_bonus_credit(
        self,
        account_id: int,
        amount: float,
        activation_date: datetime,
        expire_date: datetime,
        comment: str,
    ) -> ResponseCreditLoyaltyAccountBonus:
        """
        **Начисление бонусов участию в программе лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-loyalty-account-id-bonus-credit
        :param account_id: ID участия в программе лояльности
        :param amount: Количество бонусов к начислению
        :param activation_date: Дата активации бонусов
        :param expire_date: Дата сгорания бонусов
        :param comment: Комментарий
        :return: CreditLoyaltyAccountBonusResponse
        """
        response = await self._client.post(
            f"/loyalty/account/{account_id}/bonus/credit",
            data={
                "amount": amount,
                "activationDate": activation_date.strftime("%Y-%m-%d"),
                "expireDate": expire_date.strftime("%Y-%m-%d"),
                "comment": comment,
            },
        )

        response_obj = ResponseCreditLoyaltyAccountBonus.model_validate_json(
            response.body
        )

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def account_bonus_operations(
        self,
        account_id: int,
        filter_data: LoyaltyAccountBonusOperationsApiFilterType,
        limit: int = 20,
        page: int = 1,
    ) -> ResponseLoyaltyAccountBonusOperations:
        """
        **История бонусного счета для конкретного участия**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-loyalty-account-id-bonus-operations
        :param account_id: ID участия в программе лояльности
        :param filter_data: Фильтр
        :param limit: Количество элементов на странице
        :param page: Номер страницы
        """
        response = await self._client.get(
            f"/loyalty/account/{account_id}/bonus/operations",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )

        response_obj = ResponseLoyaltyAccountBonusOperations.model_validate_json(
            response.body
        )

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def account_bonus_details(
        self,
        account_id: int,
        status: str,
        filter_data: LoyaltyAccountBonusApiFilterType,
        limit: int = 20,
        page: int = 1,
    ) -> ResponseLoyaltyBonusDetails:
        """
        **Получение детализации по бонусному счету**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-loyalty-account-id-bonus-status-details
        :param account_id: ID участия в программе лояльности
        :param status: Статус бонусов
        :param filter_data: Фильтр
        :param limit: Количество элементов на странице
        :param page: Номер страницы
        """
        response = await self._client.get(
            f"/loyalty/account/{account_id}/bonus/{status}/details",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )

        response_obj = ResponseLoyaltyBonusDetails.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def bonus_operations(
        self,
        filter_data: LoyaltyBonusOperationsApiFilterType,
        limit: int = 20,
        cursor: str = None,
    ) -> ResponseLoyaltyBonusOperations:
        """
        **История бонусного счета для всех участий**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-loyalty-bonus-operations
        :param filter_data: Фильтр
        :param limit: Количество элементов на странице
        :param cursor: Курсор
        """
        response = await self._client.get(
            "/loyalty/bonus/operations",
            params={
                "limit": limit,
                "cursor": cursor,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )

        response_obj = ResponseLoyaltyBonusOperations.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def calculate(
        self, site: str, order: SerializedOrder, bonuses: float = 0
    ) -> ResponseLoyaltyCalculate:
        """
        **Расчёт максимальной скидки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-loyalty-calculate
        :param site: Символьный код магазина
        :param order: Заказ
        :param bonuses: Количество бонусов
        """
        response = await self._client.post(
            "/loyalty/calculate",
            params={"site": site},
            data={
                "order": order.model_dump_json(exclude_none=True, by_alias=True),
                "bonuses": bonuses,
            },
        )
        response_obj = ResponseLoyaltyCalculate.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def loyalties_filter(
        self, filter_data: LoyaltyApiFilterData, limit: int = 20, page: int = 1
    ) -> ResponseLoyaltiesFilter:
        """
        **Список программ лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-loyalty-loyalties
        :param filter_data: Фильтр
        :param limit: Количество элементов на странице
        :param page: Номер страницы
        :return: LoyaltiesResponse
        """
        response = await self._client.get(
            "/loyalty/loyalties",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )

        response_obj = ResponseLoyaltiesFilter.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def loyalty_get(self, loyalty_id: int) -> ResponseLoyaltyRetrieve:
        """
        **Получение информации о программе лояльности**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-loyalty-loyalties-id
        :param loyalty_id: ID программы лояльности
        :return: LoyaltiesResponse
        """
        response = await self._client.get(f"/loyalty/loyalties/{loyalty_id}")

        response_obj = ResponseLoyaltyRetrieve.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj
