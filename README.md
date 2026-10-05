# fraud-scoring

Scores every new claim for fraud risk between 0 and 1. Combines our own signals (claim soon after policy start, repeat claims, address changes) with a score from an external fraud data vendor.

Owned by **Claims / Handling squad**. On-call: `#tw-claims`.

| Contract | Kind | Direction |
| --- | --- | --- |
| `POST /v1/scores` | REST | provides (claims-management) |
| `claims.claim.reported` | Event | subscribes |
| `fraud.score.flagged` | Event | publishes when the score is above 0.8 |
