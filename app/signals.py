def internal_score(req) -> float:
    score = 0.0
    if req.days_since_policy_start < 30:
        score += 0.4
    if req.claims_last_3_years >= 2:
        score += 0.3
    if req.peril in {"theft", "accidental_damage"}:
        score += 0.1
    return min(score, 1.0)
