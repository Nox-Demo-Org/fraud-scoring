"""fraud-scoring: POST /v1/scores, and a subscriber on claims.claim.reported."""

from fastapi import FastAPI
from pydantic import BaseModel

from .signals import internal_score
from .vendor import vendor_score

app = FastAPI()
FLAG_THRESHOLD = 0.8


class ScoreRequest(BaseModel):
    claim_id: str
    policy_id: str
    customer_id: str
    peril: str
    days_since_policy_start: int
    claims_last_3_years: int


@app.post("/v1/scores")
def score(req: ScoreRequest) -> dict:
    ours = internal_score(req)
    theirs = vendor_score(req.customer_id, req.peril)
    total = round(0.6 * ours + 0.4 * theirs, 3)
    if total > FLAG_THRESHOLD:
        publish_flag(req.claim_id, total)  # fraud.score.flagged
    return {"claim_id": req.claim_id, "score": total, "flagged": total > FLAG_THRESHOLD}


def publish_flag(claim_id: str, score: float) -> None:
    ...  # topic fraud.score.flagged, payload {claim_id, score, reasons}
