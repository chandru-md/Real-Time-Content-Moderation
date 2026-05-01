def decide(result: dict):
    """
    Converts model output → final moderation decision.

    Threshold Logic:
    - <0.3 → ALLOW (safe)
    - 0.3–0.7 → FLAG (uncertain)
    - >0.7 → BLOCK (high risk)
    """

    confidence = result["confidence"]

    if confidence < 0.3:
        return {"decision": "ALLOW", "confidence": confidence, "reason": "SAFE"}

    elif confidence < 0.7:
        return {"decision": "FLAG", "confidence": confidence, "reason": "REVIEW"}

    else:
        return {"decision": "BLOCK", "confidence": confidence, "reason": "TOXIC"}