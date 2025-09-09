# Tracing-ip-address
This is the final year project for btech in the field of cyber-security which deals with tracing of ip address behind the vpn/proxy servers.

Tracing IP Address Behind VPN/Proxy
A light, production-quality web API that categorizes an input IP as VPN/Proxy/Tor/Hosting or Residential, provides the conclusion with a confidence value and justification, and includes ASN/organization enrichment.
What it does: identify probable anonymity use and return provider/context information; it doesn't uncover a "real IP behind" a VPN/proxy on the public Internet.

Features

Classify IPs through a configurable provider and heuristics (Tor exit list, known hosting/VPN ASNs).

Enrich responses with ASN, AS name, organization, country, hosting_flag, tor_flag.

Clean FastAPI structure, auto-generated docs at /docs, basic tests, and containerization assets.

Quickstart

Copy .env.example to .env and configure API keys/tokens.

Install: pip install -r requirements.txt or use pyproject with a modern tool.

Run: uvicorn src.app.main:app --reload and open ttp://127.0.0.1:8000/docs.

ope and limits
Universal deanonymization is out of scope and usually infeasible without provider cooperation or endpoint instrumentation; this project concentrates on detection and enrichment.

Docs in docs/: OVERVIEW, SETUP, API, METHODS, LIMITATIONS, REFERENCES.
License: MIT (see LICENSE).

