def detect_entry_pattern(volumes):
    increases = [volumes[i] > volumes[i - 1] for i in range(1, len(volumes))]
    if all(increases[-3:]):
        return "Strong Accumulation"
    if increases[-1] and not any(increases[:-1]):
        return "Sudden Pump"
    return "Normal Flow"

def detect_sells(tx_series):
    sells = [tx for tx in tx_series if tx < 0]
    if len(sells) > len(tx_series) / 2:
        return "Heavy Sell-Off"
    return "Balanced Activity"

patterns = [
    {
        "volumes": [1000, 1500, 1800, 2100],
        "tx_series": [200, -150, -100, -250]
    },
    {
        "volumes": [500, 800, 700, 650],
        "tx_series": [300, 200, 100, -50]
    },
    {
        "volumes": [200, 220, 230, 240],
        "tx_series": [-50, -60, -70, 100]
    }
]

for p in patterns:
    entry = detect_entry_pattern(p["volumes"])
    flow = detect_sells(p["tx_series"])
    print(f"{entry} | {flow}")