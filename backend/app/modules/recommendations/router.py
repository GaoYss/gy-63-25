from fastapi import APIRouter, Query

from app.modules.recommendations.models import FruitRecommendation
from app.modules.recommendations.service import list_origins, list_recommendations

router = APIRouter()


@router.get("", response_model=list[FruitRecommendation])
def get_recommendations(
    member_id: int | None = Query(default=None, gt=0),
    origin: str | None = Query(default=None),
) -> list[FruitRecommendation]:
    return list_recommendations(member_id, origin)


@router.get("/origins", response_model=list[str])
def get_origins() -> list[str]:
    return list_origins()
