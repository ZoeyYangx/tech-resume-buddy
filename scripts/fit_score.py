#!/usr/bin/env python3
"""Compute the fit score and verdict from labeled job requirements, so the same labels always give the same result.

Usage:
  python3 fit_score.py match.json

match.json:
{
  "constraints": [{"name": "Degree level", "status": "pass"}],          # pass | fail | unknown | skipped
  "requirements": [{"label": "SQL", "required": true, "match": "strong"}] # strong | partial | none
}

Rules:
- Score: required items weigh 2, preferred weigh 1. Strong earns full weight, partial half, none zero.
- Verdict: "skip" if any hard constraint fails; "stretch" if 2 or more required items are "none";
  otherwise "worth_applying".
"""
import json
import sys

WEIGHT = {"strong": 1.0, "partial": 0.5}


def fit_score(requirements):
    total = got = 0.0
    counts = {"strong": 0, "partial": 0, "none": 0}
    for r in requirements:
        w = 2 if r.get("required") else 1
        lvl = r.get("match", "none")
        lvl = lvl if lvl in counts else "none"
        total += w
        got += w * WEIGHT.get(lvl, 0)
        counts[lvl] += 1
    return {"score": round(got / total * 100) if total else 0, **counts}


def verdict(constraints, requirements):
    if any(c.get("status") == "fail" for c in constraints):
        return "skip"
    missing_required = sum(1 for r in requirements if r.get("required") and r.get("match", "none") == "none")
    return "stretch" if missing_required >= 2 else "worth_applying"


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as f:
        m = json.load(f)
    reqs, cons = m.get("requirements", []), m.get("constraints", [])
    out = fit_score(reqs)
    out["verdict"] = verdict(cons, reqs)
    out["failed_constraints"] = [c.get("name") for c in cons if c.get("status") == "fail"]
    out["unknown_constraints"] = [c.get("name") for c in cons if c.get("status") == "unknown"]
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
