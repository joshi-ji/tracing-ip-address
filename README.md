# Tracing IP Address Behind VPN/Proxy

A minimal, production-ready web API that classifies an input IP as VPN/Proxy/Tor/Hosting or Residential, explains the verdict with a confidence score and reasons, and returns ASN/organization enrichment.

What it does: detect likely anonymity usage and provide provider/context details; it does not reveal a “real IP behind” a VPN/proxy on the open Internet.

## Features
- Classify IPs via a configurable provider plus heuristics (Tor exit list, known hosting/VPN ASNs).
- Enrich responses with ASN, AS name, organization, country, hosting_flag, tor_flag.
- Clean FastAPI structure, auto-generated docs at /docs, basic tests, and containerization assets.

## Quickstart
1) Copy `.env.example` to `.env` and set API keys/tokens.
2) Install: `pip install -r requirements.txt` or use pyproject with a modern tool.
3) Run: `uvicorn src.app.main:app --reload` and open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Scope and limits
- Universal deanonymization is out of scope and generally infeasible without provider cooperation or endpoint instrumentation; this project focuses on detection and enrichment.

Documentation is provided in `docs/` — OVERVIEW, SETUP, API, METHODS, LIMITATIONS, REFERENCES.

License: MIT (see LICENSE).
