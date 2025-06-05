def detect_liquidity_risk(lp_locked_ratio, recent_drops):
    if lp_locked_ratio < 0.3 or recent_drops > 2:
        return "Liquidity Risk"
    if lp_locked_ratio < 0.5:
        return "Watch"
    return "Safe"

def detect_ownership_concentration(top_holders):
    total = sum(top_holders)
    if total > 70:
        return "Centralized"
    if total > 40:
        return "Moderate"
    return "Decentralized"

def run_risk_checks(token_data):
    lp_status = detect_liquidity_risk(token_data["lp_locked"], token_data["drops"])
    ownership = detect_ownership_concentration(token_data["top_holders"])
    return {
        "liquidity": lp_status,
        "ownership": ownership
    }

tokens = [
    {"lp_locked": 0.25, "drops": 3, "top_holders": [25, 30, 20]},
    {"lp_locked": 0.65, "drops": 1, "top_holders": [10, 12, 9]},
    {"lp_locked": 0.4, "drops": 2, "top_holders": [20, 18, 10]},
    {"lp_locked": 0.55, "drops": 0, "top_holders": [8, 7, 6]}
]

for idx, t in enumerate(tokens):
    status = run_risk_checks(t)
    print(f"Token {idx + 1}: Liquidity = {status['liquidity']}, Ownership = {status['ownership']}")