# Project Overview

## Problem
Determine if an input IP belongs to VPN/Proxy/Tor/Hosting or appears residential, providing an explainable verdict and enrichment.

## Objectives
- Classification with confidence and reasons
- Enrichment with ASN, organization, country, and flags

## Architecture
FastAPI app → provider wrapper → enrichers → heuristics + scoring → JSON responses

Seed data includes Tor exit node list and known hosting/VPN ASNs.
