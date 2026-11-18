#!/usr/bin/env python3
"""确定性随机抽取一本书（以当天日期为种子，可复现）。

用法:
    python pick_book.py --candidates candidates.json --exclude-state state.json
    python pick_book.py --fallback  # 降级模式：从内置公共书单抽取

candidates.json: [{"bookId": "...", "title": "...", "author": "..."}]
state.json:      {"distilled": [{"date": "...", "bookId": "...", "title": "..."}],
                  "blacklist": ["书名1", ...]}
"""
import argparse
import datetime
import json
import random
import sys

FALLBACK_LIST = [
    "制造繁荣", "创新者的窘境", "芯片战争", "规模", "系统之美",
    "贫穷的本质", "枪炮病菌与钢铁", "思考快与慢", "人类简史",
    "国富论", "乡土中国", "万历十五年",
]


def load_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates", help="过滤后的候选书单 JSON 路径")
    ap.add_argument("--exclude-state", dest="exclude_state", help="distill-state.json 路径")
    ap.add_argument("--fallback", action="store_true", help="降级模式（无书架数据时）")
    ap.add_argument("--date", default=None, help="覆盖日期（YYYY-MM-DD），默认今天")
    args = ap.parse_args()

    today = args.date or datetime.date.today().isoformat()
    state = load_json(args.exclude_state) if args.exclude_state else {}
    distilled_ids = {str(b.get("bookId")) for b in state.get("distilled", [])}
    blacklist = set(state.get("blacklist", []))

    if args.fallback:
        pool = [{"bookId": "", "title": t, "author": ""} for t in FALLBACK_LIST
                if t not in blacklist]
    elif args.candidates:
        pool = [b for b in load_json(args.candidates)
                if str(b.get("bookId")) not in distilled_ids
                and b.get("title") not in blacklist]
    else:
        print("需要 --candidates 或 --fallback", file=sys.stderr)
        sys.exit(2)

    if not pool:
        print("EMPTY_POOL: 候选为空，所有书均已蒸馏或被过滤", file=sys.stderr)
        sys.exit(1)

    pick = random.Random(today).choice(pool)
    print(json.dumps({"date": today, **pick}, ensure_ascii=False))


if __name__ == "__main__":
    main()
