# Detection Methods

- **Provider:** One configurable IP intelligence API for base verdict and attributes.
- **Heuristics:** Tor exit node membership, known hosting/VPN ASNs adjust confidence.
- **Scoring:** Provider verdict weighted highest; heuristics add or subtract confidence and reasons.

Combines external labels with transparent, simple rules to reduce false decisions while explaining uncertainty.
