from src.app.services.enrichers import enrich_asn_org

def test_enrich_basic_fields():
    raw = {
        "as_number": "54321",
        "as_name": "ENRICH-AS",
        "isp": "Enrich ISP",
        "country_name": "XY",
        "proxy": True,
        "tor": False
    }
    enriched = enrich_asn_org(raw)
    assert enriched["asn"] == 54321
    assert enriched["as_name"] == "ENRICH-AS"
    assert enriched["org"] == "Enrich ISP"
    assert enriched["country"] == "XY"
    assert enriched["hosting_flag"] is True
    assert enriched["tor_flag"] is False
