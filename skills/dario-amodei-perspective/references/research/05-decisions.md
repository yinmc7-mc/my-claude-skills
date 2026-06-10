# Dario Amodei 重大决策与转折点

> 调研日期：2026-05-25
> 覆盖范围：离开OpenAI、创立Anthropic、融资、技术路线、安全政策、治理结构、监管参与、商业化
> 信息源黑名单：已排除知乎、微信公众号、百度百科

---

## 1. 离开 OpenAI，创立 Anthropic（2020-2021）

### 背景
Dario Amodei 于 2016 年加入 OpenAI，逐步升任 VP of Research。其妹 Daniela Amodei 任 VP of Operations。2020 年底，Amodei 与多名核心研究员集体离开 OpenAI，2021 年创立 Anthropic。

### 离开原因（多方信息交叉验证）
1. **安全优先级的根本分歧**：Amodei 一派认为 OpenAI 在安全研究上的投入和优先级不够，发展速度压过了安全考量。
2. **商业化方向冲突**：OpenAI 与微软的合作加深后，组织重心向商业化倾斜。Amodei 等人认为这可能牺牲安全研究的独立性。
3. **治理结构不满**：对 OpenAI 决策透明度和治理方式存在质疑，包括安全考量在开发决策中的权重。
4. **与 Sam Altman 的权力博弈**：WSJ 报道指出，两人之间存在长期的信任裂痕和权力争夺，不仅是理念分歧，也涉及组织控制权。

### 随 Amodei 离开的核心人员
- **Tom Brown**（GPT-3 论文共同作者）
- **Chris Olah**（可解释性研究领军人物）
- 其他多名 OpenAI 技术团队成员

### 结果与影响
- Anthropic 从创立之初就定位为「安全优先的 AI 公司」，这一叙事直接源于创始团队在 OpenAI 的经历。
- 2023 年 11 月 OpenAI 董事会危机期间，董事会曾接触 Amodei，询问他是否愿意接替 Altman 任 CEO——Amodei 拒绝。这一事件凸显两人关系已不可修复。
- 2026 年 2 月印度 AI 峰会上，Altman 和 Amodei 在合影中 visibly 拒绝握手，公开显现裂痕。

