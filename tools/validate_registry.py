#!/usr/bin/env python3
"""Validate public registry structure without contacting task platforms.

Never equates registration with successful execution. Does not sync schedules.
"""
from collections import Counter
from pathlib import Path
import argparse
import datetime as dt
import sys

import yaml


def validate(path: Path) -> list[str]:
    errors = []
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return ["registry root is not a mapping"]
    if data.get("schema_version") != 1:
        errors.append("unexpected schema_version")
    if data.get("timezone") != "Asia/Shanghai":
        errors.append("unexpected timezone")
    try:
        dt.date.fromisoformat(str(data.get("updated")))
    except ValueError:
        errors.append("updated must be a date")
    tasks = data.get("automations")
    if not isinstance(tasks, list):
        return errors + ["automations must be a list"]
    if len(tasks) != 22:
        errors.append(f"expected 22 local registration entries, got {len(tasks)}")
    for field in ("slug", "id"):
        values = [t.get(field) for t in tasks if isinstance(t, dict)]
        if len(values) != len(tasks) or any(not isinstance(v, str) or not v.strip() for v in values):
            errors.append(f"missing or invalid local {field}")
        dupes = [v for v, n in Counter(values).items() if n > 1]
        if dupes:
            errors.append(f"duplicate local {field}: {len(dupes)}")
    if Counter(t.get("status") for t in tasks) != {"ACTIVE": 20, "PAUSED": 2}:
        errors.append("local status count deviates from documented 20/2 baseline")
    for task in tasks:
        if not isinstance(task, dict):
            errors.append("local task must be mapping")
            continue
        schedule = task.get("schedule")
        # A paused, retired platform task may intentionally have no schedule.
        if task.get("status") == "ACTIVE" and (not isinstance(schedule, dict) or not schedule.get("cron")):
            errors.append(f"active task missing schedule: {task.get('slug', '<unknown>')}")
    segments = data.get("platform_segments", {})
    for name, expected in (("claude_cloud", (18, 1)), ("chatgpt", (1, 0))):
        segment = segments.get(name) if isinstance(segments, dict) else None
        entries = segment.get("tasks") if isinstance(segment, dict) else None
        if not isinstance(entries, list):
            errors.append(f"missing {name} platform tasks")
            continue
        counts = Counter(t.get("status") for t in entries if isinstance(t, dict))
        if counts != {"ACTIVE": expected[0], **({"PAUSED": expected[1]} if expected[1] else {})}:
            errors.append(f"{name} unexpected status counts: {dict(counts)}")
        slugs = [t.get("slug") for t in entries if isinstance(t, dict)]
        if len(slugs) != len(entries) or any(not slug for slug in slugs) or len(set(slugs)) != len(slugs):
            errors.append(f"{name} missing/duplicate slug")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="?", default="registry/AUTOMATIONS.yaml")
    args = parser.parse_args()
    problems = validate(Path(args.file))
    for problem in problems:
        print("FAIL:", problem)
    if problems:
        sys.exit(1)
    print("PASS: registry structure and expected baseline counts (NOT task runtime verification)")
