# 定时任务盘点报告（2026-11-02）

审计执行：Muse（云端）只读审计。审计时间：2026-11-02 04:40–05:10（北京时间）；复核：2026-11-02 上午二次复核，基线未变——本仓 main 头 SHA（15762cbd…）与 registry blob SHA（8fb018dc…）与凌晨审计一致，云端 cron 清单仍为在册 19 个（18 启用、1 暂停）；ChatGPT 总监控已于当日创建（每日 08:30、周日深度复盘）。
验收口径：以运行日志、配置与实际产物为准；云端无法直接核实的本地运行时事项一律标「待验证」，不以任何 Agent 自述为准。
脱敏口径：本文不含原始会话、密钥、私人绝对路径与内部项目代号；任务只记名称、排期、状态与产物落点类别。
修正记录：2026-11-02 ChatGPT 独立审核（针对提交 abd8adc）提出四项修正——关键结论补可追溯证据、成功状态按证据强度分级、冲突逐项补 evidence_ref、告警规则与文档链接统一；本版已逐项修正，运行状态口径以本版四级为准。

## 一、审计范围与证据来源

| 证据源 | 可达性 | 用途 |
|---|---|---|
| 本仓 registry/AUTOMATIONS.yaml（公开镜像） | 已实读，blob SHA 8fb018dc | 登记基线：22 条 |
| 私有仓定时任务档案 AUTOMATIONS.yaml（镜像） | 已实读 | 交叉对照：updated 停在 2026-09-30 |
| 私有仓定时任务产出（manifest.json / stats / 各任务产物目录） | 已实读 | 近 7 天产物证据 |
| Muse 云端调度器（cron 清单与运行记录） | 已实读 | 云端运行面：业务任务 19 个 |
| GitHub 仓库面（提交、PR、Issue、workflows 目录） | 已实读 | 巡检与发布凭证 |
| 本地设备运行时（WorkBuddy / Claude Code / Codex 本地配置与日志） | 云端不可达 | 全部标「待验证」，以登记与产物侧面核对 |

私有全量登记真源位于用户本地工作区（云端不可读）；本仓 registry 是其脱敏公开镜像，文件头 updated 为 2026-10-14。

## 二、登记总览

- 登记总数：22 条（ACTIVE 20 / PAUSED 2）。
- 构成：以本地平台（WorkBuddy）任务为主，覆盖会话采集、资讯扫描、公众号数据复盘与贴图生产、发布飞轮、素材与技能维护、产出推送等；另有已暂停的云端资讯总结 1 条、工作区收纳 1 条。
- 登记文件状态：公开镜像 updated 2026-10-14（19 天未更新）；私有仓镜像 updated 2026-09-30（33 天未更新）；本仓最近一次「登记表同步」提交为 2026-10-15，此后提交均为门面与治理类，未再同步登记内容。

## 三、实际运行面

### 3.1 本地平台（登记 22 条，运行证据分级）

近 7 天有产物证据（产物经每晚推送进入私有仓，可核验）在跑的任务（至少 8 个）：
- 每日舆情扫描：产物到 2026-11-01，每日连续。
- 公众号数据复盘：复盘报告到 2026-11-02。
- 免费算力日刊：到 2026-11-01，日更连续。
- 公众号贴图日更：卡片编号持续增长，源池索引在更新。
- 每日发布飞轮：飞轮周报/运行日志到 2026-11-02。
- 运营日报类产出：到 2026-11-02（与登记条目的对应关系待验证，见第五节）。
- 开源矩阵巡检：产物到 2026-11-01，且为连续日期——实际已是日巡检，与登记的「每周三」不符（漂移，见冲突矩阵 C-05）。
- 产出滚动推送（每晚 23:30）：manifest 更新时间 2026-11-02 00:32，推送链存活。

有产物但已过期：技能库每周体检，最新报告 2026-10-25，此后一个周一周期未见新报告（待验证：缺期或改期）。
其余登记条目（会话采集、对话挖掘、素材刷新、变现飞轮、工具带盘点、会话归档、知识付费提醒、考研提醒、工作台同步、技能进化等）：产物目录存在，但近 7 天更新证据未逐项取得，统一标「待验证」。

### 3.2 Muse 云端（业务任务 19 个）

- 在册 19 个：启用 18、暂停 1（每日性格 Quiz，2026-11-01 满 14 天未完成已暂停，等用户决定去留）。
- 近 7 天有明确成功运行记录的包括：每日早报、每日趋势 digest、每日播客、灵感收割、排期核对、月度复盘、互动周报、FDE 案例集巡检、周三仓库流量巡检。
- 2026-11-02 新增 2 个仓库巡检任务（周一待办推进巡检、每日定时任务仓库巡检），尚未首跑。
- 云端 19 个任务全部未登记进 registry（见冲突矩阵 C-07）。

### 3.3 GitHub Actions

- 未发现以 schedule 触发的 workflow。本仓与技能仓无 workflows 目录；视频工具仓有 CI 与 tag 触发的 release workflow（非定时）。

### 3.4 本仓自身的治理巡检

