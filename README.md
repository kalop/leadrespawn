# Lead Respawn

## Backend Dev
```
pip install -e 
uvicorn app.main:app --reload
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


