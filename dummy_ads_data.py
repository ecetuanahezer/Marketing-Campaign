import random

# campaigns
campaigns = [
    {"id": 1, "name": "App Install - IOS", "status": "ENABLED"},
    {"id": 2, "name": "App Install - Android", "status": "PAUSED"},
    {"id": 3, "name": "Retargeting Campaign", "status": "ENABLED"},
]

# Ad groups
ad_groups = [
    {"id": 101, "campaign_id": 1, "name": "iOS Search Ads", "status": "ENABLED"},
    {"id": 102, "campaign_id": 1, "name": "iOS Display Ads", "status": "ENABLED"},
    {"id": 201, "campaign_id": 2, "name": "Android Search Ads", "status": "ENABLED"},
    {"id": 202, "campaign_id": 2, "name": "Android Display Ads", "status": "ENABLED"},
    {"id": 301, "campaign_id": 3, "name": "Retargeting Display Ads", "status": "ENABLED"},
]

# Metrics
metrics = []
for ad_group in ad_groups:
    for day in range(1, 8):  # 1 week of data
        impressions = random.randint(500, 5000)
        clicks = random.randint(50, 500)
        cost = round(random.uniform(20, 200), 2)
        installs = random.randint(10, 100)
        conversions = installs + random.randint(-3, 3)  
        conversions = max(0, conversions)  # no negative conversions
        revenue = round(installs * random.uniform(1.5, 5.0), 2)

        metrics.append({
            "ad_group_id": ad_group["id"],
            "date": f"2025-09-0{day}",
            "impressions": impressions,
            "clicks": clicks,
            "cost": cost,
            "conversions": conversions,  
            "installs": installs,
            "revenue": revenue,
        })

