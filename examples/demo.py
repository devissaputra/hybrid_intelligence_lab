from pathlib import Path
import json
from hybrid_intelligence_lab.synthetic import make_decisions
from hybrid_intelligence_lab.core import evaluate, threshold_sweep
root=Path(__file__).resolve().parents[1]; (root/'results').mkdir(exist_ok=True)
df=make_decisions(); sweep=threshold_sweep(df); metrics=evaluate(df)
df.to_csv(root/'results'/'synthetic_decisions.csv',index=False); sweep.to_csv(root/'results'/'routing_sweep.csv',index=False)
(root/'results'/'demo_metrics.json').write_text(json.dumps({k:round(v,3) for k,v in metrics.items()},indent=2)); print(json.dumps({k:round(v,3) for k,v in metrics.items()},indent=2))
