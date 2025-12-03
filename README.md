# Подготовка виртуальной машины


```
python3 -m venv env_recsys_start
```

```
. env_recsys_start/bin/activate
```

```
pip install -r requirements.txt
```

Сервис Feature Store 
```
uvicorn features_service:app --port 8010
```

Сервис Event Store
```
uvicorn events_service:app --port 8020
```

Сервис Recomendations
```
uvicorn recommendation_service:app
```

Тестирование
```
python test_service.py
```




