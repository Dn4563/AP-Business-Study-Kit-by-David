import json, random
PRAC = "Practice scenario written for this kit from your class materials; the company is made up."
def src(title, attr, paras, label=PRAC): return {"title": title, "attr": attr, "label": label, "paras": paras}
def tsrc(title, attr, paras, table, label=PRAC): return {"title": title, "attr": attr, "label": label, "paras": paras, "table": table}
def build(prefix, items, seed):
    n = len(items); order = ([0,1,2,3]*n)[:n]; random.Random(seed).shuffle(order); qs = []
    for i, (s, skill, topic, stem, right, wrongs, exp) in enumerate(items):
        assert len(wrongs) == 3, stem
        assert len(right) < max(len(w[0]) for w in wrongs), f"{prefix}{i+1}: right longest: {right}"
        t = order[i]; opts = [w[0] for w in wrongs]; why = [w[1] for w in wrongs]
        opts.insert(t, right); why.insert(t, "")
        q = {"id": f"{prefix}-{i+1}", "type": "mcq", "skill": skill, "topic": topic, "stem": stem,
             "options": opts, "ans": t, "exp": exp, "why": why}
        if s: q["src"] = s
        qs.append(q)
    L = "".join("ABCD"[q["ans"]] for q in qs); print(prefix, {c: L.count(c) for c in "ABCD"}); return qs
