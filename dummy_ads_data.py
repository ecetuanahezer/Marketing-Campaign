import random

# campaigns
campaigns = [
    {"id": 1, "name": "Summer Sale", "status": "ENABLED"},
    {"id": 2, "name": "Winter Promo", "status": "PAUSED"},
    {"id": 3, "name": "Spring Launch", "status": "ENABLED"},
]

# Ad groups
ad_groups = [
    {"id": 101, "campaign_id": 1, "name": "Shoes", "status": "ENABLED"},
    {"id": 102, "campaign_id": 1, "name": "Bags", "status": "ENABLED"},
    {"id": 201, "campaign_id": 2, "name": "Coats", "status": "PAUSED"},
]

# Metrics
metrics = []
for ad_group in ad_groups:
    for day in range(1, 8):  # 1 week of data
        metrics.append({
            "ad_group_id": ad_group["id"],
            "date": f"2025-09-0{day}",
            "impressions": random.randint(100, 1000),
            "clicks": random.randint(10, 100),
            "cost": round(random.uniform(5, 50), 2),
            "conversions": random.randint(0, 10),  
            "ctr": 0,  # placeholder,
            "cpc": 0   # placeholder
        })

