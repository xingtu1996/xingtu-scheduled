# Registry 同步说明（2026-11-02）

性质：登记同步 PR 的说明文件。本 PR 只更新登记与说明，未激活、暂停、删除或修改任何任务的排期、状态与执行逻辑；新 PR 保持 Draft，供独立审核。

## 一、本次同步内容

1. registry/AUTOMATIONS.yaml 文件头 updated 由 2026-10-14 更新为 2026-11-02。
2. 新增顶层 platform_segments 平台段：
   - claude_cloud：Muse 云端调度器 19 条（18 ACTIVE / 1 PAUSED），逐条登记 slug、排期、状态、唯一主执行者、产物类别；失败凭证来源为云端调度器运行记录。
   - chatgpt：ChatGPT 远端总监控 1 条（每日 08:30、周日深度复盘，ACTIVE），只读告警、不执行。
3. 本地平台（WorkBuddy）原 22 条条目本体未改动；其与实际运行状态的差异见第二节。

## 二、原 22 条登记与实际运行状态差异（证据等级口径同审计报告四级）

| 登记条目 | 登记状态 | 运行证据等级（2026-11-02） | 备注 |
|---|---|---|---|
| daily-trend-scan | ACTIVE | artifact_observed | 产物至 2026-11-01 |
| mp-data-review-daily | ACTIVE | artifact_observed | 复盘报告至 2026-11-02；其 stats 快照子环节 artifact_stale（见 C-06） |
| free-compute-daily | ACTIVE | artifact_observed | 日刊至 2026-11-01 |
| wechat-tuitu-daily | ACTIVE | artifact_observed | 仅产物变化（卡片编号至 034），无运行记录直证 |
| daily-publish-flywheel | ACTIVE | artifact_observed | 飞轮产物至 2026-11-02 |
| opensource-matrix-weekly | ACTIVE | artifact_observed | 登记「每周三」、实际连续日更（频率漂移，见 C-05） |
| ops-feed-daily-push | ACTIVE | artifact_observed | manifest updated_at 2026-11-02 00:32 |
| skill-library-weekly-checkup | ACTIVE | unverified | 最新报告 2026-10-25，疑缺一期（见 C-08） |
| github-article-reflux | ACTIVE | unverified | 近 7 天未取得运行证据 |
| session-broadcast-collect | ACTIVE | unverified | 近 7 天未逐项取得证据 |
| ai-collab-miner-daily | ACTIVE | unverified | 同上 |
| materials-library-weekly-refresh | ACTIVE | unverified | 同上 |
| monetization-flywheel-weekly | ACTIVE | unverified | 同上 |
| toolbelt-weekly-scan | ACTIVE | unverified | 同上 |
| yuanbao-archive | ACTIVE | unverified | 同上 |
| session-archive | ACTIVE | unverified | 同上 |
| knowledge-payment-reminder | ACTIVE | unverified | 提醒类，无产物证据面 |
| mem-exam-daily-reminder | ACTIVE | unverified | 提醒类，无产物证据面 |
| desk-data-daily-sync | ACTIVE | unverified | 近 7 天未逐项取得证据 |
| skill-evolution-miner | ACTIVE | unverified | 同上 |
| workspace-batch1-housekeeping | PAUSED | — | 维持暂停登记 |
| cloud-ai-news-summary | PAUSED | — | 能力已由云端 daily-trend-digest 承接（状态错位，见 C-09） |

## 三、脱敏检查结果

- 新增 platform_segments 只含条目元数据（slug/排期/状态/主执行者/产物类别/失败凭证来源），无 prompt 正文、无私人绝对路径（沿用占位符口径）、无内部业务代号、无密钥。
- 本说明文件同样口径：只记条目名、日期与证据等级，不摘录私有真源与 prompt 内容。
- 检查方式：提交前全文检索密钥样字符串、私人路径模式与代号表，结果为零命中（Muse 自查；独立复核以本 PR 审核为准）。

## 四、私有真源状态（如实标注）

- 纪律要求「先回写私有真源、再同步公开镜像」。私有全量真源位于 boss 本地工作区（云端不可达），本次无法由 Muse 在云端先行回写。
- 因此本 PR 先行完成公开镜像补登；私有真源的回写（补入云端 19 条与 ChatGPT 监控、校准 22 条状态）列为本地待办，需 boss 或本地 Agent 在本机执行后与本镜像再对一次账。此项未完成前，本镜像与私有真源之间仍可能存在细节差异，特此标注，不冒充已对齐。

## 五、验收

- YAML 已通过解析校验；顶层新增 platform_segments 与原结构并存，原 automations 段未改动。
- 本 PR 未产生任何任务状态变更、重复任务或外部发布。