- 本仓由本地 Agent 以「巡检第 N 轮」节奏维护，2026-10-30 完成第 28 轮，2026-11-01 合入治理 PR #1。该治理巡检本身未在 registry 22 条中登记（见 C-07）。

## 四、产物完整性检查（假成功排查）

- stats 数据快照：最新只到 2026-10-30，缺 2026-10-31、2026-11-01 两天（另 10-23、10-24 历史缺失）。同期 manifest 每晚照常滚动更新、数据复盘报告产出到 2026-11-02——即「推送成功、复盘在产出，但 stats 快照导出环节静默断档」，属典型「任务成功但产物未更新」。下游排期核对与月度复盘已多次因此无快照可验。
- manifest 未归类产出：unknown_in_outputs 累计 122 项，产出索引治理滞后（不影响运行，影响审计可读性）。

## 五、未登记与对应关系待验证

- Muse 云端 19 个任务：未登记（归属口径未定：registry 新增平台段，或只登记在私有档案）。
- 本仓治理巡检（第 28 轮）：未登记。
- 私有仓产出中存在「运营日报、晨间新闻、涨粉选题、今日调度、发布决策」等产物组，与登记 22 条的名称无法一一对应：疑似未登记任务或登记任务的别名产出，待验证。
- ChatGPT 远端监控：已于 2026-11-02 创建（每日 08:30、周日深度复盘），但尚未补登记进 registry，属未登记任务（见冲突矩阵 C-07），补登记待办。

## 六、隐私与公开仓风险

- 本仓 registry 为脱敏公开镜像（路径占位符化、代号泛化）。历史提交显示 2026-10-20、2026-10-22 曾两轮做隐私泛化修复，说明早期版本曾有内部路径/代号进入公开仓并已整改；此后每次同步登记仍须先脱敏复扫。
- 公开的 harness 仓根目录经实查无 scheduled/automations 目录，符合 registry 文件头的红线要求。
- 私有仓档案含未脱敏内容，只在私有仓与本地流转，本审计未将其内容摘录进本仓文档。

## 附、统一执行状态摘要（脱敏，供远端监控直接读取）

字段口径：task_id、owner、schedule、timezone、last_run、status、artifact_path、artifact_updated_at、commit_sha、error_code，证据定位见表后 evidence_ref 索引。status 按证据强度四级：run_success（有对应运行成功记录）/ artifact_observed（仅看到产物变化，无运行记录直证）/ artifact_stale（预期产物过期）/ unverified（证据不足，不判定失败）。commit_sha 只填 Git 提交 SHA；文件 blob SHA 是内容指纹，单独标注、不得混填。未取得的字段填「待验证」，不猜测。产物路径只记相对路径类别，不含私人绝对路径。

| task_id | owner | schedule | timezone | last_run | status | artifact_path | artifact_updated_at | commit_sha | error_code |
|---|---|---|---|---|---|---|---|---|---|
| daily-trend-scan | 本地平台 | 每日 09:00 | Asia/Shanghai | 2026-11-01 | artifact_observed | 私有仓产出/舆情日报 | 2026-11-01 | 待验证 | — |
| mp-data-review-daily | 本地平台 | 每日 09:40 | Asia/Shanghai | 2026-11-02 | artifact_observed | 私有仓产出/数据复盘报告 | 2026-11-02 | 待验证 | — |
| free-compute-daily | 本地平台 | 每日 09:00 | Asia/Shanghai | 2026-11-01 | artifact_observed | 私有仓产出/免费算力日刊 | 2026-11-01 | 待验证 | — |
| wechat-tuitu-daily | 本地平台 | 每日 10:00 | Asia/Shanghai | 待验证 | artifact_observed（仅产物变化，无运行记录直证） | 私有仓产出/贴图卡片 | 待验证 | 待验证 | — |
| daily-publish-flywheel | 本地平台 | 每日 19:00 | Asia/Shanghai | 2026-11-02 | artifact_observed | 私有仓产出/飞轮周报与运行日志 | 2026-11-02 | 待验证 | — |
| opensource-matrix-weekly | 本地平台 | 登记每周三 21:00（实际日更） | Asia/Shanghai | 2026-11-01 | artifact_observed | 私有仓产出/开源矩阵巡检 | 2026-11-01 | 待验证 | SCHEDULE_DRIFT |
| ops-feed-daily-push | 本地平台 | 每日 23:30 | Asia/Shanghai | 2026-11-02 00:32 | artifact_observed | 私有仓产出/manifest.json | 2026-11-02 00:32 | 待验证（Git 提交 SHA 未取得） | — |
| stats-snapshot-export（复盘子环节，非独立登记条目） | 本地平台 | 每日（随复盘与推送链） | Asia/Shanghai | 2026-10-30 | artifact_stale | 私有仓产出/stats | 2026-10-30 | 待验证 | ARTIFACT_STALE |
| skill-library-weekly-checkup | 本地平台 | 每周一 09:40 | Asia/Shanghai | 2026-10-25 | unverified（疑缺一期） | 私有仓产出/技能库体检 | 2026-10-25 | 待验证 | ARTIFACT_MISSING_UNVERIFIED |
| daily-io-briefing | Muse 云端 | 每日 07:00 | Asia/Shanghai | 2026-11-02 | run_success | 主聊交付与当日日志 | 2026-11-02 | — | — |
| daily-trend-digest | Muse 云端 | 每日 07:30 | Asia/Shanghai | 2026-11-02 | run_success | 主聊交付与底稿 | 2026-11-02 | — | — |
| xingtu-podcast-daily | Muse 云端 | 每日约 08:17 | Asia/Shanghai | 2026-11-02 | run_success（第 18 集完结已核验） | 私有播客存档 ep-018 | 2026-11-02 | — | — |
| github-daily-watch | Muse 云端 | 每日约 09:17 | Asia/Shanghai | 待验证（2026-11-02 首跑结果待回） | unverified（首跑结果待回） | 本地巡检日志目录 | 待验证 | 待验证 | — |
| github-backlog-watch | Muse 云端 | 每周一约 09:17 | Asia/Shanghai | 待验证（2026-11-02 首跑结果待回） | unverified（首跑结果待回） | GitHub 维护目标基线目录 | 待验证 | 待验证 | — |
| chatgpt-monitor | ChatGPT | 每日 08:30、周日深度复盘 | Asia/Shanghai | 待验证（2026-11-02 已创建，首跑待回） | unverified（已创建，首跑待回） | ChatGPT 侧通知 | — | — | — |

