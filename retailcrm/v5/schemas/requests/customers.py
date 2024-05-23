from datetime import date
from typing import Annotated, List, Optional

from pydantic import BaseModel, BeforeValidator


def _check_custom_field(v: list | dict) -> dict:
    if isinstance(v, list):
        return {}
    return v


class CustomerFilterData(BaseModel):
    ids: List[int] = []
    externalIds: List[str] = []
    name: str = ""
    city: str = ""
    region: str = ""
    sites: List[str] = []
    managers: List[int] = []
    managerGroups: List[str] = []
    notes: str = ""
    vip: bool = False
    bad: bool = False
    discountCardNumber: str = ""
    attachments: int = 0
    tasksCounts: int = 0
    email: str = ""
    contragentName: str = ""
    contragentTypes: List[str] = []
    contragentInn: str = ""
    contragentKpp: str = ""
    contragentBik: str = ""
    contragentCorrAccount: str = ""
    contragentBankAccount: str = ""
    classSegment: str = ""
    minOrdersCount: int = 0
    maxOrdersCount: int = 0
    minAverageSumm: int = 0
    maxAverageSumm: int = 0
    minTotalSumm: int = 0
    maxTotalSumm: int = 0
    minCostSumm: int = 0
    maxCostSumm: int = 0
    dateFrom: Optional[date] = None
    dateTo: Optional[date] = None
    firstOrderFrom: Optional[date] = None
    firstOrderTo: Optional[date] = None
    lastOrderFrom: Optional[date] = None
    lastOrderTo: Optional[date] = None
    customFields: Annotated[dict, BeforeValidator(_check_custom_field)] = {}
    sex: str = ""
    isContact: bool = False
    emailMarketingUnsubscribed: bool = False
    online: bool = False
    segment: str = ""
    commentary: str = ""
    browserId: str = ""
    mgChannels: List[int] = []
    sourceName: str = ""
    mediumName: str = ""
    campaignName: str = ""
    keywordName: str = ""
    adContentName: str = ""
    tags: List[str] = []
    attachedTags: List[str] = []
    countries: List[str] = []
    abandonedCart: bool = False
    mgCustomerId: str = ""
    firstWebVisitFrom: Optional[date] = None
    firstWebVisitTo: Optional[date] = None
    lastWebVisitFrom: Optional[date] = None
    lastWebVisitTo: Optional[date] = None
