- Ensure environment variables in `.env` are correctly filled, especially API keys and provider selection.

## Gunicorn (Manual)
- Run directly using Gunicorn for production: ```gunicorn src.app.main:app --config deployment/gunicorn_conf.py```

- UvicornWorker ensures FastAPI async support.

## Reverse Proxy Setup
- When deploying behind Nginx, Traefik, or another proxy:
- Forward headers such as `X-Forwarded-For` for real client IP detection.
- Always enable HTTPS with valid certificates.
- Example Nginx config:
  ```
  location / {
    proxy_pass http://localhost:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_redirect off;
  }
  ```
- Validate trusted proxy settings if accepting client IPs for reputation.

## Secure Configuration
- Use strong API keys and rotate regularly.
- Set `provider_timeout_ms` and `cache_ttl_seconds` appropriately in `.env`.
- Use Gunicorn `timeout`/`workers` settings in deployment/gunicorn_conf.py for scaling.

## Health & Monitoring
- Health endpoint: `/health` returns status and timestamp for liveness checks.
- Log errors and monitor critical metrics for provider timeouts, API errors, and heuristics misclassifications.

## Updating Heuristic Data
- Update `tor_exit_nodes.txt`, `known_vpn_asn.csv`, and `hosting_asn.csv` periodically for accurate detection.
- Schedule with scripts or CI as needed.

## Troubleshooting
- Use interactive docs at `/docs` to test endpoints.
- Check logs from Docker/Gunicorn for errors.
- Validate dependencies with `pip install -r requirements.txt` inside the container.
