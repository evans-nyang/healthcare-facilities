# Healthcare Facilities Grafana Dashboard

Response time:

```sql
SELECT 
  timestamp AS time,
  response_time
FROM conversations
ORDER BY timestamp
```

Relevance:

```sql
SELECT 
  relevance,
  COUNT(*) AS count
FROM conversations
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo() 
GROUP BY relevance
```

Model used:

```sql
SELECT
  model_used,
  COUNT(*) AS count
FROM conversations
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo() 
GROUP BY model_used
```

Openai cost:

```sql
SELECT
  timestamp AS time,
  openai_cost
FROM conversations
WHERE openai_cost > 0
ORDER BY timestamp
```

Recent conversations:

```sql
SELECT
  timestamp AS time,
  question,
  answer,
  relevance
FROM conversations
ORDER BY timestamp DESC
LIMIT 5
```

Feedback statistics:

```sql
SELECT 
  SUM(CASE WHEN feedback > 0 THEN 1 ELSE 0 END) as thumbs_up,
  SUM(CASE WHEN feedback < 0 THEN 1 ELSE 0 END) as thumbs_down
FROM feedback
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo() 
```
