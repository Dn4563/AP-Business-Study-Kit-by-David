import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import build, TIPS
from u1_mock import SM, QM
from u1_sets import SS, QS, MATH
def sec(name, items, seed, sources, prefix, **kw):
    used = {q[0] for q in items if q[0]}
    return dict(name=name, mode=kw.pop("mode", "practice"), tips=TIPS, sources={k: v for k, v in sources.items() if k in used}, questions=build(prefix, items, seed), **kw)
out = {"sections": [
 sec("Set A: Markets, PESTEL and new ideas (1.1-1.4)", [q for q in QS if q[0][0] == "A"], 3, SS, "SA"),
 sec("Set B: Structures, ethics and supply chains (1.5-1.8)", [q for q in QS if q[0][0] == "B"], 4, SS, "SB"),
 sec("Math drills: profit, value capture, market share", MATH, 5, {}, "MD"),
 sec("Mock test (40 questions)", QM, 51, SM, "MK", mode="exam", exam="Mock test",
     examTips=["Like the real Unit 1 test: 40 multiple-choice questions, one scenario per page, 5 questions each.",
               "Turn the Timer on and leave Shuffle off. About one minute per question.",
               "Many questions have two good answers: choose the one the scenario supports best."]),
]}
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../content/unit-01/practice.json")
json.dump(out, open(p, "w"), indent=1, ensure_ascii=False); print("wrote", p)
