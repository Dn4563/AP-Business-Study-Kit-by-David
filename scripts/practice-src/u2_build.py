import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import build, TIPS
from u2_mock import SM, QM
from u2_sets import SS, QS, MATH
def sec(name, items, seed, sources, prefix, **kw):
    used = {q[0] for q in items if q[0]}
    return dict(name=name, mode=kw.pop("mode", "practice"), tips=TIPS, sources={k: v for k, v in sources.items() if k in used}, questions=build(prefix, items, seed), **kw)
out = {"sections": [
 sec("Set A: Customers and research (2.1-2.3)", [q for q in QS if q[0] in ("P1", "P2")], 13, SS, "TA"),
 sec("Set B: Promotion (2.7)", [q for q in QS if q[0] == "P3"], 14, SS, "TB"),
 sec("Math drills: CAC, markup, margin, CTR, conversion, ROAS", MATH, 15, {}, "MM"),
 sec("Mock test (40 questions)", QM, 61, SM, "MX", mode="exam", exam="Mock test",
     examTips=["Built like your Unit 1 test: 40 multiple-choice questions, one scenario per page, 5 questions each. Your Unit 2 test format isn't known yet.",
               "Turn the Timer on and leave Shuffle off. About one minute per question.",
               "Many questions have two good answers: choose the one the scenario supports best."]),
]}
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../content/unit-02/practice.json")
json.dump(out, open(p, "w"), indent=1, ensure_ascii=False); print("wrote", p)
