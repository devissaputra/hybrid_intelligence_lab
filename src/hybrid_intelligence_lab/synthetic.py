import numpy as np, pandas as pd

def make_decisions(n=1200,seed=17):
    rng=np.random.default_rng(seed); difficulty=rng.beta(2,2,n); y=rng.integers(0,2,n)
    h_ok=rng.random(n)<(.9-.45*difficulty); a_ok=rng.random(n)<(.86-.32*difficulty)
    hp=np.where(h_ok,y,1-y); ap=np.where(a_ok,y,1-y)
    hc=np.clip(.58+.32*h_ok-.22*difficulty+rng.normal(0,.06,n),.05,.99); ac=np.clip(.58+.32*a_ok-.18*difficulty+rng.normal(0,.06,n),.05,.99)
    return pd.DataFrame({'y':y,'difficulty':difficulty,'human_pred':hp,'ai_pred':ap,'human_conf':hc,'ai_conf':ac})
