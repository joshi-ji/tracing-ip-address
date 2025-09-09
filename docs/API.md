# API Specification

## Endpoints (v1)
- `POST /api/v1/classify`  
  **Request body:** `{ "ip": "1.2.3.4" }`  
  **Response:** `{ is_privacy, type, confidence, reasons[], sources[] }`

- `GET /api/v1/details/{ip}`  
  **Response:** `{ ip, asn, as_name, org, country, hosting_flag, tor_flag, provider_hits[] }`

- `GET /health` and `GET /version` for operational checks

API documentation and Swagger UI available at `/docs`.
