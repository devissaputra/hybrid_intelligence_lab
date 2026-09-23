from hybrid_intelligence_lab.core import route_decision, evaluate
from hybrid_intelligence_lab.synthetic import make_decisions

def test_route_agreement():
    assert route_decision(1,1,.4,.9)==(1,'agreement')

def test_metrics():
    m=evaluate(make_decisions(200,3))
    assert all(0<=m[k]<=1 for k in m)
    assert 'hybrid_accuracy' in m
