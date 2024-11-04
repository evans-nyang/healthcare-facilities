# Healthcare Facilities Grafana Dashboard

Response time:

```sql
SELECT 
  timestamp AS time,
  response_time
FROM conversations
ORDER BY timestamp
```

Relvance:

```sql
SELECT 
  relevance,
  COUNT(*) AS count
FROM conversations
GROUP BY relevance
```

Model used:

```sql
SELECT
  model_used,
  COUNT(*) AS count
FROM conversations
GROUP BY model_used
```
