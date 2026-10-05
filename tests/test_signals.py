from types import SimpleNamespace

from app.signals import internal_score


def test_new_policy_raises_score():
    req = SimpleNamespace(days_since_policy_start=10, claims_last_3_years=0, peril="storm")
    assert internal_score(req) == 0.4
