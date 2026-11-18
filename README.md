# 微信读书蒸馏（weread-daily-distill）

WorkBuddy Skill · v1 · 标记：微信读书蒸馏

每日从微信读书书架中，确定性随机（以日期为种子，可复现）抽取一本**已读完、未蒸馏**的书，产出一份"可复利"的深度蒸馏报告：一句话蒸馏 / 热门划线透视 / 思维导图 / 核心概念精读 5 条 / 关键问答 / 三层延伸推荐 / 总评。

## 安装

把本仓库内容放入 WorkBuddy 用户级技能目录：

```
~/.workbuddy/skills/weread-daily-distill/
├── SKILL.md
├── scripts/pick_book.py
└── references/
    ├── report-template.md
    └── fallback-list.md
```

前置依赖：配置 weread MCP（weread_shelf / weread_book_info / weread_notes / weread_reviews），并设置 `WEREAD_API_KEY`（wrk- 前缀密钥）。

## 触发方式

对话中说"每日蒸馏一本书""随机蒸馏""今天蒸馏哪本书""微信读书蒸馏""读书日报"等。

## 设计要点

- **每日一本，同日不重复**：重复触发只补交付既有文件。
- **确定性随机**：`random.Random("YYYY-MM-DD")` 同日重跑结果一致。
- **蒸馏不是缩写**：每条精读落到"机制在什么条件下成立、能解释什么"的可迁移判断标准。
- **数据诚实**：划线聚合≠本人划线、点评接口≠全书差评，口径逐条标注（见 SKILL.md 第 3 步）。
- **交付前八问自检**：对报告自身的强势批判检验（源自《学会提问》T22-T25）。

## 版本

| 版本 | 日期 | 说明 |
|---|---|---|
| 1 | 2026-11-18 | 初始版本：抽取/模板/降级书单/接口口径沉淀 |
