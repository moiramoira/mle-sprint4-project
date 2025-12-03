import requests
import pandas as pd

recommendations_url="http://127.0.0.1:8000"
features_store_url = "http://127.0.0.1:8010"
events_store_url = "http://127.0.0.1:8020"

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
user_id = 100
event_item_ids = [597199, 1750835, 1750843, 4095918]

for event_item_id in event_item_ids:
    resp = requests.post(events_store_url + "/put", 
                         headers=headers, 
                         params={"user_id": user_id, "item_id": event_item_id})

params={"user_id": 100, "k": 10}

resp_offline = requests.post(recommendations_url + "/recommendations_offline", headers=headers, params=params)
resp_online = requests.post(recommendations_url + "/recommendations_online", headers=headers, params=params)
resp_blended = requests.post(recommendations_url + "/recommendations", headers=headers, params=params)

recs_offline = resp_offline.json()["recs"]
recs_online = resp_online.json()["recs"]
recs_blended = resp_blended.json()["recs"]

items = pd.read_parquet('recsys/data/items.parquet')

def display_items(item_ids):

    item_columns_to_use = ["item_id", "albums", "artists", "genres"]
    
    items_selected = items.query("item_id in @item_ids")[item_columns_to_use]
    items_selected = items_selected.set_index("item_id").reindex(item_ids)
    items_selected = items_selected.reset_index()
    
    print(items_selected)
    
print("Онлайн-события")
display_items(event_item_ids)
print("Офлайн-рекомендации")
display_items(recs_offline)
print("Онлайн-рекомендации")
display_items(recs_online)
print("Рекомендации")
display_items(recs_blended)
                    