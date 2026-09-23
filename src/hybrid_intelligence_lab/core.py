from __future__ import annotations
import numpy as np, pandas as pd

def route_decision(h_pred:int,a_pred:int,h_conf:float,a_conf:float,threshold:float=.15)->tuple[int,str]:
    if h_pred==a_pred: return h_pred,'agreement'
    if abs(h_conf-a_conf)<threshold: return h_pred,'human_default'
    return (h_pred,'human') if h_conf>a_conf else (a_pred,'ai')

def evaluate(df: pd.DataFrame, threshold:float=.15)->dict:
    routed=[route_decision(r.human_pred,r.ai_pred,r.human_conf,r.ai_conf,threshold) for r in df.itertuples()]
    pred=np.array([x[0] for x in routed]); route=[x[1] for x in routed]
    y=df.y.to_numpy()
    human=(df.human_pred.to_numpy()==y); ai=(df.ai_pred.to_numpy()==y)
    return {
      'human_accuracy':float(human.mean()),'ai_accuracy':float(ai.mean()),'hybrid_accuracy':float((pred==y).mean()),
      'complementarity_rate':float((human ^ ai).mean()),'override_gain':float(((pred==y)&(~ai)&human).mean()),
      'deferral_rate':float(np.mean(np.array(route)=='human_default'))
    }

def threshold_sweep(df:pd.DataFrame, thresholds=(0,.05,.1,.15,.2,.3)) -> pd.DataFrame:
    return pd.DataFrame([{'threshold':t,**evaluate(df,t)} for t in thresholds])
