# Lead Respawn

## Backend Dev
```
pip install -r app/requirements.txt
uvicorn app.main:app --reload
docker run -d --name leadrespawn-redis -p 6379:6379 redis:latest
python -m app.rq_worker generic
```
Test call
```
curl -X POST "http://127.0.0.1:8000/contact/send" \
  -H "Content-Type: application/json" \
  -d '{
    "channel": "whatsapp",
    "to": "+1234567890",
    "message": "Hello from LeadRespawn!"
}'
```


