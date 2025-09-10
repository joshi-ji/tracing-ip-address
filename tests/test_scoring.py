from src.app.services.scoring import calculate_confidence

def test_confidence_adjustments():
    base = 0.5
    assert calculate_confidence(base, ["tor_exit_node"]) == 0.7
    assert calculate_confidence(base, ["known_vpn_asn"]) == 0.8
    assert calculate_confidence(base, ["known_hosting_asn"]) == 0.7
    assert calculate_confidence(base, ["residential_asn"]) == 0.2

def test_multiple_heuristics():
    base = 0.5
    heuristics = ["known_vpn_asn", "tor_exit_node"]
    result = calculate_confidence(base, heuristics)
    assert result == 1.0  # capped at max 1.0
