from typing import Protocol

from retailcrm.v5.interfaces.integrations import IntegrationActionsInterface
from retailcrm.v5.schemas.requests.recommendation import RecommendationRequest
from retailcrm.v5.schemas.responses.recommendation import RecommendationResponse

__all__ = ["RecommendationActions"]
class RecommendationActions(IntegrationActionsInterface):
    async def recommendation(self, request: RecommendationRequest) -> RecommendationResponse:
        pass