### 来源与可信度
- [WSJ: The Decadelong Feud Shaping the Future of AI](https://www.wsj.com/tech/ai/the-decadelong-feud-shaping-the-future-of-ai-7075acde) — 高可信度，一手采访
- [Business Insider: Timeline of Anthropic and OpenAI's Rivalry](https://www.businessinsider.com/sam-altman-dario-amodei-anthropic-openai-rivalry-timeline-2026-2) — 高可信度，综合多方信源
- [ITP.net: OpenAI Board Approached Anthropic CEO](https://www.itp.net/news/openai-board-approached-anthropic-ceo-to-replace-sam-altman) — 中高可信度
- Wikipedia: Anthropic 词条 — 中可信度，综合来源

### 矛盾与不确定性
- Amodei 公开场合很少直接批评 OpenAI，更多强调 Anthropic 的正面使命。但 WSJ 的深度报道揭示私人层面的冲突远比公开表述更激烈。
- 具体离职谈判细节未公开，哪些是「安全理念」分歧、哪些是「人事权力」分歧，外界难以精确区分。

---

## 2. 融资决策：在巨头之间保持平衡（2021-2025）

### 融资时间线

| 轮次 | 金额 | 主要投资方 | 估值 | 年份 |
|------|------|-----------|------|------|
| Series A | $124M | — | — | 2021 |
| Series B | ~$580M | — | — | 2022 |
| Series C | $450M | Spark Capital | — | 2023.05 |
| Google 投资 | $2B+（承诺至 $40B） | Google/Alphabet | ~10% 股权 | 2023 |
| Amazon 投资 | $8B（后续追加至 ~$25B） | Amazon | <20% 股权 | 2023-2024 |
| Series D/E | — | — | $61.5B | 2024 |
| Series F | $13B | ICONIQ | $183B | 2025 |

### 关键决策逻辑
1. **多投资者策略**：同时接受 Google 和 Amazon 两大科技巨头的投资，而非像 OpenAI 那样与单一巨头（微软）深度绑定。表面上看是为了保持独立性。
2. **云服务绑定**：Amazon 提供 5GW 算力，Google 提供百万级云实例。这些不仅是股权投资，更是算力供应合同——投资的大部分资金会以云服务费的形式回流给投资方。
3. **估值飙升**：从 2021 年的初创公司到 2025 年 $183B 估值，4 年增长超过 1000 倍。

### 安全理想与商业现实的张力
- **核心矛盾**：一家以「AI 安全」为使命的公司，接受了总计数百亿美元的大型科技集团投资。这些投资方有各自的商业利益和战略诉求。
- **独立性疑虑**：Google 承诺投资 $40B，Amazon 投资 $25B+ 并签 $100B 云服务合同。批评者质疑 Anthropic 能否在如此深的财务依赖下保持独立安全判断。
- **资金回流结构**：投资方给出的钱大量以云服务采购形式回流，这意味着 Anthropic 对投资方的依赖不仅是股权层面的，更是运营层面的。

### 来源与可信度
- [Anthropic 官方: Series F 公告](https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation) — 极高可信度
- [Anthropic 官方: Amazon Compute 合作](https://www.anthropic.com/news/anthropic-amazon-compute) — 极高可信度
- [CNBC/NBC: Anthropic $61.5B valuation](https://www.nbcnewyork.com/news/business/money-report/amazon-backed-ai-firm-anthropic-valued-at-61-5-billion-after-latest-round/6170698/) — 高可信度
- [Big Technology: Google Struggles to Support Anthropic](https://www.bigtechnology.com/p/google-struggles-to-support-anthropic) — 中高可信度，独立分析
- [Contrary Research: Anthropic Business Breakdown](https://research.contrary.com/company/anthropic) — 中高可信度

### 矛盾与不确定性
- Anthropic 声称多投资者策略是为了保持独立性，但 Google 和 Amazon 各自的巨额投资是否真正赋予了独立性，还是创造了双重依赖，仍有争议。
- 具体投资条款（如董事会席位、否决权、算力锁定条件）未公开，外界无法评估投资方对决策的实际影响力。

---

## 3. Constitutional AI 开发决策（2022）

### 背景
Constitutional AI（CAI）是 Anthropic 的核心技术贡献，也是其区别于 OpenAI RLHF 路线的标志性方法论。

### 方法论核心
1. **第一阶段 - 监督学习**：AI 使用一套书面原则（「宪法」）来评判和修改自己的输出。
2. **第二阶段 - AI 反馈强化学习（RLAIF）**：AI 根据宪法原则评估回复质量，生成偏好数据用于 RL 训练。
3. **核心创新**：减少对人类标注者的依赖，用 AI 自我改进 + 原则引导替代传统 RLHF。

### 决策逻辑
- **研究品味驱动**：Chris Olah 等人的可解释性研究传统在此方法论中有明显体现——追求可理解、可审计的对齐方式。
- **与 OpenAI 的差异化**：OpenAI 走 RLHF（人类反馈强化学习）路线，Anthropic 选择 RLAIF，用「宪法」替代人类偏好数据——这在叙事上强调了对系统性规则的追求而非众包偏好。
- **公开「宪法」**：Anthropic 做了一个不寻常的决策——公开 Claude 的宪法原则。这在商业上不常见，但强化了安全透明的品牌形象。

### 后续发展
- 2023 年推出「Collective Constitutional AI」，探索将民主过程和公众输入纳入 AI 对齐。
- CAI 方法论成为后续所有 Claude 模型的基础。

### 来源与可信度
- [Anthropic 官方: Constitutional AI: Harmlessness from AI Feedback](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) — 极高可信度，一手来源
- [arXiv: Constitutional AI 论文 (2212.08073)](https://arxiv.org/pdf/2212.08073) — 极高可信度，同行评审
- [Anthropic: Claude's Constitution](https://www.anthropic.com/constitution) — 极高可信度
- [Anthropic: Collective Constitutional AI](https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input) — 极高可信度
- [Digi-Con: On 'Constitutional' AI 批评](https://digi-con.org/on-constitutional-ai/) — 中可信度，批评视角

### 矛盾与不确定性
- CAI 的「宪法」由谁制定、如何修订，内部决策过程不透明。公开的宪法是完整版还是精简版，外界无法确认。
- 「减少对人类反馈的依赖」本身是优势还是风险？如果 AI 用自己的判断来训练自己，是否存在循环强化的隐患？批评者认为原则本身不足以保证伦理结果。

---

## 4. Responsible Scaling Policy 安全政策制定（2023-2025）

### 背景
RSP 是 Anthropic 最具标志性的安全承诺框架，借鉴美国生物安全等级（BSL）体系，建立了 AI Safety Levels（ASL）分级制度。

### 政策演进
| 版本 | 时间 | 关键变化 |
|------|------|---------|
| RSP v1.0 | 2023.09 | 首次发布，建立 ASL 框架，定义能力阈值和安全标准 |
| RSP v2.0 | 2024 | 细化阈值和评估流程 |
| RSP v3.0 | 2025 | **重大修订，放宽多项硬性承诺** |

### RSP v3 的争议性修改
1. **放弃硬性阈值触发**：早期版本的某些安全措施由模型能力阈值自动触发。v3 改为更灵活的自主评估。
2. **竞争压力理由**：Anthropic 公开表示，单方面的安全承诺在没有其他公司跟进的情况下会导致竞争劣势。
3. **自我评估权重增加**：新框架更多依赖 Anthropic 的内部评估，而非外部可验证的指标。

### 批评声音
- **Safer AI 组织**认为 v3 是「倒退」，给予 Anthropic 过多自由裁量权来决定模型是否达到安全阈值。
- **Zvi Mowshowitz** 指出 v3 放弃了多项此前做出的具体承诺。
- **EA Forum 帖文**「Anthropic is Quietly Backpedalling on its Safety Commitments」引发广泛讨论。
- **LessWrong 社区**批评「其他人也在这样做」的论点——集体行动问题一直存在，不能作为放宽标准的理由。
- **Marketplace 报道**标题直接点明「Anthropic Loosens Safety Pledge to Compete with its AI Peers」。

### Anthropic 的辩护
- RSP v3 是务实的改进，基于实践经验修正了不切实际的硬性触发机制。
- Holden Karnofsky（Anthropic）公开论证 AGI 竞赛不是协调失败，暗示参与竞赛本身可以是负责任的。
- Anthropic 引入了 Targeted Transparency Framework 作为补充。

### 来源与可信度
- [Anthropic 官方: Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) — 极高可信度
- [Anthropic 官方: RSP v3.0 全文](https://anthropic.com/responsible-scaling-policy/rsp-v3-0) — 极高可信度
- [Anthropic: RSP 原始公告](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) — 极高可信度
- [Governance.AI: RSP v3 分析](https://www.governance.ai/analysis/anthropics-rsp-v3-0-how-it-works-whats-changed-and-some-reflections) — 高可信度，独立分析
- [Zvi Mowshowitz: Anthropic RSP v3 分析](https://thezvi.substack.com/p/anthropic-responsible-scaling-policy) — 中高可信度，有立场的分析
- [Safer AI: RSP v3 批评](https://www.safer-ai.org/anthropics-responsible-scaling-policy-update-makes-a-step-backwards) — 中高可信度
- [LessWrong: RSP v3 讨论](https://www.lesswrong.com/posts/HzKuzrKfaDJvQqmjh/responsible-scaling-policy-v3) — 中可信度，社区讨论
- [Marketplace: Anthropic Loosens Safety Pledge](https://www.marketplace.org/story/2026/02/25/anthropic-loosens-safety-pledge-to-compete-with-its-ai-peers) — 中高可信度
- [EA Forum: Anthropic Backpedalling](https://forum.effectivealtruism.org/posts/kMpf7nYRpTkGh2Qfa/anthropic-is-quietly-backpedalling-on-its-safety-commitments) — 中可信度

### 矛盾与不确定性
- **言行一致性的核心考验**：RSP 从 v1 到 v3 的演变，是 Anthropic 安全承诺含金量最直接的检验。批评者认为这是「先画靶子再射箭」——根据商业需要调整安全标准。
- Anthropic 的辩护（「务实修正」）有一定道理，但「竞争压力」作为理由与创始时的「安全优先」叙事存在张力。
- 没有外部强制执行机制，RSP 的约束力完全依赖于 Anthropic 的自律和声誉考量。

---

## 5. 模型发布策略（2023-2026）

### 发布时间线

| 模型 | 发布时间 | 战略意义 |
|------|---------|---------|
| Claude 1 | 2023.03 | Anthropic 首个生产模型，基于 CAI 训练 |
| Claude 2 | 2023.07 | 性能提升，扩大可用性 |
| Claude 3 系列 | 2024.03 | 三层产品线（Opus/Sonnet/Haiku），对标 OpenAI 全线 |
| Claude 3.5 Sonnet | 2024.06 | **关键拐点**，被广泛认为超越 GPT-4 |
| Claude 4 | 2025.05 | 新一代模型 |
| Claude Opus 4.7 | 2026 | 最新旗舰模型 |

### 核心策略决策
1. **分层产品线**（2024.03）：Claude 3 系列同时发布三个层级（Opus/Sonnet/Haiku），从高端推理到低成本快速响应全覆盖。这是明确对标 OpenAI 的 GPT-4/3.5 产品矩阵。
2. **安全审查作为发布节奏的一部分**：Anthropic 在发布前会进行 RSP 要求的安全评估，这在流程上区别于 OpenAI 的高速迭代模式。
3. **2026 年加速发布**：2026 年起平均每两周发布一个主要更新，52 天内发布 74 个产品更新——与早期「慢但安全」的节奏形成鲜明对比。
4. **从 API 优先到消费产品**：早期主要面向开发者和 API 用户，后续推出 Claude.ai 消费版、Claude Code、Claude Cowork 等产品，进入企业市场和消费者市场。

### 商业结果
- ARR 从 2024 年底的 $1B 增长到 2025 年底的 $9B+，一年增长 9 倍。
- Claude Sonnet 3.5（2024.06）被认为是 Anthropic 的 breakout moment。
- 企业客户策略：强调「安全、可靠」作为差异化卖点。

### 安全与速度的张力
- LinkedIn 分析指出：「即便是以 AI 安全起家的公司，现在也说速度是优先事项。」
- Medium 文章「Safety vs Speed: The Fight That Will Shape Enterprise AI in 2026」报道 Anthropic 内部在安全和速度之间存在紧张关系。
- 2026 年的发布节奏（74 个发布 / 52 天）是否与安全优先的承诺一致，引发质疑。

### 来源与可信度
- [Wikipedia: Claude (Language Model)](https://en.wikipedia.org/wiki/Claude_(language_model)) — 高可信度
- [Taskade: Anthropic History 2026](https://www.taskade.com/blog/anthropic-claude-history) — 中高可信度
- [Anthropic 官方: Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) — 极高可信度
- [FT: Anthropic's Breakout Moment](https://www.ft.com/content/a75555a6-24c3-4468-aba9-7fe12b5def31) — 高可信度
- [Menlo Ventures: 2025 Mid-Year LLM Market Update](https://menlovc.com/perspective/2025-mid-year-llm-market-update/) — 中高可信度
- [Reddit: 74 releases in 52 days](https://www.reddit.com/r/ClaudeAI/comments/1she8ux/anthropic_just_shipped_74_product_releases_in_52/) — 中可信度
- [LinkedIn: Anthropic Speed Over Safety](https://www.linkedin.com/posts/federicojarach_anthropic-just-dropped-its-flagship-responsible-activity-7432880325225213953-lppD) — 中可信度

### 矛盾与不确定性
- 发布节奏从「安全优先的审慎」转向「每两周一次重大更新」，这一转变的内部决策过程不透明。
- 「安全审查」在快速发布节奏中是否仍得到充分执行，外界无法验证。

---

## 6. 治理结构选择：PBC + LTBT（2021-2023）

### 结构设计
Anthropic 选择了双重治理架构：

1. **Public Benefit Corporation（PBC）**：公司法律形态为公益公司，在法律上要求平衡股东利益与公共利益。这与普通商业公司不同，董事会不仅有信义义务最大化股东价值，还有义务推进公益目标。

2. **Long-Term Benefit Trust（LTBT）**：一个独立的信托机构，拥有选举和罢免部分董事会成员的权力。LTBT 的受托人独立于投资者、创始人和管理层，被要求以人类长期利益为导向行动。

### 设计意图
- 明确声称要避免 OpenAI 的治理失误——OpenAI 的非营利/ capped-profit 结构在实际运行中暴露了控制权混乱的问题（2023 年 11 月的董事会危机就是例证）。
- LTBT 被设计为难以撤销的结构性保障，防止「使命漂移」。
- Harvard Law School 的分析将其描述为在利润和公益之间「仔细校准的公司治理机制」。

### 批评与局限
1. **象征性质疑**：ResearchGate 上的学术分析质疑 LTBT 是否有真正的执行权力，还是可能沦为「象征性治理」。
2. **PBC 的法律局限**：美国各州对 PBC 董事会公益义务的执行标准不一，实际约束力可能弱于设计意图。
3. **投资者影响**：Google 和 Amazon 作为巨额投资者，在董事会层面有多大的实际影响力，LTBT 能否有效制衡，尚未经过真正考验。
4. **未经过压力测试**：到目前为止，LTBT 尚未面对过安全使命与商业利益的根本性冲突——真正的考验是当安全要求严重影响估值或投资者回报时，LTBT 会如何运作。

### 来源与可信度
- [Anthropic 官方: The Long-Term Benefit Trust](https://www.anthropic.com/news/the-long-term-benefit-trust) — 极高可信度
- [Harvard Law: Anthropic LTBT](https://corpgov.law.harvard.edu/2023/10/28/anthropic-long-term-benefit-trust/) — 高可信度，学术分析
- [TIME: How Anthropic Designed Itself to Avoid OpenAI's Mistakes](https://time.com/6983420/anthropic-structure-openai-incentives/) — 高可信度
- [AI Invest Brief: Anthropic Business Structure](https://aiinvestbrief.com/anthropic-business-structure-explained/) — 中高可信度
- [ResearchGate: LTBT Structure Analysis](https://www.researchgate.net/figure/Structure-of-Anthropics-Long-Term-Benefit-Trust_fig3_378239309) — 中可信度

### 矛盾与不确定性
- 治理结构的真正效力只能在危机中验证。目前所有关于 LTBT 有效性的判断都是推测性的。
- Anthropic 是否会在未来面临安全使命与投资者回报的根本冲突时真正动用 LTBT 的治理权力，是一个开放问题。

---

## 7. 监管政策立场（2023-至今）

### 关键行动
1. **2023 年 7 月参议院司法委员会证词**：Amodei 出席听证会，主张 AI 监管护栏，强调 AI 带来的严重风险，支持建立监管框架。
2. **持续游说**：Anthropic 积极参与华盛顿政策讨论，推动第三方测试、NIST 标准等具体监管措施。
3. **全州级游说扩展**：NBC 报道 AI 公司（包括 Anthropic）已将游说扩展到美国所有州议会。
4. **AI Lab Watch 追踪**：Anthropic 的政策立场被追踪为支持第三方测试、支持 NIST 资助等。

### 策略分析
- **支持监管的双重动机**：
  - 正面解读：真正相信 AI 风险需要制度性护栏。
  - 策略解读：支持监管也是一种竞争策略——更高的监管门槛有利于已有资源的头部公司，不利于新进入者（监管捕获）。
- **与安全使命的一致性**：在所有 AI 公司 CEO 中，Amodei 对监管的支持态度最为明确和一贯，这与 Anthropic 的安全品牌一致。
- **游说规模**：2025 年有超过 3,500 名联邦游说者涉足 AI 议题，Anthropic 是其中一员。在这个规模下，Anthropic 的游说行动不突出但也非边缘。

### 来源与可信度
- [Senate Judiciary Committee: Amodei 书面证词](https://www.judiciary.senate.gov/imo/media/doc/2023-07-26_-_testimony_-_amodei.pdf) — 极高可信度，一手官方文件
- [YouTube: Amodei 参议院证词视频](https://www.youtube.com/watch?v=3yorhctVvm4) — 极高可信度
- [TIME: AI Lobbying Frenzy](https://time.com/6972134/ai-lobbying-tech-policy-surge/) — 高可信度
- [NBC: Lobbyists for AI in Every Statehouse](https://www.nbcnewyork.com/investigations/i-team-lobbyists-ai-in-every-us-statehouse/6503789/) — 高可信度
- [Public Citizen: Generative Influence](https://www.citizen.org/article/generative-influence/) — 中高可信度
- [AI Lab Watch: Anthropic Policy Advocacy](https://ailabwatch.org/resources/company-advocacy) — 中高可信度

### 矛盾与不确定性
- 支持监管是否包含监管捕获的成分？这是一个无法从外部验证的动机问题。
- Amodei 的监管主张与其公司在快速发布节奏下的实际行为之间存在可观察的张力——呼吁外部监管的同时，公司自身的安全承诺（RSP v3）却在放宽。

---

## 8. 思想输出：「Machines of Loving Grace」（2024.10）

### 概要
Amodei 于 2024 年 10 月发表超过 50 页的长文《Machines of Loving Grace》，系统阐述了他对 AI 积极潜力的愿景——涵盖医疗、心理健康、民主治理等领域的变革。后续发表《The Adolescence of Technology》作为补充。

### 战略意义
- 这是 Anthropic CEO 首次系统性地公开描述 AI 的乐观前景，而不仅是风险警告。
- 发表时机值得注意：正值 Anthropic 加速商业化和融资的时期，一个积极愿景有助于吸引投资和客户。
- 与 Anthropic 安全品牌形成互补：不再只是「我们理解风险」，而是「我们理解风险，也看到巨大的正面可能」。

### 外界评价
- EDRM 称其为「令人耳目一新」。
- Medium 批评文章认为虽然「文笔优秀、深思熟虑、道德严肃」，但体现了 AI 领导者愿景的根本问题。
- LCFI（剑桥未来智能中心）认为这篇文章的重要性在于它来自一个以安全著称的公司 CEO。

### 来源与可信度
- [Dario Amodei: Machines of Loving Grace](https://darioamodei.com/essay/machines-of-loving-grace) — 极高可信度，一手来源
- [Dario Amodei: The Adolescence of Technology](https://www.darioamodei.com/essay/the-adolescence-of-technology) — 极高可信度
- [LCFI: Reflections on Machines of Loving Grace](https://www.lcfi.ac.uk/news-events/blog/post/reflections-on-machines-of-loving-grace) — 高可信度
- [Hacker News 讨论](https://news.ycombinator.com/item?id=41813268) — 中可信度

---

## 综合：言行一致性评估

### 言行基本一致的领域
1. **Constitutional AI 路线**：从 2021 年创立至今，Anthropic 始终以 CAI 作为核心技术路线，没有摇摆。公开「宪法」的决策是真实的透明度贡献。
2. **监管倡导**：Amodei 在公开场合和私下（国会证词）中持续主张 AI 监管，态度一贯。
3. **治理结构投入**：PBC + LTBT 的治理设计在 AI 行业中确实是最制度化的安全承诺结构之一，远超同行。

### 言行存在张力的领域
1. **RSP v3 放宽承诺**：这是最直接的「言行不一致」案例。以安全使命创立的公司，在竞争压力下主动降低了自己的安全标准。Anthropic 的辩护（「务实调整」）部分合理，但「竞争压力」这个理由与创始叙事直接矛盾。
2. **发布节奏加速**：从「审慎安全」到「52 天 74 个发布」，速度优先的转向与安全品牌存在张力。
3. **巨头融资依赖**：接受 Google $40B、Amazon $25B+ 的投资，与「独立安全研究」的叙事存在结构性冲突。
4. **「Race to the top」策略**：Anthropic 主张通过参与前沿竞争来推动安全标准（「在内部做安全」），但 LessWrong 和 EA 社区的批评指出，这个策略的假设——领先者可以同时赢得竞赛和安全——缺乏证据支持。

### 核心判断
Amodei 的决策模式呈现出一个清晰的模式：**在安全理想不变的前提下，对实现手段做务实的、有时是痛苦的妥协**。他不是放弃安全目标的人，但也不是会为了安全目标牺牲公司生存的人。RSP v3 的修改、融资策略的选择、发布节奏的加速，都可以理解为「在安全理想和商业现实之间寻找可行路径」的尝试。

问题是：这条路径是否会越走越窄？随着竞争加剧和投资者期望升高，安全和商业之间的缓冲空间可能继续缩小。Amodei 的真正考验尚未到来——那将是安全要求严重损害 Anthropic 商业利益的时刻。

---

## 来源汇总

### 一手来源（Anthropic 官方）
- [Anthropic: Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy)
- [Anthropic: RSP v3.0](https://anthropic.com/responsible-scaling-policy/rsp-v3-0)
- [Anthropic: The Long-Term Benefit Trust](https://www.anthropic.com/news/the-long-term-benefit-trust)
- [Anthropic: Constitutional AI](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)
- [Anthropic: Claude's Constitution](https://www.anthropic.com/constitution)
- [Anthropic: Series F 公告](https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation)
- [Anthropic: Amazon Compute](https://www.anthropic.com/news/anthropic-amazon-compute)
- [Dario Amodei: Machines of Loving Grace](https://darioamodei.com/essay/machines-of-loving-grace)
- [Dario Amodei: The Adolescence of Technology](https://www.darioamodei.com/essay/the-adolescence-of-technology)
- [Senate: Amodei 证词 PDF](https://www.judiciary.senate.gov/imo/media/doc/2023-07-26_-_testimony_-_amodei.pdf)

### 高可信度二手来源
- [WSJ: The Decadelong Feud](https://www.wsj.com/tech/ai/the-decadelong-feud-shaping-the-future-of-ai-7075acde)
- [Business Insider: Anthropic-OpenAI Rivalry Timeline](https://www.businessinsider.com/sam-altman-dario-amodei-anthropic-openai-rivalry-timeline-2026-2)
- [TIME: How Anthropic Designed Itself](https://time.com/6983420/anthropic-structure-openai-incentives/)
- [Harvard Law: Anthropic LTBT](https://corpgov.law.harvard.edu/2023/10/28/anthropic-long-term-benefit-trust/)
- [FT: Anthropic's Breakout Moment](https://www.ft.com/content/a75555a6-24c3-4468-aba9-7fe12b5def31)
- [Governance.AI: RSP v3 Analysis](https://www.governance.ai/analysis/anthropics-rsp-v3-0-how-it-works-whats-changed-and-some-reflections)

### 独立批评来源
- [Safer AI: RSP v3 批评](https://www.safer-ai.org/anthropics-responsible-scaling-policy-update-makes-a-step-backwards)
- [Zvi Mowshowitz: RSP v3 分析](https://thezvi.substack.com/p/anthropic-responsible-scaling-policy)
- [EA Forum: Anthropic Backpedalling](https://forum.effectivealtruism.org/posts/kMpf7nYRpTkGh2Qfa/anthropic-is-quietly-backpedalling-on-its-safety-commitments)
- [LessWrong: Don't Rely on a Race to the Top](https://www.lesswrong.com/posts/LFxdvPiksvLHA58Mx/don-t-rely-on-a-race-to-the-top)
- [Marketplace: Anthropic Loosens Safety Pledge](https://www.marketplace.org/story/2026/02/25/anthropic-loosens-safety-pledge-to-compete-with-its-ai-peers)
- [Big Technology: Google Struggles to Support Anthropic](https://www.bigtechnology.com/p/google-struggles-to-support-anthropic)
