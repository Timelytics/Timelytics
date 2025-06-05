def calc_volume_score(volume):
    return min(volume / 1000, 40)

def calc_wallet_activity_score(wallets):
    score = 0
    for w in wallets:
        score += w["tx_count"] * 0.3 + w["volume"] * 0.001
    return min(score, 30)

def calc_transaction_score(tx_count):
    return min(tx_count * 0.5, 30)

def total_token_score(volume, tx_count, wallets):
    v_score = calc_volume_score(volume)
    w_score = calc_wallet_activity_score(wallets)
    t_score = calc_transaction_score(tx_count)
    return round(v_score + w_score + t_score, 2)

def evaluate_token(name, data):
    score = total_token_score(data["volume"], data["tx_count"], data["wallets"])
    label = "High" if score > 70 else "Medium" if score > 45 else "Low"
    return f"{name} → Score: {score} | Risk: {label}"

def get_sample_wallets(count):
    return [{"tx_count": i % 10 + 1, "volume": 1000 * (i % 5 + 1)} for i in range(count)]

def run_evaluation():
    tokens = [
        {
            "name": "Alpha",
            "volume": 110000,
            "tx_count": 90,
            "wallets": get_sample_wallets(20)
        },
        {
            "name": "Beta",
            "volume": 75000,
            "tx_count": 60,
            "wallets": get_sample_wallets(15)
        }
    ]
    for token in tokens:
        print(evaluate_token(token["name"], token))

run_evaluation()