### evidence_ref 索引（2026-11-02 审核修正补）

相对路径以私有仓 xingtu-vault 为根，产出目录为「03_运营工具箱 (Operations Toolkit)/定时任务产出/」。证据锚点：manifest.json 固定提交链接 https://github.com/xingtu1996/xingtu-vault/blob/94b81baf3269b943007177df70c6750b73cba063/03_%E8%BF%90%E8%90%A5%E5%B7%A5%E5%85%B7%E7%AE%B1%20(Operations%20Toolkit)/%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E4%BA%A7%E5%87%BA/manifest.json（blob SHA f234e6bc…，updated_at 2026-11-02 00:32:51）；产出目录 https://github.com/xingtu1996/xingtu-vault/tree/94b81baf3269b943007177df70c6750b73cba063/03_%E8%BF%90%E8%90%A5%E5%B7%A5%E5%85%B7%E7%AE%B1%20(Operations%20Toolkit)/%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E4%BA%A7%E5%87%BA ；登记文件固定链接 https://github.com/xingtu1996/xingtu-scheduled/blob/15762cbdbb8d986375443cc79b6238596cb0ab40/registry/AUTOMATIONS.yaml（blob SHA 8fb018dc…）。

- daily-trend-scan：产出/舆情日报，最新文件日期 2026-11-01，经 manifest 索引核对。
- mp-data-review-daily：产出/数据复盘报告，最新文件日期 2026-11-02。
- free-compute-daily：产出/免费算力日刊，最新文件日期 2026-11-01。
- wechat-tuitu-daily：产出/贴图卡片，编号持续增长至 034（截至 2026-11-02），仅产物变化证据，无运行记录直证。
- daily-publish-flywheel：产出/飞轮周报与运行日志，最新文件日期 2026-11-02。
- opensource-matrix-weekly：产出/开源矩阵巡检，文件日期连续至 2026-11-01，与登记周排期不符（见冲突矩阵 C-05）。
- ops-feed-daily-push：产出/manifest.json，updated_at 2026-11-02 00:32:51；其 blob SHA f234e6bc… 为文件内容指纹，不是 Git 提交 SHA，故 commit_sha 字段不填此值。
- stats-snapshot-export：产出/stats/，最新 stats_2026-10-30.json；与 manifest updated_at 对照得出断档结论（见 C-06）。
- skill-library-weekly-checkup：产出/技能库体检，最新报告 2026-10-25。
- 云端三条 run_success（daily-io-briefing、daily-trend-digest、xingtu-podcast-daily）：证据为 Muse 云端调度器 2026-11-02 运行记录与交付核验（07:00 早报已交付、07:30 digest 已交付、08:17 播客第 18 集 isComplete 已核验）。此项为 Muse 已核验，ChatGPT 未独立复核。
- github-daily-watch、github-backlog-watch、chatgpt-monitor：2026-11-02 新建或新创建，首跑结果待回，记 unverified。

其余登记条目（会话采集、对话挖掘、素材刷新、变现飞轮、工具带盘点、会话归档、知识付费提醒、考研提醒、工作台同步、技能进化等）近 7 天逐项运行证据未取得，last_run 与 status 统一记「待验证」，见第三节。

## 七、结论

- 登记 22 条、云端在册 19 条、本地近 7 天可证在跑至少 8 条；三方口径不一致的主因不是任务丢失，而是登记三层（私有真源/公开镜像/私有仓镜像）更新节奏脱节，且云端运行面从未纳入登记。
- 冲突与异常共 10 项，详见 TASK_CONFLICT_MATRIX.md；最重要的三项：登记漂移、stats 假成功断档、巡检监控多头重叠。
