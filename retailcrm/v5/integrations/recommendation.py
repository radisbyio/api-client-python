from typing import Protocol

from retailcrm.v5.schemas.requests.recommendation import RecommendationRequest
from retailcrm.v5.schemas.responses.recommendation import RecommendationResponse

__all__ = ["RecommendationActions"]
class RecommendationActions(Protocol):
    async def recommendation(self, request: RecommendationRequest) -> RecommendationResponse:
        pass